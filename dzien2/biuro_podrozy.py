import wycieczka

print(25 * "-")

kw = wycieczka.kwota(
    transport=500,
    nocleg=800,
    wyzywienie=300,
    wycieczki=300,
    ubezpieczenie=100,
    inne=50,
    rabat=5
)

print("Kwota: ", kw)
# -------------------------
# Kwota:  1985.0
