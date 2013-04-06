## Program that examines three variables -- x, y, and z --
## and prints the largest odd number among them.
## If none of then are odd, ir should print a messge for
## that effect.
		## Beta Version ##

print('Enter three numbers ')

a = raw_input('		Enter the first number: ')
b = raw_input('		Enter the second number: ')
c = raw_input('		Enter the third number: ')

print('The numbers are: ' + a + ', ' + b + ' and '+ c)

x = int(a)
y = int(b)
z = int(c)

if x%2 == 1 or y%2 == 1 or z%2==1:
	if x%2 == 1:
		if y%2 == 1 and z%2 == 1:
			if z%2 == 1:
				if x > y and x > z:
					print(a + ' is the largest number.')
				elif y > z:
					print(b + ' is the largest number.')
				else:
					print(c + ' is the largest number.')
			elif x > y:
				print(a + ' is the largest odd number.')
			else:
				print(y + ' is the largest odd number.')
		else:
			print(a + ' is the only odd number.')
	elif y%2 == 1:
		if z%2 == 1:
			if y > z:
				print(b + ' is the largest number.')
			else:
				print(c + ' is the largest number.')
		else:
			print(b + ' is the only odd number.')
	else:
		print(c + ' is the only odd number.')
else:
	print('none of the numbers are odd.')
