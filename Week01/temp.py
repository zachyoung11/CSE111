x = 5
y = 6
# This Prints True
print(x < y)

favoriteNumbersList = [3,4,5,6,7,8]

# This will print
if (4 in favoriteNumbersList) :
    print("This was true")

#This will not print
if (4 not in favoriteNumbersList) :
    print("This was true")

name = "Joey"
if("J" in name):
    print("J was in the name")

#These come up with the same thing
x = x + 1
x += 1
#+= -= *= all assign the equation to the variable

x = 5
z = x // 2 #2
print(z)
y = x % 2
print(y)
print(z+y)

x = 10
for i in range(0,x):
    print(i)

import math

#This creates a function that computes Circumference 
def computeCircumference(radius):
    return 2 * radius * math.pi


circumference = computeCircumference(5)
print(circumference)

userRadius = float(input("Please enter a radius: "))
print(computeCircumference(userRadius))

