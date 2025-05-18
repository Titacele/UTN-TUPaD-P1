#Ejercicio 1
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' en pantalla."""
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    """Devuelve un saludo personalizado con el nombre proporcionado."""
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime la información personal del usuario."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("¿Dónde vives?: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4
import math

def calcular_area_circulo(radio):
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Devuelve el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600

# Programa principal
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#Ejercicio 6
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar del número dado, del 1 al 10."""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    """Devuelve una tupla con la suma, resta, multiplicación y división de a y b."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultados = operaciones_basicas(a, b)

print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso, altura):
    """Calcula y devuelve el Índice de Masa Corporal (IMC)."""
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    """Calcula y devuelve el promedio de tres números."""
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {promedio:.2f}")
