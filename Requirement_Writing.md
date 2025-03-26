
# Requirements Writing

* The Following Document will list every requirement considered for the elaboration of this project. Requirements will be separated and categorized according to the version they seek to be implemented in, as well as the Epic that they belong to. Each Requirement, as well as the Epic they belong to, will have a unique ID for ease of access. 

* Requirements will also contain information on their priority level, estimated effort, and whether or not they qualify as functional requirements. A brief description of the requirements will also be provided.

# Version 1.0



## Milestone 1

### KM1E-1 User Registration and Authentication
1. KM1S-1
   * **Description:** Users must have the ability to self-register and log in to the website
   * **Estimated effort:** 1.5 Days
   * **Requirement Type:** Functional
2. KM1S-2
   * **Description:** Admins must be able to log, in but not self-register.
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
  
### KM1E-2 Inventory Display & Shopping Experience
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
    * **Description:** Price must be stored in decimal/currency format that is base 10. The price must not be a floating point.
   * **Estimated effort:** 0.5 Days
   * **Requirement Type:** Non-Functional


  
## Milestone 2
  
### KM2E-3 Shopping Cart & Checkout Process
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
    * **Description:** On Pay Now, Users must enter a shipping address, credit card details, phone number, and a shipping option.
   * **Estimated effort:** 3 Days
   * **Requirement Type:** Functional
     
### KM2E-4 Receipts and Order Confirmation
1. KM4S-1
   * **Description:** On order confirmation, the page must deduct items from the inventory, display a receipt, and prevent returning to the payment page.
   * **Estimated effort:** 1 Days
   * **Requirement Type:** Functional
2. KM4S-2
   * **Description:** The receipts must show items purchased, the last four digits of the credit card, shipping, and the final total
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



## Milestone 3:

### KM3E-5 Admin Features
1. KM5S-1
   * **Description:** Admins must be able to view sales reports. They must show purchased items, customer, and receipt
   * **Estimated effort:** 2 Days
   * **Requirement Type:** Functional
2. KM5S-2
   * **Description:** Admins must have the ability to export sales reports.
   * **Estimated effort:** 1.5 Days
   * **Requirement Type:** Functional
3. KM5S-3
   * **Description:** Admins must be able to add inventory to the system.
   * **Estimated effort:** 1 Day
   * **Requirement Type:** Functional
  
# Future Versions

1. KMFS-1 
   * **Description:** Multiple pictures per inventory item.
   * **Estimated effort:** 0.7 Days
   * **Requirement Type:** Non-Functional
2. KMFS-2 
   * **Description:** Admins being promoted through UI
   * **Estimated effort:** 1.4 Day
   * **Requirement Type:** Non-Functional
3. KMFS-3 
   * **Description:** Ability to place filters and sorting when searching
   * **Estimated effort:** 1 Day
   * **Requirement Type:** Non-Functional
4. KMFS-4 
   * **Description:** Email integration for sending email receipts
   * **Estimated effort:** 1,5 Days
   * **Requirement Type:** Functional
5. KMFS-5 
   * **Description:** Automated inventory entry
   * **Estimated effort:** 2 Days
   * **Requirement Type:** Functional
6. KMFS-6 
   * **Description:** Shipping tracking integration that updates order status.
   * **Estimated effort:** 2-3 Days
   * **Requirement Type:** Functional
7. KMFS-7
   * **Description:** User order history page to review past purchases
   * **Estimated effort:** 1 Day
   * **Requirement Type:** Non-Functional
8. KMFS-8
   * **Description:** Discount codes for promotional pricing
   * **Estimated effort:** 0.7 Days
   * **Requirement Type:** Non-Functional

