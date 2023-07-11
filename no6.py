def segitiga_paskal(level):
    triangle = []

    for i in range(level):
        row = [1]

        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                num = prev_row[j] + prev_row[j + 1]
                row.append(num)

        row.append(1)  
        triangle.append(row)

    return triangle

depth = int(input("Masukkan kedalaman level : "))

pascal_triangle = segitiga_paskal(depth)

for row in pascal_triangle:
    print(" ".join(str(num) for num in row))
