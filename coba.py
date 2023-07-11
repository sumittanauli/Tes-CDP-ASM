def segitiga_paskal(level):
    triangle = []
    for row in range(level):
        triangle.append([])
        for col in range(row + 1):
            if col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row - 1][col - 1] + triangle[row - 1][col])
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        for num in row:
            print(num, end=" ")
        print()

depth = int(input("Masukkan kedalaman level : "))

pascal_triangle = segitiga_paskal(depth)
print_pascal_triangle(pascal_triangle)
