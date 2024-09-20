N = int(input())
Nlist = list(map(int, input().split()))
if len(Nlist) == N:
    min_value = min(Nlist)
    max_value = max(Nlist)
    print(min_value, max_value)
