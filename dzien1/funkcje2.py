# funkcja wewnętrzna, funjkcja zagnieżdzona

def fun1():
    print("To jest funkcja1")

    def fun2():
        print("To jest fun2")

    # fun2() - zwrócenie wartości
    # znamy adres fun2
    return fun2  # zwrócenie adresu


fun1()
new_fun = fun1()
print(type(new_fun))  # <class 'function'>
print(new_fun)  # <function fun1.<locals>.fun2 at 0x0000012E3C283D80>
new_fun()
new_fun()
new_fun()
# To jest fun2
# To jest fun2
# To jest fun2

#
