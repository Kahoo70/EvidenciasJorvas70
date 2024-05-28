
'''RESERVEAS HOTEL TRIVAGO'''

#Presentación
print ("¡Bienvenido al hotel TRIVAGO!\n\n")
print ("Cuenta con un servicio de amigable y eficaz\n")
print ("A continuación puedes ver las habitaciones que tenemos disponibles \n\n")

#Seccion habitaciones
print ("______________________________\n")
print ("HABITACIONES DISPONIBLES\n\n\n")
print ("[1] | Habitación 101")
a1=1
print ("[2] | Habitación 102")
a2=2
print ("[3] | Habitación 103")
a3=3
print ("[4] | Habitación 201")
a4=4
print ("______________________________\n")

#Seleccion numero habitación
habitacion= int(input("Digite el numero de la habitacion que desea reservar : "))

#Habitacion 01
if habitacion == a1:
    print ("Ha elegido la Habitación 101\n")
    print ("ELIGE LA FECHA DE TU RESERVA\n\n")
    año = int(input("Digite el año (ejemplo: 2024) : "))
    mes= int (input("Digite el mes (ejemplo: 07) : "))
    
    #En caso de poner un dia o mes que no existe
    if mes > 12:
        print ("El mes no existe, vuelve a ejecutar el programa")
    else: 
        dia = int(input("Digite el dia (ejemplo: 14) : "))
        #En caso de poner un dia o mes que no existe
        if (dia < 0) or (dia > 31):
            print ("El dia no existe, por favor vuelva a ejecutar el programa")
        else:
            print ("La fecha que has elegido es:",dia,"/",mes,"/",año,"\n")
            
            #Seccion de datos personales
            print ("\n")
            print ("DIGITE SUS DATOS PERSONALES\n")
            nombre= str(input("Escriba sus nombres y apellidos (completos)  : "))
            identificación= int(input("Digite su numero de identificación : "))
            tel= int(input("Digite su numero telefonico : "))

            #Seccion de cuota
            print ("\n")
            print ("CUOTA DE RESERVA DIGITAL\n")
            print ("La cuota para la habitación $20000")
            cuota = int(input("Digite la cantidad acordada para la reserva : "))
            if (cuota < 20000):
                print ("Saldo ingresado insuficiente!")
            else:
                if (cuota == 20000):
                    print ("Has reservado la habitacion con exito!!")
                    #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 101| ")
                    print ("_________________________")

#SECCION CANCELAR SIN TERMINAR                    
                    #print("¿DESEA CANCELAR LA RESERVA?[No se le reenvolsara el dinero de la reserva]")
                    #cancelar= int(print("SI=[1] Y NO=[2]"))
                    #if cancelar <1:
#  
                else:
                    if (cuota > 20000):
                        ope=cuota-20000
                        print ("Su cambio de la reserva es: ",ope)

                        #Seccion informe
                        print ("_________________________\n")
                        print ("La persona : ",nombre)
                        print ("Identificado con el ID : ",identificación)
                        print ("Con el telefono : ",tel)
                        print ("Reservo con exito la |habitacion 101| ")
                        print ("_________________________")
                    

                    


                





#Habitacion 02
elif habitacion == a2:
    print ("Ha elegido la habitacion 102")
    print ("ELIGE LA FECHA DE TU RESERVA\n\n")
    año = int(input("Digite el año (ejemplo: 2024) : "))
    mes= int (input("Digite el mes (ejemplo: 07) : "))
    
    #En caso de poner un dia o mes que no existe
    if mes > 12:
        print ("El mes no existe, vuelve a ejecutar el programa")
    else: 
        dia = int(input("Digite el dia (ejemplo: 14) : "))
        #En caso de poner un dia o mes que no existe
        if (dia < 0) or (dia > 31):
            print ("El dia no existe, por favor vuelva a ejecutar el programa")
        else:
            print ("La fecha que has elegido es:",dia,"/",mes,"/",año)

            #Seccion de datos personales
            print ("\n")
            print ("DIGITE SUS DATOS PERSONALES\n")
            nombre= str(input("Escriba sus nombres y apellidos (completos)  : "))
            identificación= int(input("Digite su numero de identificación : "))
            tel= int(input("Digite su numero telefonico : "))

                        #Seccion de cuota
            print ("\n")
            print ("CUOTA DE RESERVA DIGITAL\n")
            print ("La cuota para la habitación $20000")
            cuota = int(input("Digite la cantidad acordada para la reserva : "))
            if (cuota < 20000):
                print ("Saldo ingresado insuficiente!")
            else:
                if (cuota == 20000):
                    print ("Has reservado la habitacion con exito!!")
                    #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 102| ")
                    print ("_________________________")
                else:
                    if (cuota > 20000):
                        ope=cuota-20000
                        print ("Su cambio de la reserva es: ",ope)
                        #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 102| ")
                    print ("_________________________")




#Habitacion 03
elif habitacion == a3:
    print ("Ha elegido la habitacion 103")
    print ("ELIGE LA FECHA DE TU RESERVA\n\n")
    año = int(input("Digite el año (ejemplo: 2024) : "))
    mes= int (input("Digite el mes (ejemplo: 07) : "))
    
    #En caso de poner un dia o mes que no existe
    if mes > 12:
        print ("El mes no existe, vuelve a ejecutar el programa")
    else: 
        dia = int(input("Digite el dia (ejemplo: 14) : "))
        #En caso de poner un dia o mes que no existe
        if (dia < 0) or (dia > 31):
            print ("El dia no existe, por favor vuelva a ejecutar el programa")
        else:
            print ("La fecha que has elegido es:",dia,"/",mes,"/",año)

             #Seccion de datos personales
            print ("\n")
            print ("DIGITE SUS DATOS PERSONALES\n")
            nombre= str(input("Escriba sus nombres y apellidos (completos)  : "))
            identificación= int(input("Digite su numero de identificación : "))
            tel= int(input("Digite su numero telefonico : "))

                        #Seccion de cuota
            print ("\n")
            print ("CUOTA DE RESERVA DIGITAL\n")
            print ("La cuota para la habitación $20000")
            cuota = int(input("Digite la cantidad acordada para la reserva : "))
            if (cuota < 20000):
                print ("Saldo ingresado insuficiente!")
            else:
                if (cuota == 20000):
                    print ("Has reservado la habitacion con exito!!")
                    #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 103| ")
                    print ("_________________________")
                else:
                    if (cuota > 20000):
                        ope=cuota-20000
                        print ("Su cambio de la reserva es: ",ope)
                        #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 103| ")
                    print ("_________________________")







#Habitacion 05
elif habitacion == a4:
    print ("Ha elegido la habitacion 201")
    print ("ELIGE LA FECHA DE TU RESERVA\n\n")
    año = int(input("Digite el año (ejemplo: 2024) : "))
    mes= int (input("Digite el mes (ejemplo: 07) : "))
    
    #En caso de poner un dia o mes que no existe
    if mes > 12:
        print ("El mes no existe, vuelve a ejecutar el programa")
    else: 
        dia = int(input("Digite el dia (ejemplo: 14) : "))
        #En caso de poner un dia o mes que no existe
        if (dia < 0) or (dia > 31):
            print ("El dia no existe, por favor vuelva a ejecutar el programa")
        else:
            print ("La fecha que has elegido es:",dia,"/",mes,"/",año)


             #Seccion de datos 
            print ("\n")
            print ("DIGITE SUS DATOS PERSONALES\n")
            nombre= str(input("Escriba sus nombres y apellidos (completos)  : "))
            identificación= int(input("Digite su numero de identificación : "))
            tel= int(input("Digite su numero telefonico : "))

                        #Seccion de cuota
            print ("\n")
            print ("CUOTA DE RESERVA DIGITAL\n")
            print ("La cuota para la habitación $20000")
            cuota = int(input("Digite la cantidad acordada para la reserva : "))
            if (cuota < 20000):
                print ("Saldo ingresado insuficiente!")
            else:
                if (cuota == 20000):
                    print ("Has reservado la habitacion con exito!!")
                    #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 201| ")
                    print ("_________________________")
                else:
                    if (cuota > 20000):
                        ope=cuota-20000
                        print ("Su cambio de la reserva es: ",ope)
                        #Seccion informe
                    print ("_________________________\n")
                    print ("La persona : ",nombre)
                    print ("Identificado con el ID : ",identificación)
                    print ("Con el telefono : ",tel)
                    print ("Reservo con exito la |habitacion 201| ")
                    print ("_________________________")






    #Si no elije nunguno mostrar
else:
    print ("\n")
    print ("Elija un numero que se encuentre dentro de la disponibilidad de habitaciones")




