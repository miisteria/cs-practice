import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    array = np.asarray(values, dtype=float)
    matrix = array.reshape(-1, width)

    return np.round(matrix, 6).tolist()


def block(
    matrix: list[list[float]],
    rows: list[int],
    columns: list[int]
) -> list[list[float]]:
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return []

    result = array[np.ix_(rows, columns)]

    return np.round(result, 6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return []

    means = array.mean(axis=0)

    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    array = np.asarray(matrix, dtype=float)

    if array.size == 0:
        return 0.0

    values = array[:, column]
    result = values.max() - values.min()

    return float(np.round(result, 6))