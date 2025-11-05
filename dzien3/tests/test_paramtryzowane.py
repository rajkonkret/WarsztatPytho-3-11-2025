import pytest


def divide(a, b):
    return a / b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (12, 3, 4),
    ]
)
def test_divide_ok(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a,b",
                         [
                             (1, 0),
                             (5, 0)
                         ]
                         )
def test_divide_raises(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
