##o - 14 o 14 - 28 o 28 - 60 o 

edad = int(input("Digite una edad"))

if(edad >= 0 and edad < 14):
    print(f'La edad digitada es {edad}, el sujeto es un Niño.')
elif(edad >= 14 and edad <= 28):
    print(f'La edad digitada es {edad}, el sujeto es un Joven.')
elif(edad >= 28 and edad <= 60):
    print(f'La edad digitada es {edad}, el sujeto es un Adulto.')
else:
    print("La edad digitada no es válida...")