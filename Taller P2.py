import random

print("🎮 Bienvenido al juego: Adivina el número 🎮")
print("Estoy pensando en un número del 1 al 20...")

# El número que la computadora elige
numero_secreto = random.randint(1,20)

# Variable para controlar el bucle
adivinado = False

# Bucle principal
while not adivinado: 
    intento = int(input("Escribe un número: "))

    if intento < numero_secreto:
        print("Demasiado bajo. Intenta otra vez.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta otra vez")
    else:
        print("¡Felicidades! Adivinaste el número 🎉")
        adivinado = True

print("Gracias por jugar.")
