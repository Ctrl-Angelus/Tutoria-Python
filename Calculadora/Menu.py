#from Operaciones import sumar, resta
def menu():
    bandera = True
    bandera2 = True
    bandera3 = True
    while bandera:
        print("------------------------")
        print("|      Calculadora     |")
        print("------------------------")
        print("|| 1. Suma            ||")
        print("------------------------")
        print("|| 2. Resta           ||")
        print("------------------------")
        print("|| 3. Multiplicación  ||")
        print("------------------------")
        print("|| 4. División        ||")
        print("------------------------")
        print("|| 5. Salir           ||")
        print("------------------------")

        while bandera3:
            desicion = int(input("ingrese un numero:"))
            if desicion < 1 or desicion > 5:
                print("Debe seleccionar la opción correcta")
            else:
                bandera3 = False
        match desicion:
            case 1:
                numero1 = int(input("ingrese el primer numero:"))
                numero2 = int(input("ingrese el segundo numero:"))
                suma = numero1 + numero2
                print(f"el resultado es: {suma}")

            case 2:
                numero1 = int(input("ingrese el primer numero:"))
                numero2 = int(input("ingrese el segundo numero:"))
                resta = numero1 - numero2
                print(f"el resultado es: {resta}")

            case 3:
                numero1 = int(input("ingrese el primer numero:"))
                numero2 = int(input("ingrese el segundo numero:"))
                multiplicacion = numero1*numero2
                print(f"el resultado es: {multiplicacion}")

            case 4:
                while bandera2:
                    numero1 = int(input("ingrese el primer numero:"))
                    numero2 = int(input("ingrese el segundo numero:"))
                    if numero1 == 0 or numero2 == 0:
                        print("No se puede dividir en cero")
                    else:
                        division = numero1 / numero2
                        print(f"el resultado es: {division}")
                        bandera2 = False

            case 5:
                bandera = False

    print("Gracias por usar la calculadora")


