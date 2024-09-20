number = int(input())
a = 0
for j in range(number):
    word = input()
    group = word[0]
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            group += word[i+1]
    if len(set(group)) == len(list(group)):
        a += 1
print(a)
