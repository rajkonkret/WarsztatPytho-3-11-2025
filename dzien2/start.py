import pakiet

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()

from pakiet import fun

fun.powitanie()  # Hello!!

# jako alias
import pakiet.fun as pk

pk.powitanie()  # Hello!!

# jest w __init__.py w __all__
pakiet.info()  # Jestem pakietem
