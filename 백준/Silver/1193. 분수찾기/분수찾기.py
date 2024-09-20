X = int(input())
diagonal = 1

while X > diagonal:
    X -= diagonal
    diagonal += 1

if diagonal % 2 == 0:
    numerator = X
    denominator = diagonal + 1 - X
else:
    numerator = diagonal + 1 - X
    denominator = X

print(f"{numerator}/{denominator}")
