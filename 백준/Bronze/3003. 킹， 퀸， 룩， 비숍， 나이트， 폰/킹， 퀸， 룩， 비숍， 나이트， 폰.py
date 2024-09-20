#3003
black = [1, 1, 2, 2, 2, 8]
white = input().split()
list = []
for i in range(6):
    set = black[i]-int(white[i])
    list.append(set)
print(*list)

