# El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asignaciones de vehículos y Stromtroopers 
# a las distintas misiones que parten desde la estrella de la muerte, 
# para facilitar esta tarea nos encomienda desarrollar las funciones necesarias 
# para gestionar esto mediante prioridades de la siguiente manera:
#           a). de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
#           b). si la misión fue pedida por Palpatine o Darth Vader estas tendrán alta prioridad, sino su prioridad será baja;
#           c). si la misión es de prioridad alta los recursos se asignarán manualmente independiente- mente de su tipo;
#           d). si la misión es de baja prioridad se asignarán los recursos de la siguiente manera depen- diendo de su tipo:
#               1. exploración: 15 Scout Troopers y 2 speeder bike,
#               2. contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
#               3. ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),
#           e). realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, per- mitiendo agregar nuevos pedidos de misiones durante la atención;
#           f). indicar la cantidad total de recursos asignados a las misiones.

import random 
def asignar_recursos (misiones):
    """ Las misiones 
    una misión es una lista ["PLANETA", "TIPO",[SOLDADOS, NAVES], "PRIORIDAD"]
    """
    for mision in misiones:
        if mision[3] == "Palpatine" or mision[3] == "Darth Vader":  #alta
            if mision[1] == "exploracion":
                mision[2] = [15,2]
            elif mision[1] == "contencion":
                mision[2] = [30,3]
            elif mision[1] == "ataque":
                mision[2] = [50,7]
        else: #baja
            if mision[1] == "exploracion":
                mision[2] = [15,2]
            elif mision[1] == "contencion":
                mision[2] = [30,3]
            elif mision[1] == "ataque":
                mision[2] = [50,7]
    return misiones

def mostrar_recursos(misiones):
    for mision in misiones:        
        print("La misión de tipo", mision[1], "destinada a", mision[0], "y solicitada por", mision[3])
        

def agregar_mision(misiones):
    mision = []
    mision.append(input('Ingrese el planeta destino -> '))  
    mision.append(input('Ingrese el tipo de mision -> '))
    mision.append([0,0])    
    mision.append(input('Ingrese el general que la solicitó -> '))
    misiones.append(mision)
    return misiones

def main():
    misiones = []
    misiones.append(["Tattoine","exploracion",[0,0],"Palpatine"])
    misiones.append(["Hoth","contencion",[0,0],"Palpatine"])
    misiones.append(["Coruscant","ataque",[0,0],"Darth Vader"])
    misiones.append(["Dagobah","exploracion",[0,0],"Peter"])
    misiones.append(["Kashyyyk","contencion",[0,0],"Juan"])
    misiones.append(["Mustafar","ataque",[0,0],"Lucia"])
    misiones = asignar_recursos(misiones)
    mostrar_recursos(misiones)
    while input('¿Desea agregar una nueva mision? (s/n) -> ') == "s":
        misiones = agregar_mision(misiones)
        misiones = asignar_recursos(misiones)
        mostrar_recursos(misiones)

main()





