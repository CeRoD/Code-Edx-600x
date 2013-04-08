x = 0.0
for i in range(10):
	x += 0.1
	print x			# Show the incremental value of x.
if x == 1.0:	#A better way is "abs(x-y) < 0.0001 and not
				# x == y.
	print x, '= 1.0'
else:
	print x, 'is not 1.0'
