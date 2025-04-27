# Ejercicio 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4
numeros_multiplos_de_4 = list(range(4, 101, 4))
# Imprimir la lista
print(numeros_multiplos_de_4)

#Ejercicio 2
# Creo una lista con cinco elementos que me gustan
mi_lista = ["libros", "mate", "gatos", "playa", "música"]
# Muestro el penúltimo elemento usando indexing negativo
print(mi_lista[-2])

#Ejercicio 3
# Creo una lista vacía
lista_vacia = []
# Agrego tres palabras usando append
lista_vacia.append("sol")
lista_vacia.append("playa")
lista_vacia.append("mar")
# Imprimo la lista resultante
print(lista_vacia)

#Ejercicio 4
# Lista original
animales = ["perro", "gato", "conejo", "pez"]
# Reemplazo el segundo valor (índice 1) con "loro"
animales[1] = "loro"
# Reemplazo el último valor (índice -1) con "oso"
animales[-1] = "oso"
# Imprimo la lista resultante
print(animales)

#Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#el programa busca el numero mayo de una lista y lo elimina, luego muestra los numeros restantes

#Ejercicio 6
# Creo una lista con números del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))
# Muestro los dos primeros elementos
print(numeros[0:2])

#Ejercicio 7
# Lista original
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazo los dos valores centrales
autos[1:3] = ["ferrari", "mustang"]
# Mostrar la lista actualizada
print(autos)

#Ejercicio 8
# Crear una lista vacía llamada "dobles"
dobles = []
# Agregar el doble de 5, 10 y 15 usando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
# Imprimir la lista resultante
print(dobles)

#Ejercicio 9
#Creamos las tres listas de compras
compras1 = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras2 = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras3 = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Agregar "jugo" a la lista del tercer cliente usando append.
compras3[2].append("jugo")
# Primero buscar "fideos" en la lista del segundo cliente y reemplazarlo
indice_fideos = compras2[1].index("fideos")
# Luego reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras2[1][indice_fideos] = "tallarines"
#Eliminar "pan" de la lista del primer cliente.
compras1[0].remove("pan")
#Imprimir la lista resultante por pantalla
print(compras1)
print(compras2)
print(compras3)

#Ejercicio 10
# Crear la lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
# Imprimir la lista resultante
print(lista_anidada)