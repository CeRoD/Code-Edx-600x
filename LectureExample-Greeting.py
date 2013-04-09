# This code print two times the even charecter of a string
# and one time the odd 


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')
