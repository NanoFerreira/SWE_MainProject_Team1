# app.py
import os, json
import sys
from threading import Lock
from datetime import datetime
from io import StringIO
import csv

from flask import (
    Flask, request, session, redirect, url_for,
    render_template, flash, jsonify, send_file,
    abort
)
from werkzeug.security import generate_password_hash, check_password_hash

# -----------------------------------------------------------------------------
# JSON Storage Utils
# -----------------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)
_file_lock = Lock()

def _path(name):
    return os.path.join(DATA_DIR, f"{name}.json")

def load_data(name):
    p = _path(name)
    if not os.path.exists(p):
        return []
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(name, data):
    p = _path(name)
    tmp = p + '.tmp'
    with _file_lock:
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, p)

def next_id(lst):
    return max((item['id'] for item in lst), default=0) + 1


# -----------------------------------------------------------------------------
# App Setup
# -----------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret')


# -----------------------------------------------------------------------------
# Auth Helpers
# -----------------------------------------------------------------------------
def current_user():
    uid = session.get('user_id')
    if not uid:
        return None
    return next((u for u in load_data('users') if u['id']==uid), None)

@app.context_processor
def inject_user():
    return dict(current_user=current_user)


def login_required(fn):
    def wrapper(*a, **k):
        if not current_user():
            flash("Login required.")
            return redirect(url_for('login'))
        return fn(*a, **k)
    wrapper.__name__ = fn.__name__
    return wrapper

def admin_required(fn):
    def wrapper(*a, **k):
        user = current_user()
        if not user or not user['is_admin']:
            return "Forbidden", 403
        return fn(*a, **k)
    wrapper.__name__ = fn.__name__
    return wrapper


# --------------------------------------------------------------------------
# one-time migration: convert any remaining plain-text → pbkdf2 hashes
# --------------------------------------------------------------------------
from werkzeug.security import generate_password_hash

USERS = load_data('users')
changed = False
for u in USERS:
    pw = u['password']
    if not pw.startswith('pbkdf2:'):          # still plain-text
        u['password'] = generate_password_hash(
            pw,
            method="pbkdf2:sha256",                       # <-- fixed algo
            salt_length=16
        )
        changed = True

if changed:
    save_data('users', USERS)




# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        users = load_data('users')
        uname = request.form['username']
        pw = request.form['password']
        if len(pw) < 6:
            flash("Password must be ≥6 characters.")
            return redirect(url_for('register'))
        if any(u['username']==uname for u in users):
            flash("Username taken.")
            return redirect(url_for('register'))
        new = {
            'id': next_id(users),
            'username': uname,
            'password': generate_password_hash(pw),
            'email': request.form['email'],
            'is_admin': False,
            'created_at': datetime.utcnow().isoformat()
        }
        users.append(new)
        save_data('users', users)
        session['user_id'] = new['id']
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login():
    print("✨ HIT /login (", request.method, ") ✨")
    if request.method == 'POST':
        print("FORM DATA:", dict(request.form))    # ← what did the browser send?
        users = load_data('users')
        print("LOADED USERS:", users)               # ← what is in your JSON?
        user = next((u for u in users if u['username']==request.form['username']), None)
        print("LOOKUP USER:", user)
        if user:
            ok = check_password_hash(user['password'], request.form['password'])
            print("PASSWORD OK?", ok)
        if user and ok:
            session['user_id'] = user['id']
            print("→ redirecting to index as user", user['username'])
            return redirect(url_for('index'))
        flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/')
def index():
    q = request.args.get('q','').lower()
    cars = [c for c in load_data('cars') if not c['sold']]
    if q:
        cars = [
            c for c in cars
            if q in c['name'].lower() or q in c['description'].lower()
        ]
    cars.sort(key=lambda c: c['price_cents'], reverse=True)
    return render_template('inventory.html', cars=cars, show_search=True)



# app.py
@app.route('/car/<int:car_id>')
@login_required
def car_detail(car_id):
    cars = load_data('cars')
    car  = next((c for c in cars if c['id']==car_id), None)
    if not car or car['sold']:
        abort(404)
    return render_template('car_detail.html', car=car)



@app.route('/cart/add/<int:car_id>', methods=['POST'])
@login_required
def add_to_cart(car_id):
    user = current_user()
    cars = load_data('cars')
    car = next((c for c in cars if c['id']==car_id), None)
    if not car or car['sold']:
        flash("Car not available.")
        return redirect(url_for('index'))

    carts = load_data('carts')
    cart = next((ct for ct in carts if ct['user_id']==user['id']), None)
    if not cart:
        cart = {'id': next_id(carts), 'user_id': user['id'], 'created_at': datetime.utcnow().isoformat()}
        carts.append(cart)
        save_data('carts', carts)

    cis = load_data('cart_items')
    cis.append({
        'id': next_id(cis),
        'cart_id': cart['id'],
        'car_id': car_id,
        'added_at': datetime.utcnow().isoformat()
    })
    save_data('cart_items', cis)
    return redirect(url_for('view_cart'))


@app.route("/cart")
@login_required
def view_cart():
    user = current_user()                  # the logged-in user

    carts       = load_data("carts")       # header rows
    cart_items  = load_data("cart_items")  # detail rows
    cars        = load_data("cars")

    # --- 1) find this user’s cart header -----------------------------
    cart = next((c for c in carts if c["user_id"] == user["id"]), None)
    if not cart:                     # user has nothing in the cart yet
        return render_template("cart.html",
                               cart_items=[],
                               subtotal_cents=0,
                               tax_cents=0,
                               total_cents=0)

    # --- 2) detail rows that belong to *that* cart -------------------
    rows_for_user = [ci for ci in cart_items if ci["cart_id"] == cart["id"]]

    # --- 3) enrich rows with car data + money --------------------------
    items = []
    subtotal_cents = 0

    for row in rows_for_user:
        car = next(c for c in cars if c["id"] == row["car_id"])
        price = car["price_cents"]

        subtotal_cents += price
        items.append({
            "id":          row["id"],      # primary-key of cart-item
            "car_id":      car["id"],
            "name":        car["name"],
            "price_cents": price
    })

    tax_cents   = int(subtotal_cents * 0.06)
    total_cents = subtotal_cents + tax_cents
    print("cart_items →", cart_items, file=sys.stderr)



    return render_template(
        "cart.html",
        cart_items     = items,
        subtotal_cents = subtotal_cents,
        tax_cents      = tax_cents,
        total_cents    = total_cents
    )



@app.route("/cart/remove/<int:item_id>", methods=["POST"])
@login_required
def remove_from_cart(item_id):
    """
    Delete a single CartItem (id == item_id) that belongs
    to the current user’s open cart, then redirect back to /cart
    """
    user      = current_user()                # however you get the session user
    carts     = load_data('carts')
    cart_items= load_data('cart_items')

    # ► find the “open” cart that belongs to this user
    cart = next((c for c in carts if c["user_id"] == user["id"]), None)
    if not cart:
        flash("Cart not found")
        return redirect(url_for('view_cart'))

    # ► remove the cart-item
    new_items = [ci for ci in cart_items if ci["id"] != item_id]
    save_data('cart_items', new_items)         # whatever helper you use

    return redirect(url_for('view_cart'))



@app.route('/checkout', methods=['GET','POST'])
@login_required
def checkout():
    user = current_user()
    # load this user's cart
    carts = load_data('carts')
    cart = next((ct for ct in carts if ct['user_id']==user['id']), None)
    if not cart:
        flash("Your cart is empty.")
        return redirect(url_for('index'))

    # gather items
    cis = load_data('cart_items')
    my_items = [ci for ci in cis if ci['cart_id']==cart['id']]
    if not my_items:
        flash("Your cart is empty.")
        return redirect(url_for('index'))

    cars = load_data('cars')
    items = [ next(c for c in cars if c['id']==ci['car_id']) for ci in my_items ]

    # compute costs
    subtotal = sum(i['price_cents'] for i in items)
    tax      = int(subtotal * 0.06)
    shipping_options = {'Ground':0,'3-Day':1900,'Overnight':2900}

    if request.method == 'POST':
        # pull form fields (must match your curl -F names exactly)
        addr    = request.form['shipping_address']
        phone   = request.form['phone_number']
        card    = request.form['card_number']
        exp_m   = int(request.form['exp_month'])
        exp_y   = int(request.form['exp_year'])
        cvv     = request.form['cvv']
        speed   = request.form['shipping_speed']
        ship_ct = shipping_options[speed]

        # create order record
        orders = load_data('orders')
        oid = max((o['id'] for o in orders), default=0) + 1
        order = {
            'id': oid,
            'user_id': user['id'],
            'subtotal_cents': subtotal,
            'tax_cents': tax,
            'shipping_cost_cents': ship_ct,
            'total_cents': subtotal + tax + ship_ct,
            'shipping_address': addr,
            'phone_number': phone,
            'card_last4': card[-4:],
            'exp_month': exp_m,
            'exp_year': exp_y,
            'cvv': '***',  # never store CVV in plaintext
            'shipping_speed': speed,
            'created_at': datetime.utcnow().isoformat()
        }
        orders.append(order)
        save_data('orders', orders)

        # record order_items + mark cars sold
        ois = load_data('order_items')
        for c in items:
            ois.append({
                'id': max((x['id'] for x in ois), default=0) + 1,
                'order_id': oid,
                'car_id': c['id'],
                'price_at_purchase_cents': c['price_cents']
            })
            c['sold'] = True
        save_data('order_items', ois)
        save_data('cars', cars)

        # clear out this cart
        new_ci = [ci for ci in cis if ci['cart_id'] != cart['id']]
        save_data('cart_items', new_ci)

        return redirect(url_for('receipt', order_id=oid))

    # GET → render the checkout form
    return render_template(
        'checkout.html',
        items=items,
        subtotal=subtotal,
        tax=tax,
        shipping_options={k:v//100 for k,v in shipping_options.items()}
    )



@app.route('/receipt/<int:order_id>')
@login_required
def receipt(order_id):
    # 1) Who’s making this request?
    user = current_user()

    # 2) Load orders.json and find the one they asked for
    orders = load_data('orders')
    order = next((o for o in orders if o['id'] == order_id), None)

    # 3) If it doesn’t exist or isn’t theirs → 404
    if not order or order['user_id'] != user['id']:
        # debug prints (you can remove these once it’s working)
        print("loaded orders:", orders)
        print("current user:", user)
        print("looking for order_id:", order_id)
        abort(404)

    # 4) Gather the line‐items + car details
    cars = load_data('cars')
    order_items = load_data('order_items')
    items = [
        { **oi,
          **next(c for c in cars if c['id'] == oi['car_id'])
          }
        for oi in order_items
        if oi['order_id'] == order_id
    ]

    # 5) Render the template, passing both order & user
    return render_template(
        'receipt.html',
        order=order,
        items=items,
        user=user
    )


@app.route('/admin/orders')
@admin_required
def admin_orders():
    orders = load_data('orders')
    return render_template('admin_orders.html', orders=orders)


@app.route('/admin/export')
@admin_required
def export_csv():
    orders = load_data('orders')
    users = {u['id']:u for u in load_data('users')}
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['order_id','user','total'])
    for o in orders:
        cw.writerow([o['id'], users[o['user_id']]['username'], o['total_cents']/100])
    si.seek(0)
    return send_file(si, as_attachment=True,
                     attachment_filename='sales.csv',
                     mimetype='text/csv')



# ──────────────────────────────────────────────────────────────
#  ADMIN PANEL (simple promote / receipt lookup)
# ──────────────────────────────────────────────────────────────
@app.route('/admin', methods=['GET'])
@admin_required
def admin_panel():
    """
    When GET has ?order_id=N we fetch that order + its items
    so the template can show the mini-receipt.
    """
    order_id = request.args.get('order_id', type=int)
    order, items = None, None
    if order_id:
        orders      = load_data('orders')
        order_items = load_data('order_items')
        cars        = load_data('cars')

        order = next((o for o in orders if o['id'] == order_id), None)
        if order:
            items = [
                {**oi,
                 **next(c for c in cars if c['id']==oi['car_id'])}
                for oi in order_items
                if oi['order_id'] == order_id
            ]
        else:
            flash(f"Order {order_id} not found.")

    return render_template('admin_panel.html', order=order, items=items)


@app.route('/admin/promote', methods=['POST'])
@admin_required
def admin_promote():
    users = load_data('users')
    uname = request.form['username'].strip()
    user  = next((u for u in users if u['username'] == uname), None)
    if not user:
        flash(f"User “{uname}” not found.")
    elif user['is_admin']:
        flash(f"{uname} is already an admin.")
    else:
        user['is_admin'] = True
        save_data('users', users)
        flash(f"{uname} promoted to admin.")
    return redirect(url_for('admin_panel'))


@app.route('/admin/receipt/<int:order_id>')
@admin_required
def admin_receipt(order_id):
    """Full receipt view (uses the existing receipt template)."""
    orders = load_data('orders')
    order  = next((o for o in orders if o['id']==order_id), None)
    if not order:
        abort(404)

    # reuse the logic the normal receipt route uses
    cars        = load_data('cars')
    order_items = load_data('order_items')
    items = [
        { **oi,
          **next(c for c in cars if c['id']==oi['car_id']) }
        for oi in order_items
        if oi['order_id']==order_id
    ]
    return render_template('receipt.html',
                           order=order,
                           items=items,
                           user=current_user())   # admin user


# ──────────────────────────────────────────────────────────────────
#  ADMIN – DASHBOARD, ADD-INVENTORY, CSV EXPORT
# ──────────────────────────────────────────────────────────────────
@app.route("/admin")
@admin_required
def admin_dashboard():
    """Main admin page: list every purchased car + purchaser."""
    orders       = load_data("orders")
    order_items  = load_data("order_items")
    users        = {u["id"]: u for u in load_data("users")}
    cars         = {c["id"]: c for c in load_data("cars")}

    # bundle one row per purchased car
    rows = []
    for oi in order_items:
        order  = next(o for o in orders if o["id"] == oi["order_id"])
        buyer  = users[order["user_id"]]["username"]
        car    = cars[oi["car_id"]]
        rows.append({
            "order_id": order["id"],
            "car_name": car["name"],
            "price":    oi["price_at_purchase_cents"],
            "buyer":    buyer
        })

    return render_template("admin_dashboard.html", rows=rows)


@app.route("/admin/add_car", methods=["POST"])
@admin_required
def admin_add_car():
    """Simple form handler to append one car to cars.json."""
    cars = load_data("cars")
    cars.append({
        "id":           next_id(cars),
        "name":         request.form["name"],
        "description":  request.form["description"],
        "price_cents":  int(float(request.form["price"])*100),
        "image_url":    request.form["image_url"] or "placeholder.png",
        "sold":         False,
        "mileage":      int(request.form["mileage"] or 0),
        "vin":          request.form["vin"],
        "engine_type":  request.form["engine_type"],
        "transmission": request.form["transmission"],
        "drivetrain":   request.form["drivetrain"],
        "fuel_type":    request.form["fuel_type"],
        "exterior_color": request.form["exterior_color"],
        "interior_color": request.form["interior_color"],
        "condition":    request.form["condition"],
        "created_by":   current_user()["id"],
        "created_at":   datetime.utcnow().isoformat()
    })
    save_data("cars", cars)
    flash("Car added.")
    return redirect(url_for("admin_dashboard"))




@app.route('/test_checkout')
def test_checkout():
    return render_template('test_checkout.html')


# debug: print all URL rules on startup
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint:20s} {','.join(rule.methods):40s} {rule}")


if __name__=='__main__':
    app.run(debug=True)
