### Code that ask for integer number and run a for loop ####
### that increments a varialbe by 0.1, the number of times the
### value of x by 10 times.
### This code is made for show the behavior of float points, because
### is possible to see that for python ten times 0.1 is not 1.0.


x = float(raw_input('Enter a number: '))
num = int(x * 10) 		# 10 times x, because 0.1 is added to
						# y, so is incrementing by 0.1, which
						# means that 10 times 0.1 is 1 (the unit).
						# for instance: 5 is 50 times 0.1.
y = 0.0
for i in range(num):
	y += 0.1
	print y			# Show the incremental value of x.
if y == x:
	print y, ' = ', x
else:
	print y, 'is not ', x
