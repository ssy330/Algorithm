import string
alphabet = string.ascii_uppercase
number_dic = {i: j for i, j in zip(alphabet, list(range(10, 36)))}

N, B = input().split()

number = []
for i in range(len(N)):
    if N[i] in alphabet:
        number.append(int(B)**(len(N)-(i+1)) * int(number_dic[N[i]]))
    else:
        number.append(int(B)**(len(N)-(i+1)) * int(N[i]))
print(sum(number))