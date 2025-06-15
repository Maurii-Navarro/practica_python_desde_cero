import random

datos_curiosos = [
    "El primer virus informático ('Creeper', 1971) solo mostraba un mensaje y fue eliminado por el primer antivirus ('Reaper').",
    "El 'Hello, World!' se usó en C (1978) porque era la forma más simple de probar si un programa funcionaba.",
    "El hacker más joven fue arrestado a los 12 años ('CyFi') por explotar juegos móviles.",
    "El 40% del código en proyectos grandes es 'zombie': nadie lo usa pero temen borrarlo.",
    "El teclado QWERTY se diseñó para ser lento y evitar atascos en máquinas de escribir mecánicas."
]

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

verificacion= input("Quieres que te de un dato curioso?, contesta si o no: ").lower()
if verificacion =="si":
    print(">>>>", random.choice(datos_curiosos))
else:
    print("Hacete ree culiar ", nombre)
