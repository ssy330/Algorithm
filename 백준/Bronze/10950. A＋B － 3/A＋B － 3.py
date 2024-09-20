case = int(input())
a = 1
list1 = []
while a <= case:
    append_list = list(map(int, input().split()))
    list1 = list1 + append_list
    a += 1
b = 0 
while b < case*2:     
    print(list1[b] + list1[b+1])
    b += 2