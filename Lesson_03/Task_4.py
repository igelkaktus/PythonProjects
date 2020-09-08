'''
4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''
def my_pow_func(x, y):
    # y - целое отрицательное
    try:
        x, y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x
        return 1 / res
    except ValueError:
        return 'Check value'
