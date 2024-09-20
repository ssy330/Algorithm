N, M = map(int, input().split())
number_list = []
for i in range(2*N):
    number = input()
    number_list.append(number.split())

for j in range(N):
    for k in range(M):
        print(int(number_list[j][k])+int(number_list[j+N][k]), end=' ')
    print()