# BASE DE DATOS: 
import pickle

EMPLEADOS=[]

if (len(EMPLEADOS)==0):
    with open("EMPLEADOS.pkl", "wb") as f:
        pickle.dump(EMPLEADOS, f)
else:
    with open("EMPLEADOS.pkl", "rb") as f:
        pickle.load(f)
   
#######################################

###############################################################################################################################################

#Main Object: "empleados"

class empleados:
    def __init__(self, nombre, cargo, salario, antiguedad):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.antiguedad=antiguedad

###############################################################################################################################################

#Función "Crear Empleado":

def crearEmpleado():

    nombre=input("Nombre completo del empleado:\n")

    #Validación de pre-existencia de empleado:
    for i, empleado in enumerate(EMPLEADOS):
            if (EMPLEADOS[i].nombre==nombre):
                 print(f"El empleado {nombre} ya existe en el registro.\n")
                 main() ############Poner algo que cierre el programa al terminar el main() aca BUG ##################
    ##########################################

    cargo=input("Cargo que ocupa:\n")
    salario=input("Salario:\n")
    antiguedad=input("Antigüedad en la empresa:\n")

    empleado= empleados(nombre,cargo,salario,antiguedad)
    EMPLEADOS.append(empleado)

#Función "Ver Datos de Empleado":

def mostrarDatos():
        Nombre= input("""Por favor ingrese el nombre del empleado que desea examinar: 
        (ingrese 'TODOS' para ver la totalidad de la nomina)
        """)
        for i, empleado in enumerate(EMPLEADOS):
            if (EMPLEADOS[i].nombre==Nombre):
                print("Nombre: ", EMPLEADOS[i].nombre,"/n Cargo:", EMPLEADOS[i].cargo, "/n Salario: ", EMPLEADOS[i].salario, "/n Antigüedad: ", EMPLEADOS[i].antiguedad, ".\n")
            elif (Nombre=="TODOS"):
                print("Nombre: ", empleado.nombre,"/n Cargo:", empleado.cargo, "/n Salario: ", empleado.salario, "/n Antigüedad: ", empleado.antiguedad, ".\n")
            else:
                if (i==len(EMPLEADOS)-1):
                    print("El nombre es incorrecto, o el empleado no existe. Por favor chequee los datos y vuelva a intentarlo. \n")
                    return
            

#Función "Modificar Datos de Empleado":

def modificarDatos():

    Nombre= input("Por favor ingrese el nombre del empleado a modificar: \n ")
    dato= input("Por favor ingrese el dato a modificar: \n ")
    nuevoValor= input(f"Por favor ingrese el nuevo valor de {dato}. \n")

    for i, empleado in enumerate(EMPLEADOS):
        if (EMPLEADOS[i].nombre==Nombre):
            setattr(EMPLEADOS[i], dato, nuevoValor)
            print(f"Para el empleado/a:{Nombre} el", dato,f"ha sido modificado a: {getattr(EMPLEADOS[i], dato)}. \n")
            break
        else:
            if (i==len(EMPLEADOS)-1):
                print("El nombre es incorrecto, o el empleado no existe. Por favor chequee los datos y vuelva a intentarlo. \n")
                return
    

#Función "Eliminar Empleado":

def eliminarEmpleado():

    Nombre= input("Por favor ingrese el nombre del empleado que desea eliminar del registro: \n")

    for i, empleado in enumerate(EMPLEADOS):
        if (EMPLEADOS[i].nombre==Nombre):
         del EMPLEADOS[i]
         print(f"El empleado: {Nombre} ha sido eliminado del registro. \n")
         break
        else:
            if (i==len(EMPLEADOS)-1):
                print("El nombre es incorrecto, o el empleado no existe. Por favor chequee los datos y vuelva a intentarlo. \n")
                return

#Función Menú Principal:

def opciones():
    option=input("""Por favor, ingrese el número de la acción que desea realizar:
    1. Agregar un empleado al registro.
    2. Mostrar los datos de un empleado.
    3. Modificar los datos de un empleado.
    4. Eliminar un empleado del registro.
    5. Cerrar el programa.
    
    """)

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
        print("La opción seleccionada no es válida.\n")
        main()

#Salir del programa:

def keepRunning():

    choice=""
    choice=input("¿Desea realizar alguna otra operación? (S/N) \n")
    if (choice!="S" and choice!="N"):
        print("No es una opción válida. Por favor ingrese: (S/N) \n")
        keepRunning()
    return choice

###############################################################################################################################################

#Definición de la Ejecución principal del programa

def main():

    while True:

        opciones()

        keepRunning()

        if (keepRunning()=="N"):
            break

    with open("EMPLEADOS.pkl", "wb") as f:
        pickle.dump(EMPLEADOS, f)

#Ejecución de la Pantalla del Usuario:
main()