my_list = []
submit = []
a = 1
while a <= 30:
    my_list.append(a)
    a += 1

for i in range(28):
    n = int(input())
    submit.append(n)

result = list(set(my_list)-set(submit))
print(min(result))
print(max(result))