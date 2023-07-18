import operaciones_basicas
import time

def operador(operador):
    a = input("a. Digite un numero a " + operador + ": ")
    b = input("b. Digite un numero a " + operador + ": ")
    return a, b

def tablamul():
    a = input("Digite el numero a multiplicar: ")
    return a

eleccion_2 = 0
while eleccion_2 < 1:
    eleccion_1 = input("""
        que operacion matematica desea realizar
        Digite:
            1 - para sumar
            2 - para restar
            3 - para multiplicar
            4 - para dividir
            5 - Tablas de multiplicar

            0 para salir
            Digite la opcion: 
        """)
    if int(eleccion_1) == 1:
        a, b = operador("sumar")
        respuesta = operaciones_basicas.suma(a, b)
        print("= " + str(a) + " + " + str(b) + " = " + str(respuesta))
        eleccion_2 = input("quieres repetir? 1 - si - 2 - no: ")
    elif int(eleccion_1) == 2:
        a, b = operador("restar")
        respuesta = operaciones_basicas.resta(a, b)
        print("= " + str(a) + " - " + str(b) + " = " + str(respuesta))
        eleccion_2 = input("quieres repetir? 1 - si - 2 - no: ")
    elif int(eleccion_1) == 3:
        a, b = operador("multicar")
        respuesta = operaciones_basicas.multi(a, b)
        print("= " + str(a) + " + " + str(b) + " = " + str(respuesta))
        eleccion_2 = input("quieres repetir? 1 - si - 2 - no: ")
    elif int(eleccion_1) == 4:
        a, b = operador("dividir")
        respuesta = operaciones_basicas.divi(a, b)
        print("= " + str(a) + " - " + str(b) + " = " + str(respuesta))
        eleccion_2 = input("quieres repetir? 1 - si - 2 - no: ")
    elif int(eleccion_1) == 5:
        a = tablamul()
        for b in range(10):
            c = int(a) * int(b)
            print(str(a) + " * " + str(b) + " = " + str(c))
        eleccion_2 = input("quieres repetir? 1 - si - 2 - no: ")
    elif int(eleccion_1) == 0:
        print("Adios")
        break
    else:
        print("opcion erronea... vuelve a intentarlo")
        time.sleep(1)
    if int(eleccion_2) == 1:
        print("Adios")
        break
#   print(int(eleccion_2))
#   eleccion_2 = int(eleccion_2)
