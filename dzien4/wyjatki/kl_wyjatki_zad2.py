class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("X must be integer")
    if not isinstance(y, int):
        raise MyTypeError("Y must be integer")
    if y == 0:
        raise MyValueError("Y cannot be zero")

    return x / y


print(my_function(3, 5))
# print(my_function(3, 5.9)) # MyTypeError: Y must be integer
# print(my_function(9.9, 9)) # MyTypeError: X must be integer
# print(my_function(5, 0))  # MyValueError: Y cannot be zero
