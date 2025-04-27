## Front‑End Integration & Team Assignments

Below are required‑only screens mapped to backend endpoints, plus front‑end guidelines and a two‑person division of work that aligns with our JSON data model and naming conventions.

### 1. Endpoint & Template Mapping
| Screen Name        | Template File       | Endpoint                         | Data Context Variable |
|--------------------|---------------------|----------------------------------|-----------------------|
| Main Inventory     | `inventory.html`    | `GET /`                          | `cars`                |
| Search Results     | Same as Inventory   | `GET /?q=<term>`                 | `cars`                |
| Cart View          | `cart.html`         | `GET /cart`                      | `items`               |
| Add to Cart        | N/A (button action) | `POST /cart/add/<car_id>`        | N/A                   |
| Checkout Form      | `checkout.html`     | `GET /checkout`                  | `items, subtotal, tax, shipping_options` |
| Checkout Submit    | N/A (form action)   | `POST /checkout`                 | Form fields           |
| Receipt View       | `receipt.html`      | `GET /receipt/<order_id>`        | `order, items`        |
| Admin Orders       | `admin_orders.html` | `GET /admin/orders`              | `orders`              |
| CSV Export         | N/A (button action) | `GET /admin/export`              | N/A                   |

### 2. Naming & Folder Conventions
- **Templates**: store all Jinja files in `/templates` with snake_case names matching the table above.
- **Static Assets**: images go in `/static/images`; reference via `url_for('static', filename='images/<name>')`.
- **CSS/JS Files**: place under `/static/css` and `/static/js`, named `<screen>.css` or `<screen>.js`.
- **Forms & Actions**: use RESTful URLs; form `action` attributes must exactly match the endpoints above.
- **Variable Binding**: Jinja context variable names equal JSON property names (e.g. `car.name`, `item.price_cents`).

### 3. Team Division (2 Front‑End Developers)

| Developer A                        | Developer B                         |
|------------------------------------|-------------------------------------|
| **User & Auth Flow**               | **Shopping Flow**                   |
| - `login.html`, `register.html`    | - `inventory.html` & search         |
| - Flash messages & error display   | - Add-to-cart buttons & UI states   |
| - Profile page (optional bonus)    | - `cart.html`, remove-item links    |
|                                    | - `checkout.html`, form validation  |
| **Admin Screens**                  | **Receipt & Export**                |
| - `admin_orders.html` listing      | - `receipt.html` styling            |
| - Promote‑user UI (future)         | - CSV export button triggers        |
| - Secure link logic (admin only)   |   download of `sales.csv`           |

> **Note:** Both developers share responsibility for including the `_nav.html` partial at the top of each template for consistent navigation.

These assignments cover all **required** features. Nice‑to‑haves (multiple pictures, SendGrid, history page) can be added after core delivery.
