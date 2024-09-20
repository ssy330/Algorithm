my_list = []
for i in range(10):
    N = int(input())
    my_list.append(N)

for j in range(10):
    my_list[j] %= 42

print(len(set(my_list)))