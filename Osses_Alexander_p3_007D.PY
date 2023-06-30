import funciones
import os
import msvcrt

funciones.validar_rut
funciones.validar_nombre
funciones.validar_nom_mascota
funciones.validar_cant_dias
funciones.validar_salida
funciones.arreglo_zeros

while True:
    os.system('cls')
    print("""       MENÚ LA GUARDERIA 
        MASCOTA SEGURA
    1.Registro de Mascota
    2.Buscar registro Mascotas
    3.Retirarse y pagar
    4.Salir""")

    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                break
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")
    if opc==1:
        while True:
            try:
                rut = int(input("Ingrese rut: "))
                if rut >= 1000000 and rut <= 99999999:
                    break
                else:
                    print("ERROR! RUT ENTRE 1000000 Y 99999999!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        while True:
            nom = input("Ingrese nombre: ")
            if len(nom.strip()) >= 3 and nom.isalpha():
                break
            else:
                print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        while True:
            nom_mascota = input("Ingrese nombre mascota: ")
            if len(nom_mascota.strip()) >= 3 and nom_mascota.isalpha():
                break
            else:
                print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        while True:
            try:
                dias = int(input("Ingrese cantidad de dias que desea dejar a la mascota en la guarderia: "))
                if dias >=1:
                    break
                else:
                    print("ERROR! la cantidad de dias debe ser 1 o mayor que 1!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

        print(funciones.arreglo_zeros)

        msvcrt.getch()

            
    elif opc==2:
        pass
    elif opc==3:
        pass
    else:
        while True:
            salida= input("¿Esta seguro que desea salir 'SI','NO'?")
            if salida.upper in("SI","NO"):
                break
            else:
                print("ERROR! DEBE INGRESAR 'SI' O 'NO' ")
