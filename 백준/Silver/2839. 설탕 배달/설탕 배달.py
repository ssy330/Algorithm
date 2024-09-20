N = int(input())

for i in range(N//5, -1, -1):
    num_3 = (N - 5*i) // 3
    if N == 5 * i + 3 * num_3:
        print(i + num_3)
        break
else:
    print(-1)