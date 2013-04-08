# Using Bisection search to approximate square root.
####		Bisection search	#####

x = float(raw_input('Ingrese un numero: '))
epsilon = 0.0001		# This is value the determinate
						# how close the answer is to the
						# given number.
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
	print 'low =',low, 'high =',high, 'ans =',ans
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x
