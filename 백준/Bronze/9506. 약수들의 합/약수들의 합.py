def perpect_number(n):
    lst = [i for i in range(1, n) if (n % i) == 0]
    if n == sum(lst):
        result = f"{n} = " + " + ".join(map(str, lst))
    else:
        result = f"{n} is NOT perfect."
    return result

lst2 = []           
while True:
    n = int(input())
    if n == -1:
        break
    lst2.append(perpect_number(n))

for j in lst2:
    print(j)