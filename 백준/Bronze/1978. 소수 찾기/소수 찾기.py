def prime(number):
    if number == 1:
        return False
    a = 0
    for i in range(2, number):
        if number % i == 0:
            a += 1            
    if a == 0:
        return True

N = int(input())
lst = map(int, input().split())
b = 0
for number in lst:
    if prime(number) == True:
        b += 1
print(b)