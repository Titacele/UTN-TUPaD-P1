#Ejercico 1
for i in range(101):
    print(i)

#Ejercicio 2
numero = input("Introduce un número entero: ")
if numero.startswith('-'):
    cantidad_digitos = len(numero) - 1
else:
    cantidad_digitos = len(numero)
print(f"El número tiene {cantidad_digitos} dígitos.")

#Ejercicio 3
valor_inferior = int(input("Introduce el valor inferior: "))
valor_superior = int(input("Introduce el valor superior: "))
suma = 0
for i in range(valor_inferior + 1, valor_superior):
    suma += i
print(f"La suma de los números entre {valor_inferior} y {valor_superior} (excluyendo los extremos) es: {suma}")

#Ejercicio 4
total = 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"El total acumulado es: {total}")

#Ejercicio 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0
print("Bienvenido al juego de adivinar el número.")
print("Adivina un número entre 0 y 9.")
while True:
    intento = int(input("Introduce tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break 
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")

#Ejercicio 6
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#Ejercicio 7
n = int(input("Introduce un número entero positivo: "))
if n < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"La suma de los números desde 1 hasta {n} es: {suma}")

#Ejercicio 8
cantidad_numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número #{i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\n--- Resultados ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#Ejercicio 9
cantidad_numeros = 100
suma_total = 0
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número #{i+1}: "))
    suma_total += numero
media = suma_total / cantidad_numeros
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

#Ejercicio 10
numero = input("Ingresa un número entero: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")
