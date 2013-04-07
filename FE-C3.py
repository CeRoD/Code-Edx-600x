## This program is the Finger excersise of the 600x
## Write a program that ask the user to enter a integer
## and prints two integers *root* and *pwr*, such that
## 0 < pwr < 6 and "root**pwr" is equal to the integer 
## entered by the user.
## If such pair of numbers does not exist should print
## a message fot that effect.

####	Munra	###

z = int(raw_input('Ingrese un numero entero: '))
num = 0
pwr = 1

if z < 0:
	print '\n The root is not a Real Number, sorry'
else:
	while num**2 < abs(z):
		num = num + 1
		#print num  ## This print statement is just
					## for see which value takes the
					## num variable.
	if num**2 != abs(z):
		print '\n The number ' + str(abs(z)) + ' does not have square root'
	else:
		print '\n The number has square root: '
		while (pwr > 0 and pwr < 6) and num**pwr != abs(z):
				pwr = pwr + 1
		if num**pwr == abs(z):
			print '\n \t And the numbers are: ' + str(num) + ' as the root'+\
				' and ' + str(pwr) + ' as the power.'
		else:
			print '\n \t But such numbers that root**pwr equals number enter,\
					 \t \t does not exist.'
