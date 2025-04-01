#Este programa es la practica de entrada y salida de datos, operadores numericos
# y condicionales

#Calculadora de IMC (Índice de Masa Corporal) con Diagnóstico

peso= int(input("Indique su peso (en Kg): "))
altura= float(input("Indique su altura (metros, punto decimal y centimetros): "))

IMC = peso /altura**2

if IMC < 18.5:
    print("Bajo Peso")
elif 18.5 <= IMC < 24.9:
    print("Peso Normal")
elif 25 <= IMC < 30:
    print("SobrePeso")
if IMC >30.1:
    print("Obesidad")
