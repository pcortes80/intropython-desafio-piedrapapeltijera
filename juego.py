# Importa librerias
import sys
import random

# Lee la opcion del usuario ingresada y la guarda en la variable "opcion_usuario"
opcion_usuario = sys.argv[1] # lee el primer argumento del script : opcion del usuario
        
if opcion_usuario == "piedra" or opcion_usuario == "papel" or opcion_usuario == "tijera":
    
    # Genera un número random y se lo asigna a la opcion del computador
    # La funcion randomint(a,b) genera valores aleatorios entre a y b, incluyendo los extremos
    numero_random = random.randint(1,3)
    if numero_random == 1:
        opcion_computador = "piedra" 
    elif numero_random == 2:
        opcion_computador = "papel"
    elif numero_random == 3:
        opcion_computador = "tijera"
    print("Computador juega " + opcion_computador + ".")
    
    # Revisa si la opción del usuario es la misma que la opción del computador
    if opcion_usuario == opcion_computador:
        print("Empate!")
else:
    # Mensaje al usuario
    print("Argumento inválido: debe ser piedra, papel o tijera.")
    
# Fin del programa
