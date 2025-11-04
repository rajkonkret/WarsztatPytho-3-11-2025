def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


c_d = count_down(3)
c_u = count_up_to(3)


# for n in c_u:
#     print(n)
#
# for n in c_d:
#     print(n)


# 1
# 2
# 3
# 3
# 2
# 1

def combined(gen1, gen2):
    yield from gen1
    yield from gen2


c = combined(c_u, c_d)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

for i in c:
    print(i)
# 1
# 2
# 3
# 3
# 2
# 1

dane = [x for x in range(5)]
print(dane)  # [0, 1, 2, 3, 4]
print(type(dane))  # <class 'list'>

# generator składany
dane2 = (x for x in [1, 2, 3, 4, 5])
print(type(dane2))  # <class 'generator'>
print(dane2)  # <class 'generator'>

print(next(dane2))
print(next(dane2))
print(next(dane2))
print(next(dane2))
print(next(dane2))


# print(next(dane2))  # StopIteration

def genrator3():
    for x in [1, 2, 3, 4, 5]:
        yield x

g3 = genrator3()

print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))