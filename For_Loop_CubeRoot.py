# Find the cube root of a perfect cube:
# this is an alternative for the while statement 
# so is another way of implement a exhaustive enumeration.

x = int(raw_input('Enter an integer: '))

for ans in xrange (0, abs(x)+1):
            ## xrange is a lot more effient that range.
    print ans # Added for munra to check the values that ans takes.
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print x, 'is not a perfect cube.'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
