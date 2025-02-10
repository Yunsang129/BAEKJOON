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
    pos = []
    
    for i in range(x1, x2 + 1):
        pos.append((y1, i))
        
    for i in range(y1 + 1, y2 + 1):
        pos.append((i, x2))
        
    for i in range(x2 - 1, x1 - 1, -1):
        pos.append((y2, i))
        
    for i in range(y2 - 1, y1, -1):
        pos.append((i, x1))
    
    
    N = len(pos)
    for i in range(N - 1, 0, -1):
        ny, nx = pos[i][0], pos[i][1]
        by, bx = pos[i - 1][0], pos[i - 1][1]
        matrix[ny][nx], matrix[by][bx] = matrix[by][bx], matrix[ny][nx]
    
    return min(matrix[y][x] for y, x in pos)