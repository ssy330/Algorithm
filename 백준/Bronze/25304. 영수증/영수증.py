X = int(input())
N = int(input())
n = 1
list = []
while n <= N:
    a, b = map(int, input().split())
    list.append(a * b)
    n += 1
    
sum = 0
for i in range(N):
    sum += list[i]
    
if sum == X:
    print("Yes")
else:
    print("No")
