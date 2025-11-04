import time
import tracemalloc
import numpy as np

# numpy - do działań na tablicach i macierzach, napisana w C
# pip install numpy

# tracemalloc.start()

array1 = np.arange(10_000_000, dtype=np.int64)
# array1 = np.arange(10_000_000, dtype=np.int8)
array2 = np.arange(10_000_000, dtype=np.int64)
# array2 = np.arange(10_000_000, dtype=np.int8)

# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# print(array1.dtype)  # int64
# print(np.iinfo(np.int64))
# print(np.iinfo(np.int32))
# print(np.iinfo(np.int8))
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# Machine parameters for int32
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------
# Machine parameters for int8
# ---------------------------------------------------------------
# min = -128
# max = 127
# ---------------------------------------------------------------
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
# Current memory usage: 76.29412841796875 MB
# Peak memory usage: 76.29412841796875 MB
# Current memory usage: 19.07366943359375 MB
# Peak memory usage: 19.07366943359375 MB
# int8

#
# tracemalloc.start()

lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


#
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# # Current memory usage: 762.9238739013672 MB
# # Peak memory usage: 762.9239807128906 MB


def measure_time(func):
    def wrapper(*args, **kwargs):
        # start_time = time.time()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        # end_time = time.time()
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji: {func.__name__}: {execution_time} s")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)  # zatrzymuje program na 2 sek


@measure_time
def add_without_np():
    result = [lista1[i] + lista2[i] for i in range(len(lista1))]
    return "OK"


@measure_time
def add_with_for():
    result = []
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)
    return "OK for"


# zip() - łaczy kolekcje
@measure_time
def add_zip():
    result = [a + b for a, b in zip(lista1, lista2)]
    return "OK ZIP"


@measure_time
def add_np():
    result = array1 + array2
    return "ok np"


my_time()  # Czas wykonania funkcji: my_time: 2.000600814819336 s
add_without_np()  # Czas wykonania funkcji: add_without_np: 0.9913549000048079 s
add_with_for()  # Czas wykonania funkcji: add_with_for: 1.3092078999616206 s
add_zip()  # Czas wykonania funkcji: add_zip: 0.9316708999685943 s
add_np()  # Czas wykonania funkcji: add_np: 0.041484100045636296 s
