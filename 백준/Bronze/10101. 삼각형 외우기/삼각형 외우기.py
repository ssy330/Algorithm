lst = []
for _ in range(3):
    a = int(input())
    lst.append(a)

if sum(lst) == 180:
        
    if len(set(lst)) == 3:
        print('Scalene')

    elif len(set(lst)) == 2:
        print('Isosceles')

    else: 
         print('Equilateral')
    
else:
    print('Error')