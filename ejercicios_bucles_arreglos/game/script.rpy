

label start:

    #1. Crea un arreglo de números y calcula la suma total de sus elementos usando un bucle for.
    python:
        numeros = [1,2,3,4,5]
        suma = 0
        for value in numeros:
            suma += value
            
        
    "Suma de valores: [suma]"
    
    #. Dado un arreglo de números encuentra el número más grande usando un bucle for

    python:

        numeros = [10, 20, 4, 45, 99]

        numeroMayor = 0
        for numero in numeros:
            if(numero > numeroMayor):
                numeroMayor = numero
        
    "El numero más grande de la lista es: [numeroMayor]"

    #3. Dado un arreglo, cuenta cuántos elementos tiene. Usa un bucle for para recorrer la lista.

    python:
        
        frutas = ["Manzana", "Banano", "Cereza"]

        cuenta = 0
        for fruta in frutas:
            cuenta += 1
        
    "Hay [cuenta] elementos de frutas en el arreglo de frutas"

    #4. Crea un arreglo con números y calcula el promedio de todos los elementos.

    python:
        calificaciones = [90, 85, 78, 92, 88]

        sumaCalificaciones = 0
        promedio = 0

        for nota in calificaciones:
            sumaCalificaciones += nota

        promedio = sumaCalificaciones/len(calificaciones)

    "El promedio de calificaciones es [promedio]"    


    #5. Dado un arreglo, invierte el orden de sus elementos sin usar el método .reverse().

    python:
        palabras = ["apple", "banana", "cherry"]
        palabrasInvertidas = []

        for palabra in palabras:
            palabrasInvertidas.insert(0, palabra)

        palabras = palabrasInvertidas
        
    "Palabras en orden inversio = [palabras]"


    #6. Crea un arreglo con números o palabras, y elimina todos los elementos duplicados usando un bucle.

    python:
        elementos = [1, 2, 2, 3, 4, 4, 5]
        no_duplicados = []
        for num in elementos:
            if (not num in no_duplicados):
                no_duplicados.append(num)
        
        elementos = no_duplicados
    
    "Elementos no duplicados: [elementos]"

    #7. Dado un número, genera su tabla de multiplicar (del 1 al 10) y guárdala en un arreglo.
    python:
        

        def crearTablaMultipicar(multiplicando, multiplicadorLimite):
            valoresTabla = []
            for i in range(1, multiplicadorLimite + 1):
                valoresTabla.append(multiplicando * i)
            return valoresTabla
        
        numero = 7
        multiplicadorLimite = 10

        valores = crearTablaMultipicar(numero, multiplicadorLimite)

        
    "Tabla del [numero] con límite de multiplicador [multiplicadorLimite]: [valores]"

    #8. Crea una función que reciba un valor y un arreglo, y verifique si el valor está presente en el arreglo. Devuelve un mensaje adecuado.

    python: 

        def existeValor(color, colores):
            if color in colores:
                return f"Valor {color} SÍ existe en arreglo: {colores}"
            else:
                return f"Valor {color} NO existe en arreglo: {colores}"

        colores = ["rojo", "azul", "verde", "amarillo"]
        mensaje = existeValor("gris", colores)

    "[mensaje]"

    #9. Dado un arreglo de números, crea una lista que solo contenga los números pares.
    python:
        numeros = [1, 2, 3, 4, 5, 6]
        pares = []
        for num in numeros:
            if (num % 2 == 0):
                pares.append(num)
    
    "Los numeros pares de la lista [numeros] son: [pares]"


    #10. Dado un arreglo de cadenas, concatena todas las cadenas en una sola.

    python:
        
        palabras = ["Hola", "mundo", "Python", "es", "genial"]
        cadena = ""
        for palabra in palabras:
            cadena += palabra

    "[cadena]"


    #11. Utiliza un bucle for para generar una pirámide de números.

    python:
        n = 5
        linea = ""
        piramide = ""
        
        for i in range(1, n+1):
            
            linea += str(i) 
            piramide += linea + "\n"
    
    "[piramide]"

    return
