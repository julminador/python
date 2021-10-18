def conversor(tipo_pesos, valor_dolar):
    pesos = float(input(tipo_pesos + " a convertir: $"))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " UDS")

menu = """Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos

Elija una opción:"""

opcion = input(menu)

if opcion == "1":
    conversor("COP", 3841.10)
elif opcion == "2":
    conversor("ARS", 98.56)
else:
    print("Opción invalida")