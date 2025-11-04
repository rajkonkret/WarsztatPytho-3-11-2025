import time
import tracemalloc
import numpy as np

# numpy - do działań na tablicach i macierzach, napisana w C
# pip install numpy

# tracemalloc.start()

# array1 = np.arange(10_000_000, dtype=np.int64)
array1 = np.arange(10_000_000, dtype=np.int8)
# array2 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int8)

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
