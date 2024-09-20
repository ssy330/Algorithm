def fmn(A, B):
    if B % A == 0:
        return "factor"
    elif A % B == 0:
        return "multiple"
    else:
        return "neither"

lst = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    lst.append(fmn(A, B))
    
for i in lst:
    print(i)
 