# seed_data.py
import os, json
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def write(name, obj):
    with open(os.path.join(DATA_DIR, f"{name}.json"), 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2)

now = datetime.utcnow().isoformat()

# 1) users.json with one admin
users = [
    {
        "id": 1,
        "username": "admin",
        "password": "<hashed_pw_here>",  # use werkzeug to hash or just dummy
        "email": "admin@example.com",
        "is_admin": True,
        "created_at": now
    },
    {
        "id": 2,
        "username": "johndoe",
        "password": "<hashed_pw_here>",
        "email": "johndoe@example.com",
        "is_admin": False,
        "created_at": now
    }
]

# 2) cars.json with 3 sample listings
cars = [
    {
        "id": 1,
        "name": "2021 Hyundai Sonata",
        "description": "Super clean, low mileage sedan.",
        "price_cents": 2200000,
        "image_url": "/images/sonata.jpg",
        "sold": False,
        "mileage": 45000,
        "vin": "5NPEF4JA0MH123456",
        "engine_type": "2.5L 4-Cylinder",
        "transmission": "Automatic",
        "drivetrain": "FWD",
        "fuel_type": "Gasoline",
        "exterior_color": "Red",
        "interior_color": "Black",
        "condition": "Used",
        "created_by": 1,
        "created_at": now
    },
    {
        "id": 2,
        "name": "2020 Toyota Corolla",
        "description": "Nearly new, great fuel economy.",
        "price_cents": 1500000,
        "image_url": "/images/corolla.jpg",
        "sold": False,
        "mileage": 30000,
        "vin": "JTDBR32E720061234",
        "engine_type": "1.8L 4-Cylinder",
        "transmission": "Automatic",
        "drivetrain": "FWD",
        "fuel_type": "Gasoline",
        "exterior_color": "White",
        "interior_color": "Gray",
        "condition": "Used",
        "created_by": 1,
        "created_at": now
    },
    {
        "id": 3,
        "name": "2018 Ford Focus",
        "description": "Sporty hatchback, fun to drive.",
        "price_cents": 1100000,
        "image_url": "/images/focus.jpg",
        "sold": False,
        "mileage": 60000,
        "vin": "1FADP3F21JL123456",
        "engine_type": "2.0L 4-Cylinder",
        "transmission": "Manual",
        "drivetrain": "FWD",
        "fuel_type": "Gasoline",
        "exterior_color": "Blue",
        "interior_color": "Black",
        "condition": "Used",
        "created_by": 1,
        "created_at": now
    }
]

# Empty arrays for the rest
empty = []

write('users', users)
write('cars', cars)
write('carts', empty)
write('cart_items', empty)
write('orders', empty)
write('order_items', empty)

print("Seed data written to data/*.json")
