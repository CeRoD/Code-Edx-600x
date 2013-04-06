x = input("Ingrese un numero: ")
ans = 0
itersLeft = x
while (itersLeft != 0):
	ans = ans + abs(x)
	itersLeft = itersLeft -1
	print itersLeft , ans
print str(x) + '*' + str(x) + ' = ' + str(ans)
