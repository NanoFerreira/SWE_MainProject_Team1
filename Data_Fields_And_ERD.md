# Car Sales E-Commerce JSON Data Model

This document defines the JSON structure for the Car Sales E‑Commerce Application. It includes:

- **Field Definitions**: JSON properties, data types, and descriptions for each entity.
- **Example Data**: Sample records illustrating valid JSON entries.
- **Seed Data**: Initial data loaded on first run (e.g., default admin user, preloaded car listings).

Use this as a reference when integrating the front-end UI with the back-end data layer.

---






### Table: users
| JSON Property | Type    | Description                      |
|---------------|---------|----------------------------------|
| id            | number  | Unique user ID                   |
| username      | string  | User login name                  |
| password      | string  | Hashed password                  |
| email         | string  | Contact email address            |
| is_admin      | boolean | Admin flag                       |
| created_at    | string  | ISO 8601 timestamp of account creation |

---

### Table: cars
| JSON Property           | Type    | Description                                 |
|-------------------------|---------|---------------------------------------------|
| id                      | number  | Unique car ID                               |
| name                    | string  | Car model name                              |
| description             | string  | Brief vehicle description                   |
| price_cents             | number  | Price in cents (base‑10)                    |
| image_url               | string  | URL or path to primary image                |
| sold                    | boolean | Sold status (false = available)             |
| mileage                 | number  | Odometer reading in miles                   |
| vin                     | string  | Vehicle Identification Number               |
| engine_type             | string  | Engine specification (e.g., "2.5L 4-Cylinder") |
| transmission            | string  | Transmission type (e.g., "Automatic")      |
| drivetrain              | string  | Drivetrain configuration (e.g., "FWD")     |
| fuel_type               | string  | Type of fuel (e.g., "Gasoline")            |
| exterior_color          | string  | Exterior paint color                        |
| interior_color          | string  | Interior trim color                         |
| condition               | string  | Condition (e.g., "New", "Used")          |
| created_by              | number  | Admin user ID who added the car             |
| created_at              | string  | ISO 8601 timestamp when entry was created   |

---

### Table: carts
| JSON Property | Type    | Description                          |
|---------------|---------|--------------------------------------|
| id            | number  | Unique cart ID                       |
| user_id       | number  | Owner user ID                        |
| created_at    | string  | ISO 8601 timestamp of cart creation  |

---

### Table: cart_items
| JSON Property | Type    | Description                                 |
|---------------|---------|---------------------------------------------|
| id            | number  | Unique cart item ID                         |
| cart_id       | number  | Reference to cart ID                        |
| car_id        | number  | Reference to car ID                         |
| added_at      | string  | ISO 8601 timestamp when item was added      |

---

### Table: orders
| JSON Property           | Type    | Description                                |
|-------------------------|---------|--------------------------------------------|
| id                      | number  | Unique order ID                            |
| user_id                 | number  | Customer user ID                           |
| subtotal_cents          | number  | Sum of item prices in cents                |
| tax_cents               | number  | Tax amount (6% of subtotal) in cents       |
| shipping_cost_cents     | number  | Shipping cost in cents                     |
| total_cents             | number  | Grand total in cents                       |
| shipping_address        | string  | Delivery address                           |
| phone_number            | string  | Contact phone number                       |
| card_last4              | string  | Last four digits of credit card            |
| exp_month               | number  | Credit card expiration month               |
| exp_year                | number  | Credit card expiration year                |
| cvv                     | string  | Credit card CVV code                       |
| shipping_speed          | string  | Shipping option ("Ground", "3-Day", "Overnight") |
| created_at              | string  | ISO 8601 timestamp of order placement      |

---

### Table: order_items
| JSON Property           | Type    | Description                               |
|-------------------------|---------|-------------------------------------------|
| id                      | number  | Unique order-item ID                       |
| order_id                | number  | Reference to parent order ID               |
| car_id                  | number  | Reference to purchased car ID              |
| price_at_purchase_cents | number  | Price at time of sale in cents             |



---

## Example Data

### Table: users
| id | username | password | email               | is_admin | created_at           |
|----|----------|----------|---------------------|----------|----------------------|
| 1  | admin    | hashed_pw| admin@example.com   | true     | 2025-04-18T10:00:00Z |
| 2  | johndoe  | hashed_pw| johndoe@example.com | false    | 2025-04-18T11:00:00Z |

### Table: cars
| id | name                | description                   | price_cents | image_url           | sold  | mileage | vin               | engine_type    | transmission | drivetrain | fuel_type | exterior_color | interior_color | condition | created_by | created_at           |
|----|---------------------|-------------------------------|-------------|---------------------|-------|---------|-------------------|----------------|--------------|------------|-----------|----------------|----------------|-----------|------------|----------------------|
| 1  | 2022 Toyota Camry   | One-owner, well maintained    | 2599999     | /images/camry.jpg   | false | 15000   | 1HGCM82633A004352  | 2.5L 4-Cylinder| Automatic    | FWD        | Gasoline | Blue           | Black          | Used      | 1          | 2025-04-18T11:00:00Z |

### Table: carts
| id | user_id | created_at           |
|----|---------|----------------------|
| 1  | 2       | 2025-04-18T12:00:00Z |

### Table: cart_items
| id | cart_id | car_id | added_at             |
|----|---------|--------|----------------------|
| 1  | 1       | 1      | 2025-04-18T12:10:00Z |

### Table: orders
| id | user_id | subtotal_cents | tax_cents | shipping_cost_cents | total_cents | shipping_address             | phone_number  | card_last4 | exp_month | exp_year | cvv  | shipping_speed | created_at           |
|----|---------|----------------|-----------|---------------------|-------------|------------------------------|---------------|------------|-----------|----------|------|----------------|----------------------|
| 1  | 2       | 2599999        | 155999    | 0                   | 2755998     | 123 Elm St, Springfield      | 555-123-4567  | 1234       | 12        | 2026     | 123  | Ground         | 2025-04-18T12:15:00Z |

### Table: order_items
| id | order_id | car_id | price_at_purchase_cents |
|----|----------|--------|-------------------------|
| 1  | 1        | 1      | 2599999                 |

---

## Seed Data

### Table: users
| id | username | password | email             | is_admin | created_at           |
|----|----------|----------|-------------------|----------|----------------------|
| 1  | admin    | hashed_pw| admin@example.com | true     | 2025-04-18T10:00:00Z |

### Table: cars
| id | name                | description                   | price_cents | image_url           | sold  | mileage | vin               | engine_type    | transmission | drivetrain | fuel_type | exterior_color | interior_color | condition | created_by | created_at           |
|----|---------------------|-------------------------------|-------------|---------------------|-------|---------|-------------------|----------------|--------------|------------|-----------|----------------|----------------|-----------|------------|----------------------|
| 1  | 2022 Toyota Camry   | One-owner, well maintained    | 2599999     | /images/camry.jpg   | false | 15000   | 1HGCM82633A004352  | 2.5L 4-Cylinder| Automatic    | FWD        | Gasoline | Blue           | Black          | Used      | 1          | 2025-04-18T11:00:00Z |
| 2  | 2020 Honda Accord   | Certified pre-owned, low miles| 2199999     | /images/accord.jpg  | false | 12000   | 1HGCV1F14LA123456  | 1.5L Turbo     | CVT          | FWD        | Gasoline | White          | Gray           | Used      | 1          | 2025-04-18T11:30:00Z |

### Table: carts, cart_items, orders, order_items
- Initialized empty on first run (no records)



## Data Model

### Entity Relationship Diagram
```mermaid
erDiagram
    USER ||--o{ CART : owns
    USER ||--o{ ORDER : places

    CART ||--o{ CART_ITEM : contains
    CART_ITEM }|..|{ CAR : references

    ORDER ||--o{ ORDER_ITEM : contains
    ORDER_ITEM }|..|{ CAR : references

    USER {
        INTEGER id PK
        TEXT username
        TEXT password_hash
        TEXT email
        BOOLEAN is_admin
    }
    CART {
        INTEGER id PK
        INTEGER user_id FK
    }
    CAR {
        INTEGER id PK
        TEXT name
        TEXT description
        DECIMAL price
        TEXT image_url
        BOOLEAN sold
    }
    ORDER {
        INTEGER id PK
        INTEGER user_id FK
        DECIMAL subtotal
        DECIMAL tax
        DECIMAL shipping_cost
        DECIMAL total
        TEXT shipping_address
        TEXT phone_number
        TEXT shipping_speed
        TEXT last4_cc
        DATETIME created_at
    }
    CART_ITEM {
        INTEGER id PK
        INTEGER cart_id FK
        INTEGER car_id FK
        DATETIME added_at
    }
    ORDER_ITEM {
        INTEGER id PK
        INTEGER order_id FK
        INTEGER car_id FK
        DECIMAL price_at_purchase
    }


