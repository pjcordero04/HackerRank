import math

def solitaire(a,b,c):
    piles = sorted([a, b, c])  # Sort so we always know the largest
    x, y, z = piles
    
    # If the largest pile is greater than or equal to the sum of the other two
    if x + y <= z:
        return x + y
    else:
        return (x + y + z) // 2

print(solitaire(2,3,7))
    