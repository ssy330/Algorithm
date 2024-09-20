N = int(input())
a = 2
lst = []
while N % a != N:
    if N % a == 0:
        N //= a
        lst.append(a)
    else:
        a += 1

for _ in lst:
    print(_)
