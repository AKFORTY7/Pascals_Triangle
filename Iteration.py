#Pascal triangle using Iteration
def pascal_triangle_iteration(n):
    triangle = []
    for i in range(n):
        current_row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                current_row.append(last_row[j] + last_row[j + 1])
            current_row.append(1)
        triangle.append(current_row)
    return triangle

#MAIN FUNCTION:
n = 8
triangle = pascal_triangle_iteration(n)
for row in triangle:
    print(row)

# Rough output:
'''
if n= 6
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
'''