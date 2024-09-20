N, M = map(int, input().split())
list = [0]*N
for number in range(M):
    i, j, k = map(int, input().split())
    list[i-1:j] = [k]*(j-i+1)
print(*list)
