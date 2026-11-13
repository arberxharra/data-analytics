current_savings = 5000.00
interest_rate = 0.06  # 6% written as a decimal

doubled_balance = current_savings * 2
years_to_double = 72 / (interest_rate * 100)

print("Your current savings is " + format(current_savings, ".2f") + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be")
print("worth " + format(doubled_balance, ".2f") + " in " + format(years_to_double, ".1f") + " years")