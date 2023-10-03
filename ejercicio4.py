num1=int(input("Dime el primer  número: "))
num2=int(input("Dime el segundo número: "))
num3=int(input("Dime el tercer  número: "))

if num1 > num2 and num1 > num3 :
    print ("El numero primero es el mayor")
elif num2 > num1 and num2 > num3:
    print ("El numero segundo es mayor")
elif num3 > num2 and num3 > num1:
    print ("El numero tercero es mayor")    