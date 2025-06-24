#Ejercicio1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio2
# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio3
# Lista de frutas (sin precios)
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# Ejercicio4
# Agenda telefónica
agenda = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre a consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# Ejercicio5
frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencia)

# Ejercicio6
alumnos = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} - Promedio: {promedio:.2f}")

# Ejercicio7
parcial1 = {101, 102, 103, 104}
parcial2 = {103, 104, 105, 106}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio8
stock = {'Pan': 10, 'Leche': 20, 'Huevos': 30}

producto = input("Ingrese el producto a consultar o actualizar: ")

if producto in stock:
    agregar = int(input(f"Hay {stock[producto]} unidades. ¿Cuántas desea agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio9
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de Python"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (formato HH:MM): ")

evento = agenda.get((dia, hora), "No hay actividad registrada.")
print(f"Actividad: {evento}")

# Ejercicio10
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)

