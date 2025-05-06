# practicando ahora sobre condicionales if else
#calculadora de promedios de notas y verificacion de aprobacion final

a=int(input("Introduzca la primer nota de la evaluacion:  "))
b=int(input("Introduzca la segunda nota de la evaluacion:  "))
c=int(input("Introduzca la tercer nota de la evaluacion:  "))
d=int(input("Introduzca la cuarta nota de la evaluacion:  "))
e=int(input("Introduzca la quinta nota de la evaluacion:  "))

promedio=a+b+c+d+e
promedio= promedio /5

if promedio >= 6:
    print("FELICIDADES, acabas de pasar")
    print(promedio)
else:
    print("DESAPROBADO")
    print(promedio)
