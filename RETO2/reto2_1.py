#########################################################################################
#############################--- SOLUCION DE RETO 2--- ##################################
#########################################################################################

try:
    #INGRESANDO NOMBRE DEL ESTUDIANTE
    estudiante = input("Ingrese el nombre del estudiante: \n")
    #INGRESANDO NUMERO DE NOTAS DEL ESTUDIANTE
    numero_notas = int(input("ingrese el numero de notas del estudiante: \n"))
    
    i = 0

    notas = list(range(numero_notas))

    while i < numero_notas:
        nota = int(input(f'Ingrese Nota {i+1} :'))
        notas[i] = nota 
        i += 1 

    #OBTENIENDO EL PROMEDIO DE LAS NOTAS INGRESADAS
    promedio = sum(notas)/len(notas)
    #OBTENIENDO LA MAYOR NOTAS DE TODAS
    nota_max = max(notas)
    #OBTENIENDO LA MENOR NOTA DE TODAS
    nota_min = min(notas)

    print ("===================================================")

    print (f'Las notas ingresadas del estudiante {estudiante} son: \n')

    print ("===================================================")
    #IMPRIMIENDO LA LISTA DE NOTAS
    #print (notas)

    #IMPRIMIENDO LAS NOTAS CON MEDIANTE UN FOR
    contador = 0
    j = 1
    for item in notas:
        print(f'Nota {j} : {notas[contador]}')
        contador += 1
        j += 1 
        
    print (f'El promedio de las {numero_notas} notas ingresadas es : --> {promedio}')
    print (f'La nota mas alta de las {numero_notas} notas ingresadas es : --> {nota_max}')
    print (f'La nota mas baja de las {numero_notas} notas ingresadas es : --> {nota_min}')

except Exception as ex:
    print("Ha ocurrido un inconveniente, codigo de error: " + str(ex))

