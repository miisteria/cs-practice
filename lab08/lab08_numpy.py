import numpy as np  # Подключаем NumPy под коротким именем np


# Задание 1. Создание массивов

hours = np.arange(0, 22, 3)
# Числа от 0 до 21 с шагом 3. Правая граница 22 не входит.

line = np.linspace(0, 1, 5)
# Пять равномерно расположенных чисел от 0 до 1 включительно.

zeros = np.zeros(6, dtype=int)
# Шесть нулей целого типа.

unknown_table = np.full((2, 3), -1)
# Таблица: 2 строки, 3 столбца, все значения равны -1.

identity = np.eye(3)
# Единичная матрица 3 × 3: по главной диагонали единицы, остальное — нули.

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)  # Форма массива: (8,)
print("ndim:", hours.ndim)    # Количество измерений: 1
print("size:", hours.size)    # Количество элементов: 8
print("dtype:", hours.dtype)  # Тип элементов

print("line:", line)
print("zeros:", zeros)
print("unknown_table:")
print(unknown_table)
print("identity:")
print(identity)


# Задание 2. Индексы и срезы вектора

print("Задание 2")
print("Третий элемент:", hours[2])
# Индексы начинаются с 0, поэтому третий элемент имеет индекс 2.

print("Последний элемент:", hours[-1])
# Индекс -1 означает последний элемент.

print("Элементы с индексами 2–5:", hours[2:6])
# Берём индексы 2, 3, 4, 5. Правая граница 6 не входит.

print("Каждый второй элемент:", hours[::2])
# От начала до конца с шагом 2.

print("Обратный порядок:", hours[::-1])
# Шаг -1: идём с конца к началу.


# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("Задание 3")
print("Форма:", temperatures.shape)  # (3, 4)
print("Число измерений:", temperatures.ndim)  # 2
print("Число элементов:", temperatures.size)  # 12

print("Вторая строка, третий столбец:", temperatures[1, 2])
# Сначала указываем индекс строки, потом столбца.

print("Первая строка:", temperatures[0])

print("Последний столбец:", temperatures[:, -1])
# : — все строки, -1 — последний столбец.

print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
# Строки с индексами 0 и 1; столбцы с индекса 1 до конца.

center = temperatures[0:2, 1:3]
# Строки с индексами 0, 1 и столбцы с индексами 1, 2.

print("Центральный фрагмент:")
print(center)
print("Его форма:", center.shape)

# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)
# Создаём числа от 1 до 25 и размещаем в таблице 5 × 5.

print("Задание 4")
print("Исходная матрица:")
print(matrix)

first_rows = matrix[:3, :]
# Первые три строки, все столбцы.

print("Первые три строки:")
print(first_rows)
print("Форма:", first_rows.shape)

last_rows = matrix[-2:, :]
# Последние две строки, все столбцы.

print("Последние две строки:")
print(last_rows)
print("Форма:", last_rows.shape)

first_columns = matrix[:, :2]
# Все строки, первые два столбца.

print("Первые два столбца:")
print(first_columns)
print("Форма:", first_columns.shape)

fragment = matrix[1:4, 2:5]
# Строки с индексами 1, 2, 3; столбцы с индексами 2, 3, 4.

print("Фрагмент:")
print(fragment)
print("Форма:", fragment.shape)

corner = matrix[-2:, -2:]
# Последние две строки и последние два столбца.

print("Правый нижний блок:")
print(corner)
print("Форма:", corner.shape)


# Задание 5. Изменение массива через срезы

# Сначала примеры из условия:

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
# Заменяем элементы с индексами 1, 2, 3 на нули.

print("Задание 5")
print("Пример с вектором:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
# Заменяем всю первую строку на -1.

small_matrix[1:, 1:] = 9
# В строках с индекса 1 и столбцах с индекса 1 ставим 9.

print("Пример с матрицей:")
print(small_matrix)


changed_hours = hours.copy()
# Создаём независимую копию, чтобы сохранить исходный hours.

changed_hours[2:5] = 99
# Элементы с индексами 2, 3, 4 заменяем на 99.

changed_hours[::2] = -1
# Затем каждый второй элемент, начиная с первого, заменяем на -1.

print("Изменённый hours:", changed_hours)
print("Исходный hours:", hours)


changed_matrix = matrix.copy()
# Создаём независимую копию исходной матрицы.

changed_matrix[1, :] = 0
# Вторая строка — нули.

changed_matrix[:, -1] = -1
# Последний столбец — значения -1.

changed_matrix[1:4, 1:4] = 100
# Центральный блок 3 × 3 — значения 100.

print("Изменённая матрица:")
print(changed_matrix)

print("Исходная матрица:")
print(matrix)


# Задание 6. Изменение формы

numbers = np.arange(0, 12)
# Числа от 0 до 11: всего 12 элементов.

table = numbers.reshape(3, 4)
# Располагаем их в 3 строки по 4 элемента.

transposed = table.T
# Транспонируем: строки становятся столбцами.

print("Задание 6")
print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)

print("Таблица:")
print(table)

print("После транспонирования:")
print(transposed)

# reshape(3, 4) работает, потому что 3 * 4 = 12 элементов.
# reshape(5, 3) вызовет ошибку: нужно 15 элементов, а у нас 12.