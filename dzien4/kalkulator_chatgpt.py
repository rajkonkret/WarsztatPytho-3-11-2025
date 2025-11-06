def kalkulator():
    print("=== KALKULATOR PYTHON ===")
    print("Dostępne operacje:")
    print("1. Dodawanie (+)")
    print("2. Odejmowanie (-)")
    print("3. Mnożenie (*)")
    print("4. Dzielenie (/)")
    print("5. Potęgowanie (^)")
    print("6. Zakończ")

    while True:
        wybor = input("\nWybierz operację (1-6): ")

        if wybor == "6":
            print("Do zobaczenia! 👋")
            break

        if wybor not in ["1", "2", "3", "4", "5"]:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
            continue

        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Błąd: wpisz poprawne liczby.")
            continue

        if wybor == "1":
            wynik = a + b
            symbol = "+"
        elif wybor == "2":
            wynik = a - b
            symbol = "-"
        elif wybor == "3":
            wynik = a * b
            symbol = "*"
        elif wybor == "4":
            if b == 0:
                print("Błąd: nie można dzielić przez zero!")
                continue
            wynik = a / b
            symbol = "/"
        elif wybor == "5":
            wynik = a ** b
            symbol = "^"

        print(f"Wynik: {a} {symbol} {b} = {wynik}")

if __name__ == "__main__":
    kalkulator()
