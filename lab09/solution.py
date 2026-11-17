import numpy as np  # Подключаем NumPy


def make_hours():
    hours = np.arange(0, 22, 3)
    # Создаём числа от 0 до 21 с шагом 3; граница 22 не входит.

    return hours.tolist()
    # Возвращаем обычный список Python.


def vector_report(values):
    arr = np.asarray(values, dtype=float)
    # Превращаем входной список в массив дробных чисел.

    return {
        "third": float(arr[2]),        # Третий элемент
        "last": float(arr[-1]),        # Последний элемент
        "middle": arr[2:6].tolist(),   # Индексы 2, 3, 4, 5
        "every_second": arr[::2].tolist(),  # Каждый второй с первого
        "reversed": arr[::-1].tolist()      # В обратном порядке
    }

def change_vector(values):
    arr = np.asarray(values, dtype=float).copy()
    # Создаём независимую копию массива для изменений.

    arr[2:5] = 99
    # Заменяем элементы с индексами 2, 3, 4 на 99.

    arr[::2] = -1
    # Затем заменяем каждый второй элемент, начиная с первого, на -1.

    return arr.tolist()
    # Возвращаем обычный список.


def cap_above(values, limit):
    arr = np.asarray(values, dtype=float).copy()
    # Создаём копию, чтобы не менять исходные данные.

    mask = arr > limit
    # Маска: True там, где значение больше limit, иначе False.

    arr[mask] = limit
    # Заменяем выбранные маской значения на limit.

    return arr.tolist()


def celsius_to_fahrenheit(values):
    arr = np.asarray(values, dtype=float)
    # Превращаем список температур в массив.

    result = arr * 9 / 5 + 32
    # Применяем формулу сразу ко всем температурам.

    return result.tolist()