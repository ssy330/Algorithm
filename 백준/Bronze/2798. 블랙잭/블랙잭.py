from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = []
for i in (combinations(lst, 3)):
    card_sum = sum(i)
    if card_sum <= M:
        sum_lst.append(card_sum)
print(max(sum_lst))