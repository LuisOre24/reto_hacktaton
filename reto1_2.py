
################################################################################
################ --- SEGUNDA FORMA DE SOLUCION DE RETO #########################
################################################################################

try:
    #INICIALIZANDO LISTA CON UN RANGO FIJO
    notas = list(range(5))

    #ALMACENANDO LAS NOTAS MEDIANTE UN FOR
    i = 0
    for nota in notas:
        nota = int(input(f'Ingrese Nota #{i+1}: '))
        notas[i] = nota
        i += 1

    promedio = sum(notas)/len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print ("===================================================")

    print (f'Las notas ingresadas del estudiante son: \n')
    #IMPRIMIENDO LA LISTA DE NOTAS
    #print (notas)
    
    #IMPRIMIENDO LAS NOTAS CON MEDIANTE UN FOR
    contador = 0
    j = 1
    for num in notas:
        print(f'Nota {j} : {notas[contador]}')
        contador += 1
        j += 1 
        
    print (f'El promedio de las {len(notas)} notas ingresadas es : --> {promedio}')
    print (f'La nota mas alta de las {len(notas)} notas ingresadas es : --> {nota_max}')
    print (f'La nota mas baja de las {len(notas)} notas ingresadas es : --> {nota_min}')

except Exception as ex:
    print("Ha ocurrido un inconveniente, codigo de error: " + str(ex))


