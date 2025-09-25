# IMPORTAR Y ESTILO

import time

def print2(mensaje):
    for caracter in mensaje:
        print(caracter, end="", flush=True)
        time.sleep(0.02)
    print()
    
def input2(mensaje_input):
    for caracter in mensaje_input:
        print(caracter, end="", flush=True)
        time.sleep(0.02)
    respuesta = input()
    return respuesta

def sumador1(nombre1):
    total1 = 0
    for caracter in nombre1:
        caracter = caracter.lower()
        total1 = total1 + (ord(caracter) - 96)
    return(total1)

def sumador2(nombre2):
    total2 = 0
    for caracter in nombre2:
        caracter = caracter.lower()
        total2 = total2 + (ord(caracter) - 96)
    return(total2)

#RESTO

print2("¡Bienvenido al comprobador de compatibilidad!")
time.sleep(0.5)
print2("Introduce dos nombres para comprobar su porcentaje de compatibilidad.")
time.sleep(0.5)
print2("El nombre debe estar escrito sin tildes.")
time.sleep(0.5)
nombre1 = input2("Introduce el primer nombre: ")
total1 = sumador1(nombre1)
nombre2 = input2("Introduce el segundo nombre: ")
total2 = sumador2(nombre2)
if total1 > total2:
    compatibilidad1 = total2 / total1 * 100
elif total1 < total2:
    compatibilidad1 = total1 / total2 * 100
else:
    compatibilidad1 = 100
caracteres1 = len(nombre1)
caracteres2 = len(nombre2)
if caracteres1 > caracteres2:
    compatibilidad2 = (caracteres2 / caracteres1) * 100
elif caracteres1 < caracteres2:
    compatibilidad2 = (caracteres1 / caracteres2) * 100
else:
    compatibilidad2 = 100
compatibilidad = (compatibilidad1 + compatibilidad2) / 2
compatibilidad = round(compatibilidad, 2)
print("Compatibilidad total: ", end="")
print(str(compatibilidad), end="")
print("%")