# This method for finding the square root uses
# exhaustive enumeration.
#### Exhaustive Enumeration is a technique that works #### 
#### only if the set of values being searched includes #### 
#### the answer. #### 

### In this one is possible to find the squate root of ###
### a number between 0 and 1.	###


x = float(raw_input('Enter a number: '))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans*ans <= x:
    ans += step
    numGuesses += 1
print 'numGuesses =', numGuesses
print ans , step
if abs(ans**2 - x) >= epsilon:
        print 'Failed on square root of', x
else:
    print ans , 'is close to square root of', x
