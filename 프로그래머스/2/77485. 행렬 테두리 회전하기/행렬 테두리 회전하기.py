def solution(rows, columns, queries):
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    result = []
    num = 0
    for i in range(rows):
        for j in range(columns):
            num += 1
            matrix[i][j] = num
    
    for a, b, c, d in queries:
        result.append(rotate_num(a - 1, b - 1, c - 1, d - 1 ,matrix))
    return result

def rotate_num(y1, x1, y2, x2, matrix):
    first_num = matrix[y1][x1]
    min_value = first_num
    ny, nx = y1, x1
    
    for i in range(y1, y2):
        matrix[i][x1] = matrix[i + 1][x1]
        min_value = min(min_value, matrix[i][x1])
    
    for i in range(x1, x2):
        matrix[y2][i] = matrix[y2][i + 1]
        min_value = min(min_value, matrix[y2][i])
        
    for i in range(y2, y1, -1):
        matrix[i][x2] = matrix[i - 1][x2]
        min_value = min(min_value, matrix[i][x2])
    
    for i in range(x2, x1 + 1, -1):
        matrix[y1][i] = matrix[y1][i - 1]
        min_value = min(min_value, matrix[y1][i])
    
    matrix[y1][x1 + 1] = first_num
    return min_value