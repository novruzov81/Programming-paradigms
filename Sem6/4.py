# процедурная парадигма

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

array = [2, 5, 7, 10, 15, 20, 23]
search_number = 10

result = binary_search(array, search_number)

if result != -1:
    print(f"Искомый элемент найден в позиции {result}")
else:
    print("Искомый элемент не найден")

