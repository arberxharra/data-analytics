pay_rate = 25.00
hours_worked = 19
filing_status = "single"

# Calculate weekly gross pay, including overtime if needed
if hours_worked > 40:
    weekly_gross_pay = (40 * pay_rate) + (
        (hours_worked - 40) * pay_rate * 1.5
    )
else:
    weekly_gross_pay = hours_worked * pay_rate

# Estimate annual gross income using 52 weeks
annual_gross_income = weekly_gross_pay * 52

# Determine the tax rate based on filing status and annual income
if filing_status == "single":
    if annual_gross_income < 12000:
        tax_rate = 0.05
    elif annual_gross_income < 25000:
        tax_rate = 0.10
    elif annual_gross_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
else:  # joint
    if annual_gross_income < 12000:
        tax_rate = 0.00
    elif annual_gross_income < 25000:
        tax_rate = 0.06
    elif annual_gross_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# Calculate weekly tax withholding and net pay
weekly_tax = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - weekly_tax

# Display the results
print(f"You worked {hours_worked} hours this period.")
print(
    f"Because you earn ${pay_rate:.2f} per hour, "
    f"your gross weekly pay is ${weekly_gross_pay:.2f}."
)
print(f"Your filing status is {filing_status}.")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}.")
print(f"Your net pay is ${net_pay:.2f}.")