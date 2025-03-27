
| **Condition**               | **R1** | **R2** | **R3** | **R4** | **R5** | **R6** | **R7** | **R8** |
|----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|
| C1: Cart has items         |   F    |   F    |   F    |   F    |   T    |   T    |   T    |   T    |
| C2: Shipping info entered  |   F    |   F    |   T    |   T    |   F    |   F    |   T    |   T    |
| C3: Payment info entered   |   F    |   T    |   F    |   T    |   F    |   T    |   F    |   T    |

---

| **Action**                                   | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|---------------------------------------------|----|----|----|----|----|----|----|----|
| A1: Block checkout                          | X  | X  | X  |    | X  |    | X  |    |
| A2: Show Confirm Order page                 |    |    |    | X  |    |    |    | X  |
| A3: Allow completion of order               |    |    |    | X  |    |    |    | X  |
| A4: Deduct inventory & generate receipt     |    |    |    | X  |    |    |    | X  |
| A5: Prevent return to cart after completion |    |    |    | X  |    |    |    | X  |
