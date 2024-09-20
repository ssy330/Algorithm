num = int(input())
n = 1
list = []
while n <= num:
    a, b = map(int, input().split())
    list.append("{} + {} = {}".format(a, b, a+b))
    n += 1

for i in range(num):
    print("Case #{}:".format(i+1), list[i])

