#Le damos la bienvenida al usuario
print("\n=======> BIENVENIDO A LA CALCULADORA <======= \n")

print("1.suma")
print("2.resta")
print("3.multiplicar")
print("4.dividir")
print("5.convertir de decimal a binario")
print("6.convertir de binario a decimal")
print("7.convertir de grados celsius a grados fahrenheit")
print("8.calcular el IMC")
print("9.convertir de cm a mt")
print("10.convertir de mt a cm")
print("11.convertir de mt a km")
print("12.convertir de km a mt")
print("13.convertir de segundos a minutos")
print("14.convertir de minutos a horas")
print("15.convertir de horas a minutos")

#
opcion=int(input("\nQue operacion desea realizar?\n"))

while True:
    #Suma
    if opcion == 1:
        num1=float(input("\nDigite el primer numero"))
        num2=float(input("\nDigite el segundo numero"))
        sum(num1+num2)
        print("\nel resultado de la suma es: ",sum)
        break

    #Resta
    elif opcion ==2:
        num1=float(input("\nDigite el primer numero"))
        num2=float(input("\nDigite el segundo numero"))
        resta=(num1-num2)
        print("\nEl resultado de la resta es: ", resta)
        break
    
    #Multiplicacion
    elif opcion == 3:
        num1=float(input("\ndigite el primer numero"))
        num2=float(input("\ndigite el segundo numero"))
        multiplicacion=(num1*num2)
        break
    
    #Division 
    elif opcion == 4:
        num1=int(input("\ndigite el primer numero"))
        num2=int(input("\ndigite el segundo numero"))
        div=(num1/num2)
        print("\nEl resultado de la division es:", div)
        break
    
    #Convertir decimal a binario
    elif opcion == 5:
        num1=int(input("\nDigite el numero que desea convertir a binario"))
        binnum=bin(num1)
        print(f"\n{binnum}")
        break
    
    #Convertir binario a decimal
    elif opcion == 6:
        num1=int(input("Digite su numero binario"))
        print(f"Su numero en decimal es:{int(str(num1),2)}")
        break
    
    #Convertir celsius a fahrenheit
    elif opcion == 7:
        celsius = int(input("\nIngrese los grados celsius que desea convertir a fahrenheit"))
        gradosf=(celsius*9/5+32)
        print(f"\nLos grados celcsius{celsius} convertidos a fahrenheit es: {gradosf}")
        break
    #Calcular imc
    elif opcion == 8:
        peso=int(input("\ningrese su peso en kg"))
        h=int(input("\nIngrese su estatura en centrimetros"))
        formula=(h*h/peso)
        print(f"\nEl resultado es: {formula}")
        break
    #convertir cm a m
    elif opcion == 9:
        cm=int(input("\nIngrese el valor de centimetros que desea convertir a metros"))
        formula=(cm/100)
        print(f"\nEl resultado de sus cm ({cm}) a metros es: {formula} metros")
        break
    #alreves
    elif opcion == 10:
        metros=int(input("\nIngrese el valor de metros que desea convertir a cm"))
        formula=(metros*100)
        print(f"\nEl resultado de sus metros ({metros}) a centimetros es: {formula} centimetros")
        break
    #metros a km
    elif opcion == 11:
        metros=int(input("\nIngrese el valor de metros que desea convertir a km"))
        formula=(metros/1000)
        print(f"\nEl resultado de sus metros ({metros}) a kilometros es: {formula} km")
        break
    #alreves km->m
    
    elif opcion == 12:
        km=int(input("\nIngrese el valor de km que desea convertir a metros"))
        formula=(km*1000)
        print(f"\nEl resultado de sus km ({km}) a metros es: {formula} metros")
        break
    #segundos a min
    
    elif opcion == 13:
        seg=int(input("\nDigite los segundos que desea convertir a minutos"))
        formula=int(seg/60)
        print(f"\nLos minutos son: {formula}") 
        break
    #min a horas
    
    elif opcion == 14:
        min=int(input("\nDigite los minutos que desea convertir a horas"))
        formula=int(min/60)
        print(f"\nLas horas son: {formula}") 
        break
    #alreves horas->min
    
    elif opcion == 15:
        hr=int(input("\nDigite las horas que desea convertir a minutos"))
        formula=int(hr*60)
        print(f"\nLos minutos son: {formula}") 
        break
        
