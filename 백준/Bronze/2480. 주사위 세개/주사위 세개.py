nums = map(int, input().split())
list = list(nums)
if len(set(list)) == 1:
    print(10000+list[0]*1000)
elif list[0] == list[1] and list[0] != list[2]:
    print(1000+list[0]*100)
elif list[1] == list[2] and list[0] != list[1]:
    print(1000+list[1]*100)    
elif list[0] == list[2] and list[0] != list[1]:
    print(1000+list[0]*100)     
else:
    print(max(list)*100)