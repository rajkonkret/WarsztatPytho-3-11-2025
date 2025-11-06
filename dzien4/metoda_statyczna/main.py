from daty import Dates
from ms_zad2 import Obliczanie

print(f"Wartość wynosi: {Obliczanie.oblicz(4, 63, 6)}")
# Wartość wynosi: 402

date = Dates("13-12-2025")
date_format_db = "13/12/2025"

date_with_dash = Dates.to_dash_date(date_format_db)
d1 = date.get_date()
d2 = date_with_dash

if (d1 == d2):
    print("Takie same daty")
    print(f"{d1} = {d2}")
else:
    print("Różne daty")
    print(f"{d1} != {d2}")
# Takie same daty
# 13-12-2025 = 13-12-2025