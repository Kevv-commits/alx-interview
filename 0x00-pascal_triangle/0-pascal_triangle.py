def pascal_triangle (n):
    """
    pascals triangle
    """
    results = []
    if n <= 0:
        return results
    trow = [1]
    y = [0]
    for x in range(n):
        print(trow)
        trow=[left+right for left,right in zip(trow+y, y+trow)]
    return n>=1
