bill_amount = float(input("How much was the restaurant bill? $"))
tip_percentage = float(input("What tip percentage do you want? Enter 18 for 18%: "))

tip_amount = bill_amount * tip_percentage / 100

print(f"The tip on a ${bill_amount:.2f} restaurant bill is ${tip_amount:.2f}")

# input() gives us text, so float() changes the answers into numbers for the calculation.
# The user must enter numbers; letters or a blank answer will cause an error.
# Enter 18 for an 18% tip, not 0.18.