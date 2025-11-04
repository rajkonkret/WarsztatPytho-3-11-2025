# float() - liczby zmienooprzecinkowe
import sys

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024, max_10_exp=308,
#                min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

# liczby float posiadają bład zaokrąglenia
print(0.1 + 0.9)  # 1.0
print(0.1 + 0.3)  # 0.4
print(0.1 + 0.2)  # 0.30000000000000004
if (0.1 + 0.2) == 0.3:
    print("Prawda")
print(0.1 + 0.8)
print(0.1 + 0.7)  # 0.7999999999999999
# decimal - ominięcie problemu zaokrąglenia, głównie do obliczeń na pieniądzach
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

a = 0.1 + 0.2
a = round(a, 2)
print(a)  # 0.3
