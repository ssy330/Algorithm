list = []
word = input()
for i in word:
    list.append(i)
reverse_list = list.copy()
reverse_list.reverse()

if list == reverse_list:
    print(1)
else:
    print(0)