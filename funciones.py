import random,time,os,csv,msvcrt
informacion=[]
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
aleatorio=random.choice(trabajadores)
num_aleatorio=random.randint(300000,2500000)
sueldos=[]


def opcion_1 ():
    print("has elegido Asignar sueldos aleatorios")
    for t in range(len(trabajadores)):
        sueldo=num_aleatorio
        sueldos.append(sueldo)
        Descuento_salud=int(7*sueldo/100)
        Descuento_AFP=int(12*sueldo/100)
        Sueldoliquido1=sueldo-Descuento_AFP
        sueldoliquido2=Sueldoliquido1-Descuento_salud
        trabajador ={"Nombre": trabajadores[t],
                    "Sueldo": sueldo,
                    "Descuento salud": Descuento_salud,
                    "Descuento AFP":Descuento_AFP,
                     "Sueldo líquido":sueldoliquido2 }
        informacion.append(trabajador)
    print("cargando.")
    time.sleep(1)
    os.system("cls")
    print("cargando..")
    time.sleep(1)
    os.system("cls")
    print("cargando...")
    time.sleep(1)
    os.system("cls")
    print("cargando.")
    time.sleep(1)
    os.system("cls")
    print("cargando..")
    time.sleep(1)
    os.system("cls")
    print("cargando...")
    time.sleep(1)
    os.system("cls")
    print("cargando.")
    time.sleep(1)
    os.system("cls")
    print("cargando..")
    time.sleep(1)
    os.system("cls")
    print("cargando...")
    time.sleep(1)
    os.system("cls")
    print("completado")
    time.sleep(3)
    os.system("cls")
        

    



def salida ():
    print("Finalizando programa")
    print("Desarrollado por Diego Alarcón")
    print("RUT 21.801.133-0")
     










def opcion_4():
    print("has elegido Reporte de sueldos")
    for o in range(len(informacion)):
        print("empleado numero ",o+1)
        print(informacion[o])
        

    with open("reportedesueldo.csv","x",newline="") as archivo:
        escritor=csv.DictWriter(archivo,["Nombre","Sueldo","Descuento salud","Descuento AFP","Sueldo líquido"])
        escritor.writeheader()
        
    print("Se ha guardado con exito!!")



def opcion_3():
    print("has elegido Ver estadísticas")
    print("el promedio de los sueldo es:")
    print(int(sum(sueldos)/10))
    m_g=(sueldos[0]*sueldos[1]*sueldos[2]*sueldos[3]*sueldos[4]*sueldos[5]*sueldos[6]*sueldos[7]*sueldos[8]*sueldos[9])
    mg=int(m_g)**0.1

    print("La media geométrica es:")
    print(mg)


    time.sleep(3)











        
