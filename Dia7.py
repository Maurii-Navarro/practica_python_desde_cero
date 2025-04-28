#Practica de listas, diccionarios y tuplas

#Ahora lo que voy a crear es un programa que:
#recibira numeros flotantes o decimales
#sumara los elementos de una lista
#sacara el promedio de los numeros sumados
#y se mostrara el numero mas grande y mas pequeño de la lista

numeros = []
numeros.append(float(input("Ingresa el primer número: ")))
numeros.append(float(input("Ingresa el segundo número: ")))
numeros.append(float(input("Ingresa el tercer número: ")))
numeros.append(float(input("Ingresa el cuarto número: ")))
numeros.append(float(input("Ingresa el quinto número: ")))

suma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
promedio = suma / 5

mayor = max(numeros)
menor = min(numeros)

print("Lista:", numeros)
print("Suma:", suma)
print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)