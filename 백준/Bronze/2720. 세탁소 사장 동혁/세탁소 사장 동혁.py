def change(money):
    quarter = money // 25
    money %= 25
    dime = money // 10
    money %= 10
    nickel = money // 5
    money %= 5
    penny = money

    return quarter, dime, nickel, penny

lst = []
number = int(input())
for i in range(number):
    test_case = int(input())
    lst.append(change(test_case))

for j in lst:
    print(*j)