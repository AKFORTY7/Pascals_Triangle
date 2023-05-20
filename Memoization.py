#Pascal triangle using Memoization
def pascal_triangle_memoization(n, memo={}):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n in memo:
        return memo[n]
    else:
        triangle = pascal_triangle_memoization(n - 1, memo)
        last_row = triangle[-1]
        current_row = [1]
        for i in range(len(last_row) - 1):
            current_row.append(last_row[i] + last_row[i + 1])
        current_row.append(1)
        triangle.append(current_row)
        memo[n] = triangle
        return triangle

# MAIN FUNCTION:
n = 12
triangle = pascal_triangle_memoization(n)
for row in triangle:
    print(row)
    
# ROUGH OUTPUT:
'''
if n=5
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
''' 

