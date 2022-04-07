def pascal_triangle(n):
    """
    program to generate pascals triangle
    """
    if n <= 0:
        return list()
    else:
        previous = [0] + pascal(n-1) + [0]
        new_row = [previous[i] + previous[i+1] for i in range(len(previous)-1)]
        return new_row
    
    for n in range(5):
        print(pascal(n))  
