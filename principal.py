
from funciones import *


while True:
    print("Bienvenido al menu de empleados")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    while True:
        try:
            opc=int(input("Elija una opcion: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("ERROR! elija opción valida")
        except:
            print("ERROR! ingrese numero entero")
    os.system("cls")



    if opc==1:
        opcion_1()
    elif opc==2:
        pass
    elif opc==3:
        opcion_3()
    elif opc==4:
        opcion_4()
    else:
        salida()
        break
