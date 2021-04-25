try:
    print("Ingresar las 5 notas del estudiante")
    nota_1 = int(input("Ingresar nota 1: \n"))
    nota_2 = int(input("ingresar nota 2: \n"))
    nota_3 = int(input("ingresar nota 3: \n"))
    nota_4 = int(input("ingresar nota 4: \n"))
    nota_5 = int(input("ingresar nota 5: \n"))

    notas = [nota_1, nota_2, nota_3, nota_4, nota_5]
    promedio = sum(notas)/len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print ("===================================================")

    print (f'Las notas ingresadas del estudiante son: \n')
    #IMPRIMIENDO LA LISTA DE NOTAS
    #print (notas)
    
    #IMPRIMIENDO LAS NOTAS CON MEDIANTE UN FOR
    contador = 0
    i = 1
    for num in notas:
        print(f'Nota {i} : {notas[contador]}')
        contador += 1
        i += 1 
        
    print (f'El promedio de las 05 notas ingresadas es : --> {promedio}')
    print (f'La nota mas alta de las 05 notas ingresadas es : --> {nota_max}')
    print (f'La nota mas baja de las 05 notas ingresadas es : --> {nota_min}')

except Exception as ex:
    print("Ha ocurrido un inconveniente, codigo de error: " + str(ex))


