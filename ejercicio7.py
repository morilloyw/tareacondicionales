edad = int(input("Introduce tu edad: "))

ingresos_mensuales = float(input("Introduce tus ingresos mensuales en euros: "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("Debes tributar este impuesto.")
else:
    print("No tienes que tributar.")
