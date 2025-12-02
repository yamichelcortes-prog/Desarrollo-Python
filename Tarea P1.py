def pedir_numero(mensaje):

    while True:
        try:
            entrada = input(mensaje)
            entrada = entrada.strip().replace(",", ".")
            return float(entrada)
        except ValueError:
            print(" Error: Debes ingresar un número válido. Intenta de nuevo.")


def main():
    print("Bienvenido a tu calculadora en Python")
    print("-----------------------------------------------")
    nombre = input("\nIngrese su nombre: ").strip()

    while True:
        print("\nSeleccione una opción:")
        print("1 Sumar")
        print("2 Restar")
        print("3 Multiplicar")
        print("4 Dividir")
        print("5 Salir")

        opcion = input("\nIngrese su opción: ").strip()

        if opcion == "1":
            print("-----------------------------------------------")
            print("\n¿Qué números quieres sumar?")
            a = pedir_numero("\nIngresa tu primer número: ")
            b = pedir_numero("Ingresa tu segundo número: ")
            print("\nSumando...")
            resultado = a + b
            print(f"\nHola {nombre}, el resultado es {resultado}")
            print("-----------------------------------------------")

        elif opcion == "2":
            print("-----------------------------------------------")
            print("\n¿Qué números quieres restar?")
            a = pedir_numero("\nIngresa tu primer número: ")
            b = pedir_numero("Ingresa tu segundo número: ")
            print("\nRestando...")
            resultado = a - b
            print(f"\nHola {nombre}, el resultado es {resultado}")
            print("-----------------------------------------------")

        elif opcion == "3":
            print("-----------------------------------------------")
            print("\n¿Qué números quieres multiplicar?")
            a = pedir_numero("\nIngresa tu primer número: ")
            b = pedir_numero("Ingresa tu segundo número: ")
            print("\nMultiplicando...")
            resultado = a * b
            print(f"\nHola {nombre}, el resultado es {resultado}")
            print("-----------------------------------------------")

        elif opcion == "4":
            print("-----------------------------------------------")
            print("\n¿Qué números quieres dividir?")
            a = pedir_numero("\nIngresa tu primer número: ")
            b = pedir_numero("Ingresa tu segundo número: ")
            print("\nDividiendo...")

            try:
                resultado = a / b
            except ZeroDivisionError:
                print("⚠️ Error: No se puede dividir entre cero.")
            else:
                print(f"\nHola {nombre}, el resultado es {resultado}")

            print("-----------------------------------------------")

        elif opcion == "5":
            print("-----------------------------------------------")
            print("\nSaliendo de la calculadora... ¡Hasta luego y gracias por visitarnos!")
            print("-----------------------------------------------")
            break

        else:
            print("\n-----------------------------------------------")
            print("\nLa opción es inexistente. Intente de nuevo.")
            print("\n-----------------------------------------------")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupción por teclado. Saliendo...")
