x = 20
def computeVolume(l, w, h):
    global x
    x = 50
    return l * w * h


def displaySomething(userValue):
    print(userValue)

displaySomething(computeVolume(5, 7, 2))
print(x)



