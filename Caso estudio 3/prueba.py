def distribucion_cal():
    camiones_cargados = 0

    while camiones_cargados < 20:
        capacidad_camion = int(input("Ingrese la capacidad del camión en kg: "))
        peso_saco = int(input("Ingrese el peso del saco en kg: "))

        if capacidad_camion > 0 and peso_saco > 0:
            if peso_saco <= capacidad_camion:
                print("Cargar saco en el camión.")
                capacidad_camion -= peso_saco
            else:
                print("Despachar camión para cargar otro.")
                camiones_cargados += 1
        else:
            print("La capacidad del camión y el peso del saco deben ser mayores que cero.")

distribucion_cal()
