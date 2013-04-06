if type(varA) == str:
    print('string involved')
elif type(varB) == str:
    print('string involved')
else:
    if varA > varB:
        print('bigger')
    elif varA == varB:
        print('equal')
    elif varA < varB:
        print('smaller')
