alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
dictionary = {alphabet : -1 for alphabet in alphabet_list}
word_list = []
word = input()
for k in word:
    word_list.append(k)
for i in word:
    for j in range(len(dictionary)):
        if i == alphabet_list[j]:
            dictionary[i] = word_list.index(i)
print(*list(dictionary.values()))
