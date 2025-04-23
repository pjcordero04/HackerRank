def countSquares(rectangles):
    squares = []
    for rect in rectangles:
        squares.append(min(rect))
    squares.sort
    max = -9999
    count = 0
    for i in range(len(squares)):
        if(squares[i]>=max):
            count+=1
            max = squares[i]
    return count

rectangles = [[5,8],[3,9],[5,12],[16,5]]
print(countSquares(rectangles))