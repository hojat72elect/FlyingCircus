"""This is a representation of best functions in "math" module."""

import math

print(math.pi)
print(math.e)

myFirstFloat = 5.67
print(math.ceil(myFirstFloat))
print(math.floor(myFirstFloat))

print(math.copysign(-4.5, 1))
print(math.fabs(-4.23))
print(math.factorial(4))

print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

print(math.gcd(36, 24))  # the greatest common divisor of two integers.
print(math.gcd(3, 2))

print(math.isfinite(myFirstFloat))
print(math.isinf(myFirstFloat))

print(math.remainder(10.5, 2))

print(math.trunc(47.999999))

print(math.exp(10))  # e is powered by 10.
print(math.expm1(1))  # Return exp(x)-1

print(math.log(math.e))  # If the base not specified, returns the natural logarithm (base e)
print(math.log(625, 5))  # logarithm of x to the given base.
print(math.log10(1000))

print(math.pow(2, -6))

print(math.sqrt(36))  # square root
