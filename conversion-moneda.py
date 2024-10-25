 # Paso 1 : Definir el valor actual del Euro y Dolar con respecto al Peso Argentino

tipo_cambio_eur_a_ars = 1066 # En un caso más realista habría que consumir información actualizada de una BDD o API
tipo_cambio_usd_a_ars = 985 # En un caso más realista habría que consumir información actualizada de una BDD o API

# Paso 2 : Solicitar al usuario el tipo de conversión (euro a ars o dolara ars)

tipo_conversion = input("Ingrese la moneda origen para la conversión(EUR/USD): ")

# Paso 3 : Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4 : Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso 5 : Mostrar el resultado de la conversión al usuario

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_ars
    print("El resultado de la conversión de EUR a ARS es:", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_ars
    print("El resultado de la conversión de USD a ARS es:", resultado)
else:
    print("No está disponible este tipo de cambio de conversión actualmente")
