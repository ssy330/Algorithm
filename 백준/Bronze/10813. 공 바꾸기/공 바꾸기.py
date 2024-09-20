N, M = map(int, input().split())
list = []
a = 1
while a <= N:
    list.append(a)
    a += 1
for number in range(M):
    i, j = map(int, input().split())
    new_list = [list[i-1], list[j-1]]
    list[i-1] = new_list[1]
    list[j-1] = new_list[0]
print(*list)