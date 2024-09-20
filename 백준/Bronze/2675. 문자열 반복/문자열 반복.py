number = int(input())
list = []
for i in range(number):
    user_input = input()
    list.append(user_input)

for j in range(len(list)):
    a, b = list[j].split()
    for k in range(len(b)):
        print(b[k]*int(a), end="")
    print()   