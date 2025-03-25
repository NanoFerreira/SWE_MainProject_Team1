# Team 1 - Intro to SWE project

• Welcome to Team 1’s project repository for SWE 3313, (Introduction to Software Engineering). Our Presentations, Documentation, Source code, and artifacts will be located here and updated as the project continues.


• For our application we are designing an E-Commerce vehicle website In Python using Flask and JSON In order to create a vehicle marketplace. 

• We are excited to show you our process through the different aspects of our software engineering work! Check out the sections below and follow the links for more details. Thank you for taking the time to explore our work!

## Meet our Team

•Aaron Yemisrach   [Resume](Aaron_Resume.md)

•Bryan Julius      [Resume](Bryan_Resume.md)

•Juan Ferreira     [Resume](Juan_Resume.md)

## Team Assignments 
•To distribute work efficiently for this project, we are dividing our workflow in two different ways. 
- For each of the main three project Sprints (UI, Technology, Implementation), we have delegated a lead programmer for each sprint. We will all share the workload for each sprint. The lead programmer will focus on laying the foundation for each respective sprint.
- Additionally, we have divided our roles in a general sense throughout all sprints. To ensure proper communication and documentation, each member will deal with future expectations, current performance, backlogging, and feedback.

• Click [here](TeamAssignments.md) for a detailed breakdown of each of the team member's roles.

## Technology Selection
To build our application, we will be coding in Python using Flask. We will use a JSON database to store user and item attributes.

Click [here](Technology_Description.md) for a detailed explanation of the technologies and tools we are using and why.

## Gantt Chart

Click [here](https://motorsports.youtrack.cloud/gantt-charts/226-0) to view our project plan Gantt Chart in YouTrack.

## Video Presentations
For all our video presentations and tech demos, you can access them [here](Video_Presentations.md)


# Project Requirements

In this section of the document, we will specify every requirement that we seek to meet during the duration of the project. All specific features, logic, and use cases will be presented here. These requirements have been selected based on our scope, taking the requests made in the client's elicitation.

You may go to the Video Presentations section of the document to find the presentation related to the Project Requirements, as well as all future presentations.

## Requirements

- Click [here](Requirement_Writing.md) for a detailed breakdown of what requirements will be taken into account and prioritized.
  
- Click [here](1.0_Version_Expectations.md) for an exploration on what requirements will be implemented for version 1.0.

## Use case Diagram

- Click [here]() for a Diagram dissecting the different use cases clients and admins may go through. 

- Click [here]() for a Decision table detailing the thought process that goes behind each of the users and admins can perform.

- ## Decision Table
  


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





