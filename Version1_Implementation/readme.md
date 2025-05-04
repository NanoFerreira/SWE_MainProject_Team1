# Kennesaw Motorsports – Used‑Car Storefront  

---

## 1 · What the application does (end‑user view)

| Role | Capabilities |
|------|--------------|
| Shopper | Browse inventory (price‑sorted) · search · add to cart · checkout · view receipt |
| Admin   | Promote users · add inventory · see all orders (click for receipt) · export sales to **CSV** |

Data persists as JSON in **/data/**, so nothing is lost between sessions.

---

## 2 · Environment requirements

| Item    | Tested on | Notes |
|---------|-----------|-------|
| **OS**  | Windows 10/11| No OS‑specific calls |
| **Python** | 3.11 (min 3.9) | Verify with `python --version` |
| **Browser** | Any modern Chromium / Firefox | Edge 123 used during development |

---

## 3 · Quick‑start (clean machine)

```bash
# 1) clone the repo
git clone https://github.com/NanoFerreira/SWE_MainProject_Team1.git
cd SWE_MainProject_Team1/Version1_Implementation
you can also do this on github without command line
# 2) create & activate a virtual‑env    (macOS/Linux: source venv/bin/activate)
python -m venv venv
venv\Scripts\activate

You can also use any ide that supports python to run a virtual environment.

# 3) **install all dependencies in one line – NO requirements.txt**
pip install Flask passlib[bcrypt,scrypt] python-dotenv

We have few dependencies so its basically just flask and the password library as long as you have python installed.

# 4) (optional) load sample data
python seed_data.py

Note this is not necessary because we have sample data already loaded in the json files in github. If you run the seed_data.py
 file it will change the User json files containing usernames and passwords among other data. I would reccomend not doing
  this unless you lost the original files for whatever reason.

# 5) run the site
python app.py
# └── open  http://127.0.0.1:5000  in your browser

If you don't run the seed_data file the original login will be (Recommended) 
username: admin
password: password

If you run the seed_data file
 The original admin username and password should be 
username: admin
password: <hashed_pw_here>

typed exactly like that with the angle brackets. After you run it once 
and for any password you make after initial run it will be stored in the user.json file but it will be a hashed version 
so even an admin will not be able to read plaintext passwords. 

So be careful not to forget passwords in version 1. If you absolutely have to you can edit the user.json manually to type in a password in plaintext which will then get hashed at next run of the app.py file. 

Adding inventory is fairly easy because variables are named well just be aware that prices are stored in cents not dollars and images need to be provided in the /static/image folder. 

here is what your folder hierarchy should look like 

Version1_Implementation/
├─ app.py              ← main Flask app
├─ seed_data.py        ← optional demo‑data loader
├─ /templates/         ← Jinja2 HTML templates
├─ /static/
│   ├─ css/styles.css
│   └─ images/…        ← all images referenced by the app
├─ /data/              ← *.json (persistent storage)
└─ README.md           ← this file



static holds the images folder and css style sheet and data holds all the json files it should be pretty clear and laid out correctly the way we uploaded it on github but if anything changes it or it fails to clone correctly this is how the files should be arranged 
