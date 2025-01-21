def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

n = int(input("Введите n: "))
result = sum_of_squares(n)
print("Сумма квадратов от 1 до", n, "равна:", result)
