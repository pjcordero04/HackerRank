
def validMatrix(matrix):
    n = len(matrix)
    for row in matrix:
        for num in range(1,n+1,1):
            if num not in row:
                return False
            
    col = list(zip(*matrix))
    for j in range(n):
        for num in range(1,n+1,1):
            if num not in col[j]:
                return False
    return True
matrix = [[1,2,3],[3,1,2],[3,2,1]]
print(validMatrix(matrix))