N, X = map(int, input().split())
A = input().split()
new_list = []
if len(A) == N:
    for i in  range(N):
        if int(A[i]) < X:
            new_list.append(int(A[i]))
print(*new_list)    