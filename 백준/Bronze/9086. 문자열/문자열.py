list = []
T = int(input())
for i in range(T):
    word = input()
    list.append(word[0]+word[len(word)-1])
for j in list:
    print(j)