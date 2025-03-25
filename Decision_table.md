# Decision Table
  


| Condition / Rule                                                                 | Registered User | Admin |
|----------------------------------------------------------------------------------|------------------|--------|
| Can self-register                                                                | Yes              | No     |
| Can log in                                                                       | Yes              | Yes    |
| Must have unique username                                                        | Yes              | Yes    |
| Must have min 6-character password                                               | Yes              | Yes    |
| Can promote user to admin                                                        | No               | Yes    |
| Can view available inventory (sorted high → low)                                 | Yes              | Yes    |
| Sold items hidden from inventory                                                 | Yes              | Yes    |
| Inventory shows name                                                             | Yes              | Yes    |
| Inventory shows at least one picture                                             | Yes              | Yes    |
| Inventory shows price in $X,XXX.XX format                                        | Yes              | Yes    |
| Price stored as decimal (base 10)                                                | Yes              | Yes    |
| Inventory shows brief description                                                | Yes              | Yes    |
| Inventory item has “Add to Cart” button                                          | Yes              | Yes    |
| Can search inventory by name/description                                         | Yes              | Yes    |
| Can add multiple items to cart                                                   | Yes              | Yes    |
| Cannot checkout with empty cart                                                  | Yes (Blocked)    | Yes (Blocked) |
| Can view cart items and subtotal at checkout                                     | Yes              | Yes    |
| Can remove items from cart                                                       | Yes              | Yes    |
| Emptying cart returns user to main screen                                        | Yes              | Yes    |
| “Pay Now” requires shipping address                                              | Yes (Required)   | Yes    |
| “Pay Now” requires credit card (number, exp, CVV)                                | Yes (Required)   | Yes    |
| “Pay Now” requires phone number                                                  | Yes (Required)   | Yes    |
| “Pay Now” requires shipping speed selection                                      | Yes (Required)   | Yes    |
| “Confirm Order” shows item list, subtotal, 6% tax, shipping, grand total         | Yes              | Yes    |
| Can return to checkout or main page from Confirm Order                           | Yes              | Yes    |
| “Complete Order” deducts items from inventory                                    | Yes              | Yes    |
| “Complete Order” generates and displays receipt                                  | Yes              | Yes    |
| Cannot return to cart/payment after “Complete Order”                             | Yes (Blocked)    | Yes (Blocked) |
| Receipt shows items purchased                                                    | Yes              | Yes    |
| Receipt shows last four digits of credit card                                    | Yes              | Yes    |
| Receipt shows shipping address                                                   | Yes              | Yes    |
| Receipt shows final total                                                        | Yes              | Yes    |
| Receipt displayed as email preview                                               | Yes              | Yes    |
| Can click OK to return to main page                                              | Yes              | Yes    |
| Purchased items no longer visible on main page                                   | Yes              | Yes    |
| Can view sales reports (items + purchaser)                                       | No               | Yes    |
| Can click item in sales report to view its receipt                               | No               | Yes    |
| Can export sales report to CSV                                                   | No               | Yes    |
| Can add inventory to system (via UI or manual entry)                             | No               | Yes    |
| High-fidelity mockup must be created before development starts                   | Yes              | Yes    |
