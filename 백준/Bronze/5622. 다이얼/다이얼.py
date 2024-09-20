number2 = ['A', 'B', 'C']
number3 = ['D', 'E', 'F']
number4 = ['G', 'H', 'I']
number5 = ['J', 'K', 'L']
number6 = ['M', 'N', 'O']
number7 = ['P', 'Q', 'R', 'S']
number8 = ['T', 'U', 'V']
number9 = ['W', 'X', 'Y', 'Z']

word = input()
sum = 0
for i in word:
    for j in range(2, 10):
        if i in globals()[f"number{j}"]:
            sum += j+1
print(sum) 