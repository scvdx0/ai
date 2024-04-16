# ref: https://m.boostcourse.org/ai222/lecture/22957
from typing import Iterable


def add_vectors(*vectors: tuple[int, ...]) -> list[int]:
    # v1 + v2 ...
    return [sum(col) for col in zip(*vectors)]


def add_vects_with_scalar_product(alpha: int, *vectors: tuple[int, ...]) -> list[int]:
    # alpha * (v1 + v2 ...)
    return [alpha * sum(col) for col in zip(*vectors)]


def add_matrices(*matrices: Iterable[tuple[int, ...]]) -> list[list[int]]:
    return [[sum(col) for col in zip(*rows)] for rows in zip(*matrices)]


def scalar_product(alpha: int, matrix: Iterable[tuple[int, ...]]) -> list[list[int]]:
    return [[alpha * e for e in row] for row in matrix]


def traspose(matrix: list[list[int]]) -> list[list[int]]:
    return [[e for e in col] for col in zip(*matrix)]


def product_matrices(
    matrix_a: tuple[tuple[int, int, int], tuple[int, int, int]],
    matrix_b: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
) -> list[list[int]]:
    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)]
        for row_a in matrix_a
    ]


if __name__ == "__main__":
    assert add_vectors((2, 2), (2, 3), (3, 5)) == [7, 10]
    assert add_vects_with_scalar_product(2, (1, 2, 3), (4, 5, 6)) == [10, 14, 18]

    matrix_a = ((3, 6), (4, 5))
    matrix_b = ((5, 8), (3, 7))
    assert add_matrices(matrix_a, matrix_b) == [[8, 14], [7, 12]]
    assert scalar_product(4, ((3, 6), (4, 5))) == [[12, 24], [16, 20]]
    assert traspose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

    matrix_a = ((1, 2, 3), (4, 5, 6))
    matrix_b = ((1, 4), (2, 5), (3, 6))
    assert product_matrices(matrix_a, matrix_b) == [[14, 32], [32, 77]]
