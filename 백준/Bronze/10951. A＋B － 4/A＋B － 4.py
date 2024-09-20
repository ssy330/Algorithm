import sys
while True:
    user_input = sys.stdin.readline().rstrip()
    if user_input == "":
        break
    A, B = map(int, user_input.split())
    print(A+B)