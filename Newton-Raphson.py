## Aproximation algorithm make by Isaac Newton
## the Newton's method, the Newton-Rapphson method.
## It can only be used to find the the real roots of many functions,
## but we shall look at it only in the context of finding the real
## roots of a polynomial with one variable.

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0.

epsilon = 0.01
y = 24.0
guess = y/2.0
while abs(guess*guess -y) >= epsilon:
	guess = guess - (((guess**2) - y)/(2*guess))
print 'Square root of', y, 'is about', guess
