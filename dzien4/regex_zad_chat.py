import re
from functools import wraps

# --- Wzorce regex ---
ISBN10_RE = re.compile(r"^(?:\d[\s-]?){9}[\dX]$")
ISBN13_RE = re.compile(r"^(?:\d[\s-]?){13}$")

def validate_isbn(param_name: str = "isbn"):
    """
    Dekorator walidujący numer ISBN (ISBN-10 lub ISBN-13) z użyciem regex.
    Usuwa spacje i myślniki, sprawdza poprawność struktury i cyfry kontrolnej.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Pobranie wartości ISBN
            if param_name in kwargs:
                raw = kwargs[param_name]
                from_kwargs = True
            else:
                try:
                    raw = args[1]
                    from_kwargs = False
                except IndexError:
                    raise ValueError("Brak argumentu ISBN.")

            # Normalizacja
            isbn = str(raw).strip().upper()

            # Wstępne dopasowanie regex
            if ISBN10_RE.match(isbn):
                clean = re.sub(r"[\s-]", "", isbn)
                valid = _validate_isbn10(clean)
            elif ISBN13_RE.match(isbn):
                clean = re.sub(r"[\s-]", "", isbn)
                valid = _validate_isbn13(clean)
            else:
                raise ValueError("Niepoprawny format ISBN (dozwolone cyfry, myślniki lub spacje).")

            if not valid:
                raise ValueError("Niepoprawny numer ISBN (cyfra kontrolna).")

            # Aktualizacja argumentów
            if from_kwargs:
                kwargs[param_name] = clean
                return fn(*args, **kwargs)
            else:
                new_args = list(args)
                new_args[1] = clean
                return fn(*new_args, **kwargs)
        return wrapper
    return decorator


# --- Walidatory kontrolne ---
def _validate_isbn10(isbn: str) -> bool:
    """Sprawdza cyfrę kontrolną ISBN-10."""
    if len(isbn) != 10:
        return False
    total = sum((i + 1) * (10 if c == "X" else int(c)) for i, c in enumerate(isbn[:10]))
    return total % 11 == 0


def _validate_isbn13(isbn: str) -> bool:
    """Sprawdza cyfrę kontrolną ISBN-13."""
    if len(isbn) != 13:
        return False
    total = sum((int(c) * (1 if i % 2 == 0 else 3)) for i, c in enumerate(isbn[:12]))
    check = (10 - (total % 10)) % 10
    return check == int(isbn[-1])
