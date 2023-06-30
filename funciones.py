import numpy

arreglo_zeros=numpy.zeros((5,5))

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_cant_dias():
    while True:
        try:
            dias = int(input("Ingrese cantidad de dias que desea dejar a la mascota en la guarderia: "))
            if dias >=1:
                return dias
            else:
                print("ERROR! la cantidad de dias debe ser 1 o mayor que 1!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_nom_mascota():
    while True:
        nom_mascota = input("Ingrese nombre mascota: ")
        if len(nom_mascota.strip()) >= 3 and nom_mascota.isalpha():
            return nom_mascota
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

def validar_salida():
    while True:
        salida_opc= input("¿Esta seguro que desea salir 'SI','NO'")
        if salida_opc.upper in ("SI","NO"):
            return salida_opc
        else:
            print("ERROR! DEBE INGRESAR 'SI' O 'NO' ")
