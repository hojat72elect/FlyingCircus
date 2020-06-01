def sayHello():
    print("saying hello to the world!")


def maxFinder(a, b):
    if a > b:
        print(f'a = {a} is the maximum.')
    elif b > a:
        print(f'b = {b} is the maximum.')
    else:
        print("a and b are the same.")


def sayIt(message, times=1):
    print((message + '\n') * times)


'''This is how you can variable number of arguments in a function:'''


def total(a=5, *numbers, **phonebook):
    print(f'a is : {a}')

    # iterate through all the items in tuple:
    for singleItem in numbers:
        print(f"The single item is: {singleItem}")

    # iterate through all the items in dictionary:
    for firstPart, secondPart in phonebook.items():
        print(f"{firstPart}:{secondPart}")


def anotherMaxFinder(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "the input numbers are equal."


sayHello()
sayHello()

maxFinder(a=232, b=45)
maxFinder(6, 6)

sayIt("My name is Hojat")
sayIt("I love programming", 3)

total(10, 2, 7, 8, 3, 6, 4, 7, 2, Hojat="Kerman", Jennifer="Sudbury", Aly="Texas")

print(anotherMaxFinder(75, 7))
