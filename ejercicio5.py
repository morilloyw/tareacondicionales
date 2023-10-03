dia =input("Ingresa un día de la semana: ")

if dia == "lunes":
    print("Es lunes.")
elif dia == "viernes":
    print("Es viernes.")
elif dia == "sabado" or dia == "domingo":
    print("Es fin de semana (sabado o domingo).")
else:
    print("No es lunes, viernes, sabado ni domingo.")