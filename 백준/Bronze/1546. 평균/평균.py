N = int(input())
score = list(map(int, input().split()))
new_score = [0]*N
if len(score) == N:
    for i in range(N):
        new_score[i] = score[i] / max(score) * 100
print(sum(new_score)/N)
    
    
