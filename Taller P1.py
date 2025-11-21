# --- Primera clase de Python ---
# Tema: Variables,entrada de datos, operaciones y salida

# Pedidor datos al usuario
nombre = input ("Ingrese su nombre:")
horas = float (input("Ingrese las horas trabajadas esta semana: "))
pago_hora = float(input("Ingrese el pago por hora: "))

# Calculamos el salario total
salario = horas  * pago_hora

# Mostramos el resultado
print("\n--- Resultado ---")
print(f"Hola {nombre}, tu salario semanal es: ${salario:.2f}")
