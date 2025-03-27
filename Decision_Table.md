

###  Conditions (Causes)

| **Condition**                        | **R1** | **R2** | **R3** | **R4** | **R5** | **R6** |
|-------------------------------------|--------|--------|--------|--------|--------|--------|
| C1: User is logged in               | T      | T      | T      | T      | F      | T      |
| C2: Cart has items                  | F      | T      | T      | T      | T      | T      |
| C3: All items are available         | -      | F      | T      | T      | T      | T      |
| C4: Shipping info entered           | -      | -      | F      | T      | T      | T      |
| C5: Payment info entered            | -      | -      | F      | T      | T      | F      |

---

###  Actions (Effects)

| **Action**                                      | R1 | R2 | R3 | R4 | R5 | R6 |
|------------------------------------------------|----|----|----|----|----|----|
| A1: Block checkout                             | T  | T  | T  | F  | T  | T  |
| A2: Show Confirm Order page                    | F  | F  | F  | T  | F  | F  |
| A3: Allow order completion                     | F  | F  | F  | T  | F  | F  |
| A4: Deduct inventory and generate receipt      | F  | F  | F  | T  | F  | F  |
| A5: Prevent return to cart after order         | F  | F  | F  | T  | F  | F  |
