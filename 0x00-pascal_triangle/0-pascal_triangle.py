def pascal_triangle(n):
    """
    program to generate pascals triangle
    """
    results = []
    if n <= 0:
        return results
    else:
        for i in range(n):
            row = [1]
            if results:
                last_row = results[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            results.append(row)
    return results
