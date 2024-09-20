n = int(input())
x_coordinates = []
y_coordinates = []

for _ in range(n):
    x, y = map(int, input().split())
    x_coordinates.append(x)
    y_coordinates.append(y)

min_x = min(x_coordinates)
max_x = max(x_coordinates)
min_y = min(y_coordinates)
max_y = max(y_coordinates)

rectangle_area = (max_x - min_x) * (max_y - min_y)

print(rectangle_area)
