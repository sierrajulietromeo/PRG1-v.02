# Task 1: Construct Identification, Answers

Complete this alongside `BRIEF_T1.md`. Write in your own words; quote from the code exactly where the brief asks you to.

## Identification table

### A constant

> `BONUS_PERCENTAGE = 15`. I know it's a constant because it's written in capital letters at the top of the file before any of the functions, and it never gets changed anywhere in the program, it's just used to work out the bonus each time.

### A variable that stores input data

> `hours_worked`. It's not something the program works out itself, it's set directly with a value.

### A second, different variable that stores input data

> `hourly_rate`, also just given a value directly rather than calculated by the program.

### A variable that stores a calculated value

> `gross_pay`. It's worked out inside `calculate_gross_pay` by multiplying `hours_worked` by `hourly_rate`, so it's not typed in directly like the two above.

### A function definition

> `def calculate_bonus(gross_pay):` - takes one parameter, `gross_pay`.

### A different function definition

> `def build_payslip(employee_name, gross_pay, bonus_amount):` - takes three parameters.

### A return statement

> `return bonus_amount`, sends back the bonus amount that was worked out inside that function.

### A function call

> `gross_pay = calculate_gross_pay(hours_worked, hourly_rate)`. This calls the `calculate_gross_pay` function and passes in `hours_worked` and `hourly_rate`.

### An expression

> `hours_worked * hourly_rate`

### The formatted output construct

> The f-string inside `build_payslip` that builds the payslip text, for example `f"Total pay:  £{total_pay:.2f}"`. It puts the numbers into the string in the right format.

## Explain the flow

> First `calculate_gross_pay` is called to work out the pay from the hours and rate. Then `calculate_bonus` is called, using the gross pay that was just returned, to work out the bonus. Then `build_payslip` is called last, using both of those results, to put everything together into the final payslip text that gets printed. It has to happen in that order because each function needs the result of the one before it.
