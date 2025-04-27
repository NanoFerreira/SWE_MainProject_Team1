## Front‑End Integration & Team Assignments

Below are **required** screens (9 of the 17 total) mapped to backend endpoints — these must be delivered in Version 1. Optional/future screens are listed afterward.

### Required Screens (9/17)
| Screen Name        | Template File       | Endpoint                         | Notes                           |
|--------------------|---------------------|----------------------------------|---------------------------------|
| Main Inventory     | `inventory.html`    | `GET /`                          | shows available cars            |
| Search Results     | Same as Inventory   | `GET /?q=<term>`                 | filters inventory by name/desc  |
| Login              | `login.html`        | `GET/POST /login`                | auth form                       |
| Register           | `register.html`     | `GET/POST /register`             | auth form                       |
| Product Detail     | `inventory.html` or separate detail template| `GET /car/<id>` or modal | shows full car info + Add to Cart |
| Cart View          | `cart.html`         | `GET /cart`                      | list items + remove            |
| Checkout           | `checkout.html`     | `GET/POST /checkout`             | shipping & payment form        |
| Receipt            | `receipt.html`      | `GET /receipt/<order_id>`        | final totals & last-4 card     |
| Admin Orders/Report| `admin_orders.html` | `GET /admin/orders`              | list sales + export CSV        |

### Optional/Future Screens (8/17)
| Screen Name            | Reason                 |
|------------------------|------------------------|
| Profile Page (User)    | Not required V1        |
| Add User / Promote UI  | Manual DB OK V1        |
| Multi‑Image Gallery    | Nice‑to‑have           |
| Advanced Search Filters| Nice‑to‑have           |
| Order History (User)   | Nice‑to‑have           |
| Discount Codes         | Nice‑to‑have           |
| Shipping Tracking      | Nice‑to‑have           |
| Email Integration      | Nice‑to‑have           |


These 9 required screens cover the core user journey and admin features defined in the spec. The remaining 8 can be scheduled for later sprints.

## Updated Team Division (Version 1 Only)
Assign the **9 required screens** evenly between two developers:

| Developer A                        | Developer B                        |
|------------------------------------|------------------------------------|
| **Auth & Inventory**               | **Cart & Checkout**                |
| - `login.html`, `register.html`    | - `cart.html`, remove-item UI      |
| - `inventory.html` (incl. search)  | - `checkout.html`                  |
| - Product Detail view (Add to Cart)| - `receipt.html`                   |
|                                    |                                    |
| **Admin Reporting**                | **(No additional tasks)**          |
| - `admin_orders.html` listing      |                                    |
| - CSV Export button                |                                    |

> Both developers integrate the global `_nav.html` partial into their assigned screens for consistent navigation.

This split gives each developer **5** and **4** required templates, respectively, ensuring balanced workload and rapid delivery of Version 1.
