#Ejercicio 1
edad = int(input("¿Cuántos años tienes? "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#Ejercicio 2
nota = int(input("¿Cuál es la nota? "))

if edad >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("¿Cuál es tu edad? "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5
contraseña = input("Introduce tu contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode, median, mean

# Crear una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, la mediana y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Evaluar el sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#Ejercicio 7
frase = input("Introduce una frase o palabra: ")

# Verificar si la última letra es una vocal
if frase[-1].lower() in 'aeiou':
    # Si termina con vocal, añadir un signo de exclamación
    print(frase + '!')
else:
    # Si no termina con vocal, imprimir el string tal cual
    print(frase)

#Ejercicio 8
nombre = input("Introduce tu nombre: ")

# Mostrar las opciones
print("Elige una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")

# Solicitar la opción seleccionada
opcion = int(input("Ingresa el número de la opción que deseas: "))

# Realizar la transformación de acuerdo a la opción seleccionada
if opcion == 1:
    # Convertir a mayúsculas
    print(nombre.upper())
elif opcion == 2:
    # Convertir a minúsculas
    print(nombre.lower())
elif opcion == 3:
    # Convertir a la primera letra mayúscula
    print(nombre.title())
else:
    print("Opción inválida. Por favor ingresa 1, 2 o 3.")

#Ejercicio 9
magnitud = float(input("Introduce la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
# Solicitar al usuario el hemisferio, mes y día
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Función para determinar la estación según el hemisferio, mes y día
def determinar_estacion(hemisferio, mes, dia):
    if hemisferio == 'N':  # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
            return "Verano"
        else:  # Otoño
            return "Otoño"

    elif hemisferio == 'S':  # Hemisferio Sur
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
            return "Invierno"
        else:  # Primavera
            return "Primavera"
    else:
        return "Hemisferio inválido"

# Llamar a la función para determinar la estación
estacion = determinar_estacion(hemisferio, mes, dia)

# Imprimir el resultado
if estacion != "Hemisferio inválido":
    print(f"En el hemisferio {'norte' if hemisferio == 'N' else 'sur'}, la estación es {estacion}.")
else:
    print("Hemisferio inválido. Por favor, ingresa 'N' o 'S'.")
