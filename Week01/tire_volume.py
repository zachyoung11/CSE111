# Import the math module so that I can use math.pi
import math

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date = datetime.now().date()

# Explanation to user how tire dimensions work in the U.S.
print("The size of a car tire in the United States is represented with three numbers like this: 205/60R15.")
print("The first number is the width of the tire in millimeters.The second number is the aspect ratio.")
print("The third number is the diameter in inches of the wheel that the tire fits.")
print()

# What will this program do
print("This program computes and outputs the volume of space inside of a tire.")
print()

# Get the dimensions of the tire from user.
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))


# Compute the volume
w_a_d = (width * ratio) + (2540 * diameter)
numerator = (math.pi * (width **2) * ratio) * w_a_d
volume = numerator / 10000000

# Open a text file named volume.txt in append mode.
with open("volume.txt", "at") as volume_file:

    # Print a car's model and dimensions to the file.
    print(f"{current_date}, {width}, {ratio}, {diameter}, {volume: .1f}", file=volume_file)


# Output
print(f"The approximate volume is {volume: .1f} cubic cm.")

if diameter >= 12 and diameter <= 15:
    print("The average cost of an all-season tire this size will be between $80 and $150.")
elif diameter >= 16 and diameter <= 20:
    print("The average cost of an all-season tire this size will be between $100 and $250.")
elif diameter >=21 and diameter <= 26:
    print("The average cost of an all-season tire this size will be between $140 and $250.")
else:
    print("This tire is either for a trycicle or a monster truck. Either way we currently dont have the pricing for this size.")
    


