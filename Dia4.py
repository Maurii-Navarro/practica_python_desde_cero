#Pequeña practica de un ejercicio que muestra si un numero
#Ingresado por teclado es positivo, negativo o cero y a la vez si es par o impar

print("Verificar si un numero es Positivo o Negativo, Par e Impar")

numero=int(input("Ingrese el numero:  "))

if numero > 0 and numero %2==0:
    print("Su numero es POSITIVO y PAR")
elif numero > 0 and numero%2==1:
    print("Su numero es POSITIVO e IMPAR")
elif numero <0 and numero%2==0:
    print("Su numero es NEGATIVO y PAR")
elif numero <0 and numero %2==1:
    print("Su numero es NEGATIVO e IMPAR")
elif numero ==0:
    print("TU NUMERO ES EL PODEROSISIMO CERO!!")