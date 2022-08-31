#ENTRADAS: VARIABLES = REFERENCIAS EN MEMORIA 
nivelAgua = int(input("Digite el nivel de agua: "))

#PROCESOS:
if(nivelAgua >= 0 and nivelAgua < 20 ):
    #SALIDA:
    print(f'El nivel de agua es {nivelAgua} m^3 y este es bajo')
elif(nivelAgua >=20 and nivelAgua < 400):
    #SALIDA:
    print(f'Operando normalmente, nivel de agua es igual a {nivelAgua} m^3')
elif(nivelAgua >= 400):
    #SALIDA:
    print(f'PELIGRO... el nivel de agua es igual a {nivelAgua} m^3')
else:
    #SALIDA:
    print("El nivel de agua no es valido")




