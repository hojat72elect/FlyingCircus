"""This is a representation of how we can easily deal with strings in python ."""

import string

initials = "Hojat Ghasemi"

print(initials)
print(initials[-1])
print(initials[5])
print(initials[:7])

print(len(initials))
print(initials.split())
print(initials.split('a'))
print(initials.split('a', 1))  # the function is allowed to do the split just once.
print('***'.join(initials.split()))

print("this is" + "it")
print("this is" * 3)
print("\155")
print("\x6d")

print(initials, end="")
print(initials.upper())  # uppercasing all the letters.
print(initials.lower())  # lowercasing all the letters.
print(initials.isupper())
print(initials.islower())
print(initials.capitalize())
print(initials.title())
print(initials.swapcase())  # changes the case of each character of the string.

###################################
###################################

floatNum = "456.56"
intNum = "34"
print(intNum.isdigit())  # checks to see that the string is comprised of digits or not.
print(intNum.isalpha())  # checks to see if that string is comprised of alphabets.
print(float(floatNum) + 0.6)
print(int(intNum) * 4)
print(int(intNum, 8))
# assumes the digits in the string to be of octal base and converts the string to a decimal number.

###################################
###################################

myName = "   mr  Hojat       Ghasemi   "
print(myName.strip())
print(myName.lstrip())
print(myName.rstrip())

myActualName = "Hojat Ghasemi"
print(myActualName.strip("moeHi"))

###################################
###################################


print(string.whitespace)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
###################################
###################################

print(initials.find('a'))
print(initials.find('a', 4))
print(initials.find('ab'))
print(initials.rfind('a'))
print(initials.count('s'))

###################################
###################################

print(initials.startswith("h"))
print(initials.startswith("H"))
print(initials.endswith("emi"))
print(initials.endswith(("h", "i", "o")))

###################################
###################################

print(initials.replace('a', "**"))

###################################
###################################
'''this is how we can translate some string from one programming language to another one.'''
x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")
print(x.translate(table))

table2 = x.maketrans("x", " ")
print(x.translate(table2))

###################################
###################################

myChar = "M"
print(myChar.islower())
print(myChar.isupper())

###################################
###################################

mydict = {"Canada": "Ottawa", "Germany": "Berlin"}
print(repr(mydict))
print(repr(int))

###################################
###################################

print("my name is {} and I'm {} years old.".format("Hojat", 26))
print("I", "am", "Hojat", sep="+*+")
print("I", "am", "Hojat", end="\n\n")

print(f'my name is {initials}')  # only available in python3.
###################################
###################################

name = "Hojat Ghasemi"
print(name.partition("a"))
print(name.rpartition("a"))
