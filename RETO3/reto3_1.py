#########################################################################################
#############################--- SOLUCION DE RETO 3--- ##################################
#########################################################################################

try:
    x = 0
    #SOLICITANDO CANTIDAD DE ESTUDIANTES A REGISTRAR
    cant_estudiantes = int(input("Por favor ingresar el numero de estudiantes: \n"))
    #INICIALIZANDO UNA LISTA VACIA
    lista = []
    #INICIALIZANDO UN DICCIONARIO VACIO
    estudiantes = {}
    #EJECUTANDO BUCLE PARA SOLICITAR DATOS Y NOTAS DEL ESTUDIANTE
    while x < cant_estudiantes:
        nombre = input(f'Por favor ingresar el nombre del estudiante #{x+1}: \n')
        cant_notas = int(input(f'Ingresar la cantidad de notas para {nombre}: '))
        #INICIALIZANDO LISTA DE NOTAS
        notas = list(range(cant_notas))
        #EJECUTANDO BLUCLE PARA SOLICITAR LAS NOTAS DEL ESTUDIANTE
        i = 0
        while i < cant_notas:
            nota =  int(input(f'Ingrese Nota #{i+1}: '))
            #ALMACENANDO NOTA INGRESADA POR POSICION DE LA LISTA
            notas[i] = nota
            #VALIDANDO SI LA NOTA INGRESADA ESTA DENTRO DEL RANGO, CASO CONTRARIO VOLVERA A SOLICITAR INGRESAR A NOTA
            if nota < 0 or nota > 20:
                print ("Ingresar una nota valida (Mayor a 0 y menor a 20)")
            else:
                i += 1

        #CALCULANDO EL PROMEDIO DE NOTAS INGRESADAS
        promedio = sum(notas)/(cant_notas)
        #OBTENIENDO LA NOTA MAYOR DE TODAS
        nota_max = max(notas)
        #OBTENIENDO LA NOTA MENOR DE TODAS
        nota_min = min(notas)

        #REGISTRANDO LOS DATOS OBTENIDOS EN UN DICCIONARIO
        estudiantes = {
                'estudiante_'+str(x+1) : nombre,
                'notas' : notas,
                'promedio' : promedio,
                'nota_max' : nota_max,
                'nota_min' : nota_min
            }
        #AGREGANDO EL DICCIONARIO EN UNA LISTA
        lista.append(estudiantes)

        print ("========================================================")    

        x += 1

    #IMPRIMIENDO LA LISTA DE DICCIONARIOS
    for item in lista:
        print (item)

except Exception as ex:
    print ("ocurrio un error : " + str(ex))