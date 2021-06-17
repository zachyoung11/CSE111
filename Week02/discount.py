# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current = datetime.now()

# Call the isoweekday() method to get the day
# of the week from the current datetime object.
weekday = current.isoweekday()

#User input prompt
sub_total = 0
more_items = "yes"

while more_items.lower() == "yes":
    name = input("What is your item? ")
    price = float(input(f"How much is {name}? "))
    quantity = int(input(f"Enter the quantity of {name}? "))
    more_items = input("Would you like to enter more items?")
    item_total = price * quantity
    sub_total += item_total

#Calculate discount
if sub_total >= 50 and (weekday == 2 or weekday == 3):
    discount = sub_total * .1
    sub_total -= discount
    tax = sub_total * 0.06
    total = sub_total + tax

    print(f"Discount amount: {discount: .2f}")
    print(f"Sales tax amount: {tax: .2f}")
    print(f"Total: {total: .2f}")
elif sub_total < 50 and (weekday == 2 or weekday == 3):
    difference = 50 - sub_total
    tax = sub_total * 0.06
    total = sub_total + tax

    print(f"Spend ${difference: .2f} more to get a 10% discount")
    print(f"Sales tax amount: {tax: .2f}")
    print(f"Total: {total: .2f}")
else:
    tax = sub_total * 0.06
    total = tax + sub_total

    print(f"Sales tax amount: {tax: .2f}")
    print(f"Total: {total: .2f}")
    


