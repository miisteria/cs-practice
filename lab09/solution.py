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