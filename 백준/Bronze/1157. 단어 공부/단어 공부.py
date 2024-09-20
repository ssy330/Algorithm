word = input().upper()
letter_frequency = {}
for i in word:
    letter_frequency[i] = letter_frequency.get(i, 0) + 1
most = max(letter_frequency.values())
most_word = [letter for letter, frequency in letter_frequency.items() if frequency == most]
if len(most_word) == 1:
    print(most_word[0])
else:
    print("?")