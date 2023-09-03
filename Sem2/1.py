
def multiplication_table(n):
    for i in range(1, n+1):      # итерируемся по числам от 1 до n
        for j in range(1, 10):   # итерируемся по числам от 1 до 9 для получения таблицы умножения до 9
            print(f"{i} * {j} = {i*j}")
        print()  # добавляем пустую строку после каждой строки таблицы умножения

n = int(input("Введите число n: "))
multiplication_table(n)

