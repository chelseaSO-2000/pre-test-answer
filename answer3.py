def calculateSeriesSum (n, cur):
    if (not cur):
        cur = 0
        
    if n < 2:
        raise ValueError('Invalid input')
    
    for x in range (3,n+1):
        cur += 1 / (n * (n -1))
        n-= 1
    return 1 / n + cur

result = calculateSeriesSum (1, 0)
print(f'Result for n={n}: {result}')

result = calculateSeriesSum (2, 0)
print(f'Result for n={n}: {result}')

result = calculateSeriesSum (10, 0)
print(f'Result for n={n}: {result}')