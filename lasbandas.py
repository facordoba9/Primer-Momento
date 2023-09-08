print("***BANDAS PRI PRA***")
print("**********************")
print("0. Salir")
print("1. Registrar Banda")
print("2. Lista de Bandas")
print("3. Cambios de Hora")
print("4. Retirar Banda")
print("**********************")

elige=1
bandas=[]

while elige !=0:
    banda={}
    #Opcion de agregar bandas de una manera completa con ciertos datos
    elige=int(input("Digite una opción: "))
    if elige==1:
        banda["id"]=int(input("Ingrese su id: "))
        banda["nombre"]=input("Nombre de la Banda: ")
        banda["genero"]=input("Genero Musical: ")
        banda["hora"]=input("Hora de pesentación: ")
        banda["pago"]=float(input("Pago de la banda: "))
        estado = input("¿La agrupación ya se presentó? (True/False): ").lower()
        banda["estado"] = estado == 'true' 
        
        bandas.append(banda)
        print(f"{banda['nombre']} ha sido registrado.")
    #Mostramos bandas que no han tocado 
    elif elige == 2:
        print("Agrupaciones no presentadas:")
        for banda in bandas:
            if not banda["estado"]:
                print(f"ID: {banda['id']}, Nombre: {banda['nombre']}, Hora de presentación: {banda['hora']}")
    #Damos la opcion de cambiar la hora segun el id registrado
    elif elige == 3:
        id_a_cambiar = int(input("Ingrese el ID de la banda a la que desea cambiar la hora: "))
        banda_encontrada = False 

        for banda in bandas:
            if banda["id"] == id_a_cambiar and not banda["estado"]:
                banda_encontrada = True
                while True:
                    nueva_hora = input(f"Ingrese la nueva hora de presentación para {banda['nombre']} (HH:MM): ")
                    # Verificar si la entrada es una hora válida en formato "HH:MM"
                    if len(nueva_hora) == 5 and nueva_hora[2] == ':' and nueva_hora[:2].isdigit() and nueva_hora[3:].isdigit():
                        banda["hora"] = nueva_hora
                        print(f"Hora de presentación actualizada para {banda['nombre']}.")
                        break
                    else:
                        print("Hora inválida. Ingrese la hora en formato HH:MM.")

        if not banda_encontrada:
            print("No se encontró una banda con el ID especificado o la banda ya se presentó.")

    elif elige == 4:
        id_a_retirar = int(input("Ingrese el ID de la banda que desea retirar: "))
        for banda in bandas:
            if banda["id"] == id_a_retirar and not banda["estado"]:
                bandas.remove(banda)
                print(f"{banda['nombre']} ha sido retirado del listado de bandas.")
                break
        else:
            print("La opción es inválida (la banda ya se presentó o el ID no existe).")

    elif elige == 5:
        print("Todas las bandas registradas:")
        for banda in bandas:
            print(f"ID: {banda['id']}, Nombre: {banda['nombre']}, Género: {banda['genero']}, Hora de presentación: {banda['hora']}, Pago: ${banda['pago']}, ¿Ya se presentó? {banda['estado']}")

    elif elige == 0:
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        