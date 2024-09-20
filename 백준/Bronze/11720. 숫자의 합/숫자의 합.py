N = int(input())
number = input()
sum = 0
if len(number) == N:
    for i in range(N):
        sum += int(number[i])
print(sum)   
