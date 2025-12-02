def sumar(a, b, c, d, e):
    return a + b + c + d + e

def restar(a, b ):
    return a - b

def presentacion():
    print("--------------------------------------------")
    print("== Calculadora de ganancias == ")
    print("\nBienvenido, selecciona una de las opciones")
    print("\n1. Sumar ganancias ")
    print("2. Restar porcentaje de ganancias")
    print("3. Salir")
    print("\n--------------------------------------------")

while True:
    presentacion()
    opcion = input("\nElige una opción: ")

    if opcion == "3":
        print("\nSaliendo...")
        break

    try:

        if opcion == "1":
           
           n1 = float(input("Ingresa el primer número: "))
           n2 = float(input("Ingresa el segundo número: "))
           n3 = float(input("Ingresa el tercer número: "))
           n4 = float(input("Ingresa el cuarto número: "))
           n5 = float(input("Ingresa el quinto número: "))

           print("\nResultado:", sumar(n1, n2, n3, n4, n5))


        elif opcion == "2":
            nu1 = float(input("Ingrese el porcentaje que quiere restar: "))
            nu2 = float(input("Ingrese su ganancia total: "))
            result = nu1 / 100
            print("\nResultado :", restar(nu2, result))

        else:
            print("Opción inválida")



    except ValueError:
      print("Error: Solo se permiten números.")


  
