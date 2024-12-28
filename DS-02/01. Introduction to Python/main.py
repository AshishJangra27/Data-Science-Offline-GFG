
a = 18
b = 20

Comaprison Operators
>
<
==
!=
>=
<=

Logical Operators
and
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# or
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not
print(not(True))


print('-'*25)

print(True and (True or False))

age = 18

if (age >= 18 and age <= 100): # 18-100
    print('Eligible')
    
elif (age >= 0 and age <= 18):  # 0 - 17
    print('Not Eligible')
    
elif (age >= 0 and age <= 18):  # 0 - 17
    print('Not Eligible')
    
else:
    print('Invalid Age')
    

num = 10

if (num % 5 == 0):
    if (num % 7 == 0):
        print('Valid')
    else:
        print('not valid-')
else:
    print('not valid')


num = 35
    
if (num % 5 == 0):
    print('div by 5')

if (num % 7 == 0):
    print('div by 7')


pr   = 14232.42
intr = 7
yrs  = 5


print(pr + (pr * intr * yrs)/100)
print((pr + (pr * intr * yrs)//100))


