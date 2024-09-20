import sys
N = int(sys.stdin.readline())
my_list = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    my_list.append(A + B)
    
for i in my_list:
    print(i)
