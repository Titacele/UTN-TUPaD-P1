#Ejercicio 1
def factorial(n):
    return 1 if n==0 else n * factorial(n - 1)

# Solicitar al usuario un número
n = int(input("Introduce un número entero positivo: "))
print(f"El factorial de {n} es: {factorial(n)}")

#Ejercicio 2
# Función recursiva para calcular el número de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario una posición
n = int(input("Introduce una posición entera no negativa para la serie de Fibonacci: "))
print(f"El número de Fibonacci en la posición {n} es: {fibonacci(n)}")
for i in range(n + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

#Ejercicio 3
# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)

# Algoritmo general para probar la función
# Solicitar al usuario base y exponente
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

# Verificar que el exponente sea válido
if exponente < 0:
    print("Este algoritmo solo admite exponentes enteros no negativos.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")

#Ejercicio 4
# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    return "" if n==0 else decimal_a_binario(n // 2) + str(n % 2)

# Algoritmo general para probar la función
n = int(input("Introduce un número entero positivo: "))

if n == 0:
    print("El número binario es: 0")
else:
    binario = decimal_a_binario(n)
    print(f"El número {n} en binario es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la subcadena sin primera y última letra
    return es_palindromo(palabra[1:-1])

# Prueba de la función
texto = input("Introduce una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')

#Ejercicio 6
def suma_digitos(n):
    return n if n<10 else n % 10 + suma_digitos(n // 10)
# Solicitar un número al usuario
n = int(input("Introduce un número entero positivo: "))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

#Ejercicio 7
def contar_bloques(n):
    return 1 if n==1 else n + contar_bloques(n - 1)
#Solicitar nro al ususario
n = int(input("Introduce un número entero positivo: "))
print(f"El número de bloques necesarios para construir una pirámide de {n} niveles es: {contar_bloques(n)}")

#Ejercicio 8
def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito es igual al buscado
        contador = 1 if numero % 10 == digito else 0
        # Llamada recursiva con el resto del número
        return contador + contar_digito(numero // 10, digito)

# Solicitar un número y un dígito al usuario
numero = int(input("Introduce un número entero positivo: "))
digito = int(input("Introduce un dígito (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")

