lst = []
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    lst.append([a, b, c])

result_lst = []
for i in range(len(lst)):
    sorted_lst = sorted(lst[i])
    the_longest = sorted_lst[2]

    if the_longest >= sum(sorted_lst[0:2]):
        result_lst.append('Invalid')
    
    else:
         
        if len(set(lst[i])) == 3:
            result_lst.append('Scalene')

        elif len(set(lst[i])) == 2:
            result_lst.append('Isosceles')

        else: 
            result_lst.append('Equilateral')
    

for j in result_lst:
    print(j)