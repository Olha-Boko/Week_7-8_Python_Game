# let's explore some functions
# and what they do


def greeting():
    # say hello
    print("hello from your first functionn!")


# this is how you call or invoke a function
greeting()


def greetings(msg="hello there!", num=0):
    print("Our function says", msg)


greetings()
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)

myVeriableNumber = 0


def someMatch(num1=2, num2=5):
    global myVeriableNumber

    myVeriableNumber = num1 + num2
    return num1 + num2


sum = someMatch()
print("Our sum variable is:", sum, "myVeriableNumber is also", sum)
