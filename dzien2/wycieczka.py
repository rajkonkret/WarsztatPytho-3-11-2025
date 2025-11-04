def procent_na_ulamek(fn):
    def wrapper(transport, nocleg, rabat, *args, **kwargs):
        rate = rabat / 100
        return fn(transport, nocleg, rate, *args, **kwargs)

    return wrapper


@procent_na_ulamek
def oblicz_rabat(transport, nocleg, rabat):
    return (transport + nocleg) * rabat


def kwota(transport, nocleg, wyzywienie, wycieczki, ubezpieczenie, inne, rabat=0.0):
    rabat_kwota = oblicz_rabat(transport, nocleg, rabat)
    koszt_rabatowany = (transport + nocleg) - rabat_kwota
    koszt_pelny = wyzywienie + wycieczki + ubezpieczenie + inne
    suma = koszt_pelny + koszt_rabatowany
    return round(suma, 2)


# rabaty = [0.0, 0.05, 0.10, 0.15, 0.20]
rabaty = [0, 5, 10, 15, 20]  # procentowo
print(25 * "-")

for r in rabaty:
    kw = kwota(
        transport=500,
        nocleg=800,
        wyzywienie=300,
        wycieczki=300,
        ubezpieczenie=100,
        inne=50,
        rabat=r
    )
    # print(f"Rabat: {int(r * 100)}% -> {kw:.2f} zł")
    print(f"Rabat: {r:>3}% -> {kw:.2f} zł")
# >3 - wyrównaj do prawej, ustaw szerokosc kolumny na 3
# .2f - zaokrąglaj wyświetlanie do 2 miejsc po przecinku
# -------------------------    -------------------------
# Rabat: 0% -> 2050.00 zł      Rabat:   0% -> 2050.00 zł
# Rabat: 5% -> 1985.00 zł      Rabat:   5% -> 1985.00 zł
# Rabat: 10% -> 1920.00 zł     Rabat:  10% -> 1920.00 zł
# Rabat: 15% -> 1855.00 zł     Rabat:  15% -> 1855.00 zł
# Rabat: 20% -> 1790.00 zł     Rabat:  20% -> 1790.00 zł
