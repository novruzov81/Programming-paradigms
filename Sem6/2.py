# процедурная парадигма
def calculate_mse(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Векторы должны иметь одинаковую длину")

    sum_of_squared_errors = 0
    for i in range(len(vector1)):
        squared_error = (vector1[i] - vector2[i]) ** 2
        sum_of_squared_errors += squared_error

    mse = sum_of_squared_errors / len(vector1)
    return mse

vector1 = [1, 2, 3, 4, 5]
vector2 = [2, 3, 4, 5, 6]

mse = calculate_mse(vector1, vector2)
print(mse)
