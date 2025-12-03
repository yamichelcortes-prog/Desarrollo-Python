def sumar(a, b, c, d, e):
    return a + b + c + d + e

def restar(a, b ):
    return a - b



def hope ():
    print ("Ingrese cinco ganancias:")

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
           
           print("\n--------------------------------------------")
           hope()
           n1 = float(input("1: "))
           n2 = float(input("2: "))
           n3 = float(input("3: "))
           n4 = float(input("4: "))
           n5 = float(input("5: "))
           sum= sumar(n1, n2, n3, n4, n5)

           print(f"\nResultado: B/. {sum:.2f}")


        elif opcion == "2":
            print("\n--------------------------------------------")
            nu1 = float(input("Ingrese el porcentaje que quiere restar: "))
            nu2 = float(input("Ingrese su ganancia total: "))
            result = nu1 / 100
            res = result * nu2
            rest= restar  (nu2, res)
            print (f"\n Resultado: B/. {rest:.2f}")

        else:
            print("Opción inválida")



    except ValueError:
      print("Error: Solo se permiten números.")
      