import classTeam as ct

lista_equipos = []

def nuevo_equipo():
    if len(lista_equipos) < 4:
        while True:
            nombre_equipo = input("\nIngrese el nombre del equipo: ").capitalize()
            if len(lista_equipos) > 0:
                for j in lista_equipos:
                    if nombre_equipo == j.get_nombre():
                        print("Equipo existente, no se puede agregar.")
                        return
            if nombre_equipo.isdigit():
                print("Reintentar, nombre incorrecto")
            else:
                break
        nuevo_equipo = ct.Equipo(nombre_equipo)
        lista_equipos.append(nuevo_equipo)
        print("Equipo agregado con exito!!!")
        return
    else:
        print("El grupo de equipos esta lleno!!!")

def agregar_resultado():

    equipo_uno = input("\nIngrese el equipo uno: ").capitalize()
    var = 0
    for i in lista_equipos:
        if equipo_uno == i.get_nombre():
            print("Equipo existente")
            var = 1
    if var == 0:
        print("Equipo no existente")
        return

    equipo_dos = input("\nIngrese el equipo dos: ").capitalize()
    var_dos = 0
    for i in lista_equipos:
        if equipo_dos == i.get_nombre():
            print("Equipo existente")
            var_dos = 1
    if var_dos == 0:
        print("Equipo no existente")
        return

    while True:
        opcion = input(f"""
        Indique la opcion correcta:
        1. {equipo_uno} le gano a {equipo_dos}
        2. {equipo_dos} le gano a {equipo_uno}
        3. {equipo_uno} empato con {equipo_dos}
        Opcion: """)
        if opcion == "1":
            for i in lista_equipos:
                if equipo_uno == i.get_nombre():
                    i.set_puntaje(3)
                    print("Resultado agregado con exito!!!")
                    return
        elif opcion == "2":
            for i in lista_equipos:
                if equipo_dos == i.get_nombre():
                    i.set_puntaje(3)
                    print("Resultado agregado con exito!!!")
                    return
        elif opcion == "3":
            for i in lista_equipos:
                if equipo_uno == i.get_nombre():
                    i.set_puntaje(1)
            for i in lista_equipos:
                if equipo_dos == i.get_nombre():
                    i.set_puntaje(1)
            print("Resultado agregado con exito!!!")
            return
        else:
            print("Reintentar, valor incorrecto")

def mostrar_posicion():
    lista_resultados = []
    for i in lista_equipos:
        valores_de_puntajes = i.get_puntaje()
        lista_resultados.append(valores_de_puntajes)
    lista_resultados.sort(reverse=True)
    print("\n---Tabla de posiciones---")
    for i in lista_resultados:
        for j in lista_equipos:
            if i == j.get_puntaje():
                print(f"Equipo: {j.get_nombre()}, Puntos: {j.get_puntaje()}")



# def mostrar_equipos():
#     print("\n---EQUIPOS---")
#     for i in lista_equipos:
#         print(i.get_nombre())

# def mostrar_puntaje():
#     for i in lista_equipos:
#         print(i.get_puntaje())