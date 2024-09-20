a, b, c = map(int, input().split())
lst = [a, b, c]
X = max(lst)
if X < sum(lst) - X:
    print(sum(lst))
else:
    lst[lst.index(X)] = sum(lst) - X - 1
    print(sum(lst))