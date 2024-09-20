list = []
while 0 not in list:
    a, b = map(int, input().split())
    list.append(a+b)
    if 0 in list:
        break
for i in range(len(list)-1):
    print(list[i])