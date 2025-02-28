


# The game starts here.

label start:

    #1. Pide al usuario que ingrese un número y determina si el número es positivo, negativo o cero.

    $ num = int(renpy.input("Ingresa un numero: "))

    if(num < 0):
        "[num] numero es negativo"
    elif (num > 0):
        "[num] numero es positivo"
    else:
        "[num] numero es cero"

    # Pide al usuario que ingrese tres números y determina cuál de ellos es el mayor.

    python:
        numeroMayor = 0
        for i in range(3):
            nume = int(renpy.input("Ingresa un numero: "))
            if(nume > numeroMayor):
                numeroMayor = nume
    "El numero mayo de los que ingresaste es [numeroMayor]"

    # Solicita la edad de una persona y clasifícala en una categoría:

    $ edad = int(renpy.input("Ingresa la edad de una persona: "))
    $ mensaje = ""

    if(edad < 18):
        $ mensaje = "Es menor de edad"
    elif(edad > 18 and edad < 64):
        $ mensaje = "Es adulto"
    elif(edad > 65):
        $ mensaje = "Es persona mayor"
    
    "[mensaje]"


    # Pide al usuario que ingrese un número y determina si es par o impar.

    $ numero = int(renpy.input("Ingresa un numero: "))

    if(numero % 2 == 0):
        "El numero es par"
    else:
        "El numero es impar"
    

    # Solicita una calificación de un examen (entre 0 y 100) y muestra un mensaje dependiendo del rango:
    # Si la calificación es mayor o igual a 90, imprime "Excelente"
    # Si está entre 70 y 89, imprime "Aprobado"
    # Si está entre 50 y 69, imprime "Regular"
    # Si es menor a 50, imprime "Reprobado"

    $ calificacion = int(renpy.input("Ingresa una calificacion del 0 al 100: "))

    if(calificacion >= 90 and calificacion <= 100 ):
        "Excelente"
    elif(calificacion <= 69 and calificacion >= 50):
        "Aprobado"
    elif(calificacion <= 89 and calificacion >= 50):
        "Regular"
    elif(calificacion < 50 and calificacion >=0):
        "Reprobado"
    else:
        "Numero no valido"
    


    # Pide al usuario que ingrese los tres lados de un triángulo y determina si es:
    # Equilátero (todos los lados iguales)
    # Isósceles (dos lados iguales)
    # Escaleno (todos los lados diferentes)
    # : 5, 5, 8
    # : "El triángulo es isósceles."7.

    python:
        lados = []
        mensaje=""
        for i in range(3):
            lado = int(renpy.input("Ingrese un a longitud para un lado del triangulo: "))
            lados.append(lado)

        if (lados[0]==lados[1] and lados[1] == lados[2]):
            mensaje = "El triángulo es equilatero"
        elif (lados[0] != lados[1] and lados[1] != lados[2] and lados[2] != lados[0]):
            mensaje="El triangulo es escaleno"
        else:
            mensaje="El triangulo es isósceles"
        
    "[mensaje]"

    # Pide al usuario un número entre 1 y 12 y determina el mes correspondiente. Si el número no está en ese rango, muestra un mensaje de error.
    # : 5
    # : "Mayo

    $ mes = int(renpy.input("Ingrese un numero del 1 al 12: "))

    if (mes==1):
        "El mes [mes] es enero"
    elif(mes==2):
        "El mes [mes] es febrero"
    elif(mes==3):
        "El mes [mes] es marzo"
    elif(mes==4):
        "El mes [mes] es abril"
    elif(mes==5):
        "El mes [mes] es mayo"
    elif(mes==6):
        "El mes [mes] es junio"
    elif(mes==7):
        "El mes [mes] es julio"
    elif(mes==8):
        "El mes [mes] es agosto"
    elif(mes==9):
        "El mes [mes] es septiembre"
    elif(mes==10):
        "El mes [mes] es octubre"
    elif(mes==11):
        "El mes [mes] es noviembre"
    elif(mes==12):
        "El mes [mes] es diciembre"
    else:
        "El numero no es valido para ningun mes"
    



    # Solicita un número y determina si es divisible por 3, por 5, o por ambos.
    # : 15
    # : "El número es divisible por 3 y por 5."9.
    $ numero = int(renpy.input("ingrese un numero: "))

    if(numero % 3 == 0 and numero % 5 == 0):
        "El número es divisible por 3 y por 5."
    elif(numero % 3 == 0):
        "El número es divisible por 3"
    elif(numero % 5 ==0):
        "El número es divisible por 5"
    else:
        "No es divisible ni por 3 ni por 5"



    # Crea una calculadora básica que pida al usuario dos números y una operación (suma, resta, multiplicación o división) y luego muestre el resultado.
    # : 5, 3, 'suma'
    # : "El resultado de la suma es 8."10.
    $ num1 = int(renpy.input("Ingrese un numero: "))
    $ num2 = int(renpy.input("Ingrese un segundo numero: "))
    $ operacion = (renpy.input("Ingrese la operacion que desea realiza: s para suma, r para resta, m para multiplicacion y d para division"))


    if(operacion == "s"):
        "El resultado de la suma es [num1 + num2]"
    elif(operacion == "r"):
        "El resultado de la resta es [num1 - num2]"
    elif(operacion == "m"):
        "El resultado de la multiplicación es [num1 * num2]"
    elif(operacion == "d"):
        "El resultado de la división es [num1 / num2]"
    else:
        "Operacion invalida"


    # Pide al usuario que ingrese un año y determina si es bisiesto o no. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
    # : 2024
    # : "El año 2024 es bisiesto."
    $ año = int(renpy.input("Ingrese un año: "))

    if((año % 4 == 0 and año%100!=0) or (año % 400 == 0)):
        "Es año bisiesto"
    else:
        "No es año bisiesto"

    return
