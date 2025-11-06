from decimal import Decimal

kwota1 = Decimal("45.78")
kwota2 = Decimal("7.80")

suma = kwota1 + kwota2
print("Sum is:", suma)  # Sum is: 53.58

precyzja = Decimal("0.00")

podatek = Decimal("0.23")
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)  # Kwota z podatkiem: 56.3094
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))  # Kwota z podatkiem: 56.31
