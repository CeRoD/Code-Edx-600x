### Code for L3 Problem 5 ####

# Codigo va de 2 a 10, de dos en dos y luego
# imprime Goobye!.

# Esta es mi solucion.
for num in range(2,12,2):
    print(num)
print('Goodbye!')

# Sugerencias de solucion del curso.

# There are many ways to solve this problem! Here is one:
for count in range(11):
    if count != 0 and count % 2 == 0:
        print count
print "Goodbye!"

# Here is another:
for count in range(2, 12, 2):
    print count
print "Goodbye!"



######
## Codigo imprime la cadena "Hello!" y luego 
## numeros de 10 a 2 de dos en dos,

# Mi solucion:
print('Hello!')
x = 10
for num in range(0,x,2):
    print(x)
    x -= 2

## Sugerencias del curso:
# # There are always many ways to solve a programming problem. Here is one:
print "Hello!"
for num in range(0, 10, 2):
    print 10 - num

# Here is another:
print "Hello!"
for num in range(10, 0, -2):
    print num

## Write a for loop that sums the values 1 through end, inclusive.
#  end is a variable that we define for you. 
# So, for example, if we define end to be 6, your code
#  should print out the result: 21

# Mi solucion:
suma=0
for num in range(1,end+1):
    suma += num
print suma

## Sugerencias del curso:
# Here is one of a few ways to solve this problem:
total = 0
for next in range(1, end+1):
    total += next
print total

# Here is another:
total = end
for next in range(end):
    total += next
print total
