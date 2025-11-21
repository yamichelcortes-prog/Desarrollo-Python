import random

print("📌 Bienvenido al Programa de Utilidades en Python")
print("-----------------------------------------------")

# Bucle principal del menú
while True:
    print("\n Seleccione una opción:")
    print("1 Contar del 1 al número que elijas")
    print("2 Mini juego: Adivina el número")
    print("3 Salir")

    opcion = input("Ingrese su opción: ")

    # Opción 1: Contar del 1 al número
    if opcion == "1":
        limite = int(input("¿Hasta qué número quieres contar?: "))
        print("\nContando...")
        for i in range(1, limite + 1):
            print(i)
        print("✔ Conteo terminado")

    # Opción 2: Adivina el número
    elif opcion == "2":
        secreto = random.randint(1, 10)
        print("Estoy pensando en un número del 1 al 10...")
        adivinado = False

        while not adivinado:
            intento = int(input("Adivina el número: "))

            if intento < secreto:
                print("Muy bajo, intenta otra vez.")
            elif intento > secreto:
                print("Muy alto, intenta otra vez.")
            else:
                print("🎉 ¡Correcto! Ese era el número.")
                adivinado = True

    # Opción 32
    # : Salir
    elif opcion == "3":
        print("Saliendo del programa... ¡Hasta luego!")
        break

    # Opción inválida
    else:
        print("❌ Opción incorrecta. Intente de nuevo.")