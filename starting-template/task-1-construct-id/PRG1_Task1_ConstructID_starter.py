"""
Shift Pay Calculator

Calculates an employee's pay for a single shift, including a bonus
for shifts flagged as premium (for example, a bank holiday shift).

This program is complete and working. Do not change it.
Read it, run it if you like, then complete the identification task.
"""

BONUS_PERCENTAGE = 15  # fixed company policy for premium shifts


def calculate_gross_pay(hours_worked, hourly_rate):
    """Return gross pay for a shift, before any bonus is added."""
    gross_pay = hours_worked * hourly_rate
    return gross_pay


def calculate_bonus(gross_pay):
    """Return the bonus amount for a premium shift."""
    bonus_amount = gross_pay * (BONUS_PERCENTAGE / 100)
    return bonus_amount


def build_payslip(employee_name, gross_pay, bonus_amount):
    """Return a formatted payslip string ready to print."""
    total_pay = gross_pay + bonus_amount
    payslip = (
        f"Payslip for {employee_name}\n"
        f"Gross pay:  £{gross_pay:.2f}\n"
        f"Bonus:      £{bonus_amount:.2f}\n"
        f"Total pay:  £{total_pay:.2f}"
    )
    return payslip


# ---- Example shift ----

employee_name = "Amir Khan"
hours_worked = 7.5
hourly_rate = 12.50

gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
bonus_amount = calculate_bonus(gross_pay)
payslip_text = build_payslip(employee_name, gross_pay, bonus_amount)

print(payslip_text)
