mesAño = input("Digite un mes del año y conozca su estación: ")
mesMinus = mesAño.lower()

if(mesMinus == 'enero' or mesMinus == 'febrero' or mesMinus == 'marzo'):
    print(f'{mesMinus} corresponde a INVIERNO')
elif(mesMinus == 'abril' or mesMinus == 'mayo' or mesMinus == 'junio'):
    print(f'{mesAño} corresponde a PRIMAVERA')
elif(mesMinus == 'julio' or mesMinus == 'agosto' or mesMinus == 'septiembre'):
    print(f'{mesAño} corresponde a VERANO')
elif(mesMinus == 'octubre' or mesMinus == 'noviembre' or mesMinus == 'diciembre'):
    print(f'{mesMinus} corresponde a OTOÑO')
else:
    print(f'{mesMinus} no corresponde a un mes del año...')