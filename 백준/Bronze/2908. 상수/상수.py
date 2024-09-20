A, B = input().split()
new_A = A[::-1]
new_B = B[::-1]
if int(new_A) < int(new_B):
    print(new_B)
else:
    print(new_A)