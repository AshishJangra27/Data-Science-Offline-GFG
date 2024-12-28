

# list
user_1 = ['Ashish', 25, 3274023, 98,78,78,99,88]

for i in range(len(user_1)):
  print(i, user_1[i])

found = False

for i in user_1:
    if i == 'Ashish':
        found = True
        
if found:
    print('found')
else:
    print('not found')
    
    
lst = []
    
for i in range(len(user_1)):
    if i%2 == 0:
        lst.append(user_1[i])

print(lst)

lst = []

num = 15
for i in range(num,num*10 + 1, num):
    lst.append(i)

print(lst)


lst = [12,'AShish',23423.12,True,[43,23,43,12,43]]
print(lst[4][2])


lst = [ [1,2,3], 
        [4,5,6], 
        [7,8,9]]
    
print(lst[0][2])


