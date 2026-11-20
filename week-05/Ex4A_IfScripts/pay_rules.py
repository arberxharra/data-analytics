pay_rate = 17.30
hours_worked = 45

if hours_worked > 40:
    gross_pay = (40 * pay_rate) + ((hours_worked - 40) * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"Gross pay is ${gross_pay:.2f}")