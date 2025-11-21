print("Clasificador de Números (Par o Impar)")

for i in range(1 ,6):
    numero = int(input(f"Ingrese el número {i}: "))

    if numero % 2 == 0:
        print(f"El número {numero} es PAR")
    else:
        print(f" El número {numero} es IMPAR")

print("Programa finalizado. ¡Gracias por participar!")
