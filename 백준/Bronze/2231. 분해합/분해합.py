def dissolution_sum(num):
    a = 0
    for i in str(num):
        a += int(i)        
    return num + a
    
N = int(input())

found = False

for j in range(1, N+1):
    if dissolution_sum(j) == N:
        print(j)
        found = True
        break
if not found:
    print(0)