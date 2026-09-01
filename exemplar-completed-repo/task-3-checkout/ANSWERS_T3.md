# Task 3: Applied Implementation, Answers

Complete this alongside `BRIEF_T3.md`.

## Explain your approach

### 1. Why does `apply_discount_code` call `apply_standard_discount` instead of repeating its logic?

> Because `apply_standard_discount` already has the 10%-over-£50 rule written in it, so calling it means I don't have to write that logic out a second time. If I'd copied it into `apply_discount_code` as well and the shop ever changed the standard discount rule, for example to over £60 instead of £50, I'd have to remember to change it in two separate places, and it would be easy to forget one of them and end up with the two versions disagreeing.

### 2. Trace `print_order_summary("Pen", 2.00, 2, "invalid")`

> `subtotal = 2.00 * 2 = 4.00`. `"invalid"` is lowercase so `validate_discount_code` returns `False`, so `apply_discount_code` falls back and calls `apply_standard_discount(4.00)` instead. Since 4.00 is not over £50, no discount applies, so the total stays at 4.00.

### 3. Why does the default value on `discount_code` matter?

> Because `print_order_summary` was already being called elsewhere without a discount code before this feature existed, and if `discount_code` had to be given every single time, all of those old calls would break because they only pass three arguments. Giving it a default of `""` means those older calls keep working exactly the same as before, without anyone having to go back and update them.

### 4. `isalpha()` vs `isalnum()` in `validate_discount_code`

> `isalnum()` allows both letters and digits to count as valid, whereas `isalpha()` only allows letters, so any digit makes it return `False`. If `isalpha()` was swapped for `isalnum()`, a code like `"SAVE12"` would wrongly pass validation even though it contains numbers, which shouldn't be allowed under the spec.
