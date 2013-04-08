## In this code I change the if satement in the ExhaustiveEnumeration.py
## so now check if is equal to the given number besides the other one the
## check if was different.


x=int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
	print 'Value of the decrementing function, abs(x)-ans**3, =',\
			abs(x) - ans**3 #The print statement can be coment and works.
	print ans		# to see what is number that is computing.
	ans=ans + 1
if ans**3 == abs(x):
	if x < 0:
		ans = -ans
	print 'Cube root of ' + str(x) + ' is ' + str(ans)
else:
	print x,  'is not a perfect cube'
