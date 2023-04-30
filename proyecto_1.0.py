import pickle

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#Validaciones de entries y funciones de aviso:

def noDataError():
         
     print("""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║   ■ No se encontraron empleados.                                              ║
    ║     Revise su base de datos de forma externa o consulte a servicio técnico.   ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
      """)
     
def incorrectDataErr():

    print("""
            ╔════════════════════════════════════════════════════════════╗
            ║    ■ El nombre es incorrecto, o el empleado no existe.     ║
            ║      Por favor, chequee los datos y vuelva a intentarlo.   ║
            ╚════════════════════════════════════════════════════════════╝
              """)

def validNum(num):
    while(num.isdigit()==False):
        num=input("""
            ╔════════════════════════════════════════════════════╗
            ║  ■ No es un dato valido.                           ║
            ║    Por favor, ingrese un numero natural entero:    ║
            ╚════════════════════════════════════════════════════╝
              » """)
    return num

def validStr(str):
    while(str.isalpha()==False):
        str=input("""
            ╔════════════════════════════════════════════════════════════════════════════╗
            ║  ■ No es un dato valido.                                                   ║
            ║    Por favor, ingrese sólo palabras, sin números o caracteres especiales:  ║
            ╚════════════════════════════════════════════════════════════════════════════╝
              » """)
    str=str.lower()
    return str

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Main Object: "empleados"
class empleados:

    def __init__(self, nombre, cargo, salario, antiguedad):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.antiguedad=antiguedad
        try:
             with open("EMPLEADOS.pkl", 'rb') as f:
                 EMPLEADOS = pickle.load(f)
        except FileNotFoundError:
            EMPLEADOS = []
        self.id=EMPLEADOS[len(EMPLEADOS)-1].id +1

    def __str__(self):
        return (f"""                          
║\t■      Nombre: {self.nombre}                
║\t■       Cargo: {self.cargo}                 
║\t■     Salario: {self.salario}               
║\t■  Antigüedad: {self.antiguedad}
║                                         
╚════════════════════╦═════════════════════""")

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Función "Crear Empleado":
def crearEmpleado():
        
    nombre=input("""║ 
║
║   ╔═════════════════════════════════╗
╠═══╣ » Nombre completo del empleado: ║
║   ╚═════════════════════════════════╝
║     » """) 
    nombre=validStr(nombre)

    cargo=input("""║
║  ╔════════════════════╗
╠══╣ » Cargo que ocupa: ║
║  ╚════════════════════╝
║     » """)
    cargo=validStr(cargo)
    
    salario=input("""║
║   ╔═════════════╗
╠═══╣ » Salario:  ║
║   ╚═════════════╝
║     » """)
    salario=validNum(salario)
    
    antiguedad=input("""║ 
║   ╔══════════════════════════════╗
╠═══╣ » Antigüedad en la empresa:  ║
║   ╚══════════════════════════════╝
║     » """)
    
    empleado= empleados(nombre,cargo,salario,antiguedad)

    try:
        with open("EMPLEADOS.pkl", 'rb') as f:
            EMPLEADOS = pickle.load(f)
    except FileNotFoundError:
        EMPLEADOS = []
    with open('EMPLEADOS.pkl', 'wb') as f:
        EMPLEADOS.append(empleado)
        pickle.dump(EMPLEADOS, f)

    print("""║
║           ╔══════════════════════════════════════════╗
╚═══════════╣  ■ ¡Empleado registrado exitosamente! «  ║
            ╚══════════════════════════════════════════╝
""")

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Función "Ver Datos de Empleado":
def mostrarDatos():
            
    Nombre= input("""║ 
║          ╔════════════════════════════════════════════════════════════════════╗
╚══════════╣  » Por favor ingrese el nombre del empleado que desea examinar:    ║
           ║      (ingrese 'TODOS' para ver la totalidad de la nomina)          ║
           ╚════════════════════════════════════════════════════════════════════╝
             » """)
    Nombre= validStr(Nombre)
    
    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            lista=pickle.load(f)

        if len(lista)>0:
            if (Nombre=="todos"):
                with open("EMPLEADOS.pkl", "rb") as f:
                    lista=pickle.load(f)
                    for i in (lista):
                        id=i.id
                        #responsiveOptions
                        if len(str(id))==1:
                            print(f"""                ╔════╩═══╗
╔═══════════════╣ ID: {id  }  ╠═════════════════
║               ╚════════╝""",i)
                        elif len(str(id))==2:
                            print(f"""                ╔════╩═══╗
╔═══════════════╣ ID: {id  } ╠═════════════════
║               ╚════════╝""",i)
                        elif len(str(id))==3:
                            print(f"""                ╔════╩════╗
╔═══════════════╣ ID: {id  }  ╠═════════════════
║               ╚═════════╝""",i)
                        elif len(str(id))==4:
                            print(f"""                ╔════╩═════╗
╔═══════════════╣ ID: {id  }   ╠═════════════════
║               ╚══════════╝""",i)
            else:
                repeat=0

            #Nombre repetido
                for i, empleado in enumerate(lista):
                    if (lista[i].nombre==Nombre):
                        repeat+=1
                if repeat>=2:
                    #Busqueda por ID forzada
                    Nombre= input(""" 
    ╔═════════════════════════════════════════════════════════════════════════╗
    ║    » El nombre aparece en múltiples empleados.                          ║   
    ║      Por favor ingrese el número de ID del empleado que desea mostrar:  ║
    ╚═════════════════════════════════════════════════════════════════════════╝
      » """)
                    Nombre= validNum(Nombre)
                    found=0
                    for i, empleado in enumerate(lista):
                        id=empleado.id
                        
                        if (id==int(Nombre)):
                             #responsiveOptions
                            if len(str(id))==1:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }   ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==2:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }  ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==3:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id } ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==4:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

        """)
                            found+=1
                        elif (i==len(lista)-1 and found==0):
                            incorrectDataErr()                 
                       #Nombre único:    
                else:
 
                    for i, empleado in enumerate(lista):
                        id=empleado.id
                        if (empleado.nombre==Nombre):
                            #responsiveOptions
                            if len(str(id))==1:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }   ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==2:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }  ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==3:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id } ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            elif len(str(id))==4:
                                print(f"""                 ╔═══════════╗
╔════════════════╣   ID: { id }╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

            """)
                            break
                        else:
                            if (i==len(lista)-1):
                                incorrectDataErr()     
        else:
            noDataError()
    except FileNotFoundError:
        noDataError()

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Función "Modificar Datos de Empleado":

def modificarDatos():

    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            EMPLEADOS=pickle.load(f)
        
        Nombre= input("""║  
║           ╔═══════════════════════════════════════════════════════════╗
╠═══════════╣  » Por favor ingrese el nombre del empleado a modificar:  ║
║           ╚═══════════════════════════════════════════════════════════╝
║            » """)
        Nombre=validStr(Nombre)
        dato= input("""║ 
║           ╔═════════════════════════════════════════════╗
╠═══════════╣  » Por favor ingrese el dato a modificar:   ║
║           ╚═════════════════════════════════════════════╝
║            » """)
        dato=validStr(dato)
        nuevoValor= input(f"""║  
║           ╔════════════════════════════════════════════════════════
╠═══════════╣  » Por favor ingrese el nuevo valor de {dato}.            
║           ╚════════════════════════════════════════════════════════
║            » """)
        if dato=="salario":
            nuevoValor=validNum(nuevoValor)
        elif dato=="nombre" or dato=="cargo":
            nuevoValor=validStr(nuevoValor)
        
        for i, empleado in enumerate(EMPLEADOS):
            if (EMPLEADOS[i].nombre==Nombre):
                with open("EMPLEADOS.pkl", "wb") as f:
                    setattr(EMPLEADOS[i], dato, nuevoValor)
                    print(f"""║ 
║           ╔═════════════════════════════════════════════════════════════════════
╚═══════════╣  » Para el empleado/a: {Nombre} el {dato} ha sido modificado a:                                
            ║     {getattr(EMPLEADOS[i], dato)}.                                                              
            ╚═════════════════════════════════════════════════════════════════════
                """)
                    pickle.dump(EMPLEADOS, f)
                break
            else:
                if (i==len(EMPLEADOS)-1):
                    incorrectDataErr()
    except FileNotFoundError:
        noDataError()

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Función "Eliminar Empleado":
def eliminarEmpleado():

    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            EMPLEADOS=pickle.load(f)

        if len(EMPLEADOS)>0:
            
            Nombre= input("""║ 
║   ╔══════════════════════════════════════════════════════════════════════════════════════════════╗
╠═══╣  » Por favor ingrese el nombre o número de ID del empleado que desea eliminar del registro:  ║
║   ╚══════════════════════════════════════════════════════════════════════════════════════════════╝
║     » """)
            
            #Busqueda por nombre:
            if Nombre.isalpha():
                Nombre= validStr(Nombre)
                repeat=0

            #Nombre repetido
                for i, empleado in enumerate(EMPLEADOS):
                    if (EMPLEADOS[i].nombre==Nombre):
                        repeat+=1
                if repeat>=2:
                    #Busqueda por ID forzada
                    Nombre= input("""║ 
║   ╔═══════════════════════════════════════════════════════════════════════════════════════╗
╠═══╣    » El nombre aparece en múltiples empleados.                                      ║   
║   ║      Por favor ingrese el número de ID del empleado que desea eliminar del registro:  ║
║   ╚═══════════════════════════════════════════════════════════════════════════════════════╝
║     » """)
                    Nombre= validNum(Nombre)

                    with open("EMPLEADOS.pkl", "wb") as f:
                        for i, empleado in enumerate(EMPLEADOS):
                            if (EMPLEADOS[i].id==int(Nombre)):
                                del EMPLEADOS[i]
                                print(f"""║
║   ╔═════════════════════════════════════════════════════════════════════════════
╚═══╣  ■ El empleado con número de ID: {Nombre} ha sido eliminado del registro.  
    ╚═════════════════════════════════════════════════════════════════════════════
            """)
                                pickle.dump(EMPLEADOS, f)
                                break
                            
                            if (i==len(EMPLEADOS)-1):
                                incorrectDataErr()                 
            #Nombre único
                else:
                    for i, empleado in enumerate(EMPLEADOS):
                        if (EMPLEADOS[i].nombre==Nombre):
                            del EMPLEADOS[i]
                            print(f"""║
║   ╔════════════════════════════════════════════════════════════════════
╚═══╣  ■ El empleado: {Nombre} ha sido eliminado del registro.  
    ╚════════════════════════════════════════════════════════════════════
        """)
                            pickle.dump(EMPLEADOS, f)
                            break
                        
                        if (i==len(EMPLEADOS)-1):
                            incorrectDataErr()
        
            #Busqueda por ID:
            elif Nombre.isalnum():
                Nombre= validNum(Nombre)

                # Abrir el archivo .pkl y cargar la estructura de datos
                with open("EMPLEADOS.pkl", "rb") as f:
                    EMPLEADOS = pickle.load(f)

                if (not EMPLEADOS):
                    incorrectDataErr()

                # Buscar el registro por ID
                for i, empleado in enumerate(EMPLEADOS):
                    if (empleado.id == int(Nombre)):
                        # Buscar el registro por ID
                        EMPLEADOS.pop(i)
                        print(f"""║
║   ╔═════════════════════════════════════════════════════════════════════════════
╚═══╣  ■ El empleado con número de ID: {Nombre} ha sido eliminado del registro.  
╚═════════════════════════════════════════════════════════════════════════════
    """)
                        break

                # Guardar los cambios en el archivo .pkl
                with open('EMPLEADOS.pkl', 'wb') as f:
                    pickle.dump(EMPLEADOS, f)    
                        
            else:
                print("""
            ╔════════════════════════════════════════════════════════╗
            ║  ■ No es un dato valido.                               ║
            ║    Por favor, ingrese sólo palabras o sólo números.    ║
            ╚════════════════════════════════════════════════════════╝ 
            """)
                # eliminarEmpleado()
        else:
            noDataError()

    except FileNotFoundError:
       noDataError()

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Función Menú Principal:
def opciones():
    option=input("""
                 ╔═══════════════════════════════════════════════════════════════╗
╔════════════════╣ Por favor, ingrese el número de la acción que desea realizar: ╠═══════════════╗
║                ╚═══════════════════════════════════════════════════════════════╝               ║
║ \t\t   ■      1»  Agregar un empleado al registro.                                   ║
║ \t\t   ■      2»  Mostrar los datos de un empleado.                                  ║
║ \t\t   ■      3»  Modificar los datos de un empleado.                                ║    
║ \t\t   ■      4»  Eliminar un empleado del registro.                                 ║
║ \t\t   ■      5»  Cerrar el programa.                                                ║
║                                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════════════════════╝
║     » """)

    if (option=="1"):
        crearEmpleado()
    elif (option=="2"):
        mostrarDatos()
    elif (option=="3"):
        modificarDatos()
    elif (option=="4"):
        eliminarEmpleado()
    elif (option=="5"):
        keepRunning()
    else:
        print("""
    \t\t        ╔═══════════════════════════════════════════╗
    \t\t        ║  ■ La opción seleccionada no es válida.   ║                                             
    \t\t        ╚═══════════════════════════════════════════╝
            """)
        main()

# Salir del programa:
def keepRunning():

    choice=""
    choice=input("""
    \t\t        ╔═════════════════════════════════════════════════╗
    \t\t        ║ » ¿Desea realizar alguna otra operación? (S/N)  ║                                             
    \t\t        ╚═════════════════════════════════════════════════╝
     \t» """)
    choice=validStr(choice)

    if (choice!="s" and choice!="n"):
        print("""
    \t        ╔══════════════════════════════════════════════════════╗
    \t        ║ » No es una opción válida. Por favor ingrese: (S/N)  ║                                             
    \t        ╚══════════════════════════════════════════════════════╝
     \t» """)
        keepRunning()
    return choice

# Definición de la Ejecución principal del programa
def main():

    while True:

        opciones()

        keepRunning()

        if (keepRunning()=="n"):
            break

# Ejecución de la Pantalla del Usuario:
if __name__=="__main__":
    main()