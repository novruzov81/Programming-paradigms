

def sort_numbers(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers = [5, 2, 9, 1, 7]
sort_numbers(numbers)
print(numbers)

