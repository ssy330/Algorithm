def board(lst):
    a = 0
    for i in range(8):   
        if i%2 == 0:
            for j in range(0, 8, 2):
                if lst[i][j] == 'B':
                    a += 1
                if lst[i][j+1] == 'W':
                    a += 1            
        else:
            for k in range(0, 8, 2):
                if lst[i][k] == 'W':
                    a += 1
                if lst[i][k+1] == 'B':
                    a += 1
    return min(a, 64-a)

N, M = map(int, input().split())
lst = [input() for i in range(N)]

num = []
for col in range(N-7):
    for line in range(M-7):
        lst88 = [j[line:line+8] for j in lst[col:col+8]]
        num.append(board(lst88))
print(min(num))