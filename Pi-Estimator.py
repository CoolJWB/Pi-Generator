# Using the Gregory-Leibniz series you can calculate Pi (roughly).
# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

import decimal
Pi = decimal.Decimal('3')
sized = 2

while True:
    Pi = Pi + decimal.Decimal((4/(sized * (sized + 1) * (sized + 2))))
    sized = (sized + 2)
    Pi = Pi - decimal.Decimal((4/(sized * (sized + 1) * (sized + 2))))
    sized = (sized + 2)
    print(Pi)
