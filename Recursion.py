#Pascal triangle using recursion
def pascal_triangle_recursion(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle_recursion(n - 1)
        last_row = triangle[-1]
        current_row = [1]
        for i in range(len(last_row) - 1):
            current_row.append(last_row[i] + last_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)
        return triangle

# MAIN FUNCTION:
n = 10
triangle = pascal_triangle_recursion(n)
for row in triangle:
    print(row)
    
    
#Rough output:
'''
if n=7
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1] 
'''
