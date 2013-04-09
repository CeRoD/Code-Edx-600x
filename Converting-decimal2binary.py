### I don't really undestand the code.
### but the computers do something like
### this converting decimals to binary and then
### compute the numbers, because computer use just
### binary.

num = int(raw_input('Ingrese numero: '))
if num < 0:
	isNeg = True
	num = abs(num)
else:
	isNeg = False
result = ''
if num == 0:
	result = '0'
while num > 0:
	result = str(num%2) + result
	num = num/2
if isNeg:
	result = '-' + result
print result
