N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
result = sorted(lst)
for i in result:
    print(' '.join(map(str, i)))
