B, N = map(int, input().split())
result = ""
while B > 0:
    remainder = B % N
    if remainder >= 10:
        result = chr(ord('A') + remainder - 10) + result
    else:
        result = str(remainder) + result
    B = B // N
print(result)