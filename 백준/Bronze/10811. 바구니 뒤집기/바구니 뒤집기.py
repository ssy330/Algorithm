N, M = map(int, input().split())
a = 1
my_list = []
for i in range(N):
    my_list.append(a)
    a += 1
for i in range(M):
    i, j = map(int, input().split())
    new_list = my_list[i-1:j]
    new_list.reverse()
    my_list[i-1:j] = new_list    
print(*my_list)