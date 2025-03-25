
# Requirements Writing

* The Following Document will list every requirement taken into consideration for the elaboration of this project. Requirements will be separated and categorized according to the version they seek to be implemented in, as well as the Epic that they belong to. Each Requirement, as well as the Epic they belong to, will have a unique ID for ease of access. 

* Requirements will also contain information on their level of priority, estimated effort, and whether or not they qualify as functional requirements. A brief description of the requirement will also be provided.

# Version 1.0

## KM1E-1 User Registration and Authentication
1. KM1S-1
   * **Description:** Users must have the ability to self-register and log-in to the website
   * **Estimated effort:** 1.5 Days
   * **Requirement Type:** Functional
2. KM1S-2
   * **Description:** Admins must be able to log-in, but not self-register.
   * **Estimated effort:** 1.2 Days
   * **Requirement Type:** Functional
3. KM1S-3
   * **Description:** Previous Admins must be able to promote a standard user to admin
   * **Estimated effort:** 0.6 Days
   * **Requirement Type:** Functional
4. KM1S-4
   * **Description:** All users must have a unique username and a minimum 6-character password
   * **Estimated effort:** 0.5 Days
   * **Requirement Type:** Non-Functional
  
## KM1E-2 Inventory Display & Shopping Experience
1. KM2S-1
   * **Description:** Users must have access to a list of the available inventory
   * **Estimated effort:** 3 Days
   * **Requirement Type:** Functional
2. KM2S-2
   * **Description:** Inventory must be sorted by price from highest to lowest.
   * **Estimated effort:** 0.5 Days
   * **Requirement Type:** Non-Functional
3. KM2S-3
   * **Description:** Sold Items must not be displayed
   * **Estimated effort:** 0.6 Days
   * **Requirement Type:** Non-Functional
4. KM2S-4
   * **Description:** Each inventory must include Name, 1+ pictures, price, description, add to cart option
   * **Estimated effort:** 4 Days
   * **Requirement Type:** Functional  
5. KM2S-5
    * **Description:** Price must be stored in decimal/currency format that is base 10. Price must not be a floating point.
   * **Estimated effort:** 0.5 Days
   * **Requirement Type:** Non-Functional

  
## KM1E-3 Shopping Cart & Checkout Process
1. KM3S-1
   * **Description:** Users must be able to add multiple items to their cart
   * **Estimated effort:** 0.7 Days
   * **Requirement Type:** Non-Functional
2. KM3S-2
   * **Description:** Users cannot proceed to checkout if their cart is empty
   * **Estimated effort:** 0.5 Days
   * **Requirement Type:** Non-Functional
3. KM3S-3
   * **Description:** On checkout, users must be able to see a list of cart items, a subtotal cost. They must also have the ability to remove items from the cart.
   * **Estimated effort:** 2.5 Days
   * **Requirement Type:** Functional
4. KM3S-4
   * **Description:** After their cart has been emptied, users are returned to the main screen.
   * **Estimated effort:** 0.7 Days
   * **Requirement Type:** Non-Functional  
5. KM3S-5
    * **Description:** On pay now, Users must enter a shipping address, credit card details, phone number, and a shipping option.
   * **Estimated effort:** 3 Days
   * **Requirement Type:** Functional
     
## KM1E-4 Shopping Cart & Checkout Process
1. KM3S-1
    * **Description:** On order confirmation, the page must deduct items from the inventory, display a receipt, and prevent returning to the payment page.
   * **Estimated effort:** 1 Days
   * **Requirement Type:** Functional
2. KM4S-2
   * **Description:** The receipts must show items purchased, last four digits of the credit card, shipping, and final total
   * **Estimated effort:** 1.5 Days
   * **Requirement Type:** Non-Functional
3. KM4S-3
   * **Description:** The receipt must also be displayed as an electronic message.
   * **Estimated effort:** 1 Day
   * **Requirement Type:** Non-Functional
4. KM4S-4
   * **Description:** Users may click OK to return to their main page. Their purchase items must no longer be visible
   * **Estimated effort:** 0.7 Days
   * **Requirement Type:** Non-Functional  


