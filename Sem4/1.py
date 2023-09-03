from math import sqrt

def mean(arr):
    return sum(arr) / len(arr)

def pearson_correlation(x, y):
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    sum_xy = sum(map(lambda a, b: (a - mean_x) * (b - mean_y), x, y))
    sum_x_squared = sum(map(lambda a: (a - mean_x) ** 2, x))
    sum_y_squared = sum(map(lambda b: (b - mean_y) ** 2, y))

    correlation = sum_xy / (sqrt(sum_x_squared) * sqrt(sum_y_squared))
    return correlation


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print(correlation)

