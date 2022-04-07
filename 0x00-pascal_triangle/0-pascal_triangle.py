def pascal_triangle(n):
    """
    program to generate pascals triangle
    """
    if n <= 0:
        return list()
    else:
        for i in range(n):
            # adjust space
            print(' '*(n-i), end='')
            
            # compute power of 11
            print(' '.join(map(str, str(11**i))))
