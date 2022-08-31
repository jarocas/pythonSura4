#ENTRADAS: VARIABLES = REFERENCIAS EN MEMORIA 
nivelAgua = int(input("Digite el nivel de agua: "))

#PROCESOS:
if(nivelAgua >= 0 and nivelAgua < 20 ):
    print(f'El nivel de agua es {nivelAgua} m^3 y este es bajo')
elif(nivelAgua >=20 and nivelAgua < 400):
    print(f'Operando normalmente, nivel de agua es igual a {nivelAgua} m^3')
elif(nivelAgua >= 400):
    print(f'PELIGRO... el nivel de agua es igual a {nivelAgua} m^3')
else:
    print("El nivel de agua no es valido")


#SALIDA:

