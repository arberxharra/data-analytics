bill_amount = 45.00
tip_percentage = 18

tip_amount = bill_amount * tip_percentage / 100

print(
    "The tip on a $" + format(bill_amount, ".2f")
    + " restaurant bill is $" + format(tip_amount, ".2f")
)