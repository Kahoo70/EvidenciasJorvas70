#Caso de Estudio 3: Programa Distribución de Cal. Solucione: Una central distribuye cal hacia diferentes almacenes sucursales. Disponen de un muelle de carga a donde van llegando Sacos de cal de entre 3000 y 9000 kg, con pesos variables en función de las circunstancias de la producción. La empresa dispone de una flota de camiones con capacidades de carga de entre 18000 y 28000 kg. Se pretende establecer un protocolo que consiste en cargar 20 camiones diarios. Cada camión se quiere cargar como máximo a su límite de capacidad teniendo este que partir, si con la siguiente saca en la línea de producción fuera a exceder su capacidad. La empresa quiere desarrollar un programa que le pida al operario encargado de carga la capacidad del camión y el peso de las Sacos, indicándole si debe cargar la saca o despachar el camión para comenzar a cargar otro. (Sena Virtual)
# Mostramos un mensaje de bienvenida al usuario
print("Bienvenido al programa para calcular las cargas de los camiones")

# Inicializamos una variable para contar los camiones cargados
camiones_cargados = 0

# Usamos un ciclo 'while' para repetir el proceso hasta que se carguen todos los camiones necesarios
while camiones_cargados < 20:
    # Pedimos al usuario que ingrese la capacidad del camión
    capacidad_camion = int(input("Ingrese la capacidad del camion ENTRE 18000kg y 28000kg: "))
    
    # Verificamos si la capacidad del camión está dentro del rango permitido
    if capacidad_camion < 18000 or capacidad_camion > 28000:
        print("Error: La capacidad del camion debe estar entre 18000kg y 28000kg.")
        continue
    
    # Pedimos al usuario que ingrese el peso del saco
    peso_saco = int(input("Ingrese el peso de los sacos ENTRE 3000kg y 9000kg: "))
    
    # Verificamos si el peso del saco está dentro del rango permitido
    if peso_saco < 3000 or peso_saco > 9000:
        print("Error: El peso del saco debe estar entre 3000kg y 9000kg.")
        continue
    
    # Utilizamos un bucle 'while' para cargar tantos sacos como sea posible en el camión
    while peso_saco > 0 and capacidad_camion >= peso_saco:
        print("Cargar saco en el camión.")
        capacidad_camion -= peso_saco
        peso_saco = int(input("Ingrese el peso de los sacos o 0 para finalizar: "))
    
    # Si la capacidad del camión llega a cero, significa que está lleno y se debe despachar
    if capacidad_camion == 0:
        print(" EL CAMION ESTA LLENO. Despachar camión para cargar otro.")
        camiones_cargados += 1
    else:
        print("Despachar camión para cargar otro.")
        camiones_cargados += 1