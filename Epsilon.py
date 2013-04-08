# This method for finding the square root uses
# exhaustive enumeration.
#### Exhaustive Enumeration is a technique that works #### 
#### only if the set of values being searched includes #### 
#### the answer. #### 
#### That means that if the number is between 0 and 1 will not ###
#### works. ###

x = float(raw_input('Enter a number: '))
epsilon = 0.01			#I think that this determinated
						# the precision of the number, I mean
						# if is close 0.01 to the numbre the number
						# is a close enough square root.
step = epsilon**2		# According to the book this is what
						# determinate the steps (duh), so:
						# epsilon**3 gives smaller steps.
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
	print 'ans =', ans, ' Epsilon=',epsilon, ' step=',step # Just for see
										#what is doing.
    	ans += step
    	numGuesses += 1
print 'numGuesses =', numGuesses
print ans , step
if abs(ans**2 - x) >= epsilon:
        print 'Failed on square root of', x
else:
    print ans , 'is close to square root of', x
