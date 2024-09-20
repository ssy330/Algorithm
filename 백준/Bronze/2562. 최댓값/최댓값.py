list = []
for i in range(9):
    number = int(input())
    list.append(number)
max_value = list.index(max(list))
print(max(list))
print(int(max_value)+1)
