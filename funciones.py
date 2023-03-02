from clearwindow import clearWindow
from colorama import init, Fore, Back, Style
init()
clearWindow()

#entrada
archivo = "Bastión de lágrimas.txt"

#salida
diccionario = {}

def reader(archivo):
    """
    Recorre la informacion de un archivo linea por linea
    almacena en formato list
    Se espera la informacion este correctamente formateada
    
    Returns:
        return: type(tuple)
        versosLista: type(list) versos sin agrupar // sin formato
        versosTextoPlano: type(str) versos en texto plato para modificacion final
    """    
    versosLista = [] 
    versosTexto = ""
    versosFormateadosTemp = []
    
    with open(f'letras/{archivo}', 'r',
              encoding="utf-8") as fichero:
        temp = fichero.readlines()
        for linea in temp:
            linea = linea.lower()
            versosTexto += linea
            versosLista.append(linea.split())
    
    num_min = 0
    num_max = 4
    while num_max <= len(versosLista):
        versosFormateadosTemp.append(versosLista[num_min:num_max])
        num_min = num_max + 1
        num_max += 5
    
    return versosFormateadosTemp, versosTexto
    
#
versosFormateados, versosTextoPlano  = reader(archivo)

def diccionarioCreate(num):
    """
    recorre la estructura 4x4 
    se detiene en la ultima palabra de cada verso
    la recorre y la almacera en diccionario
    {"palabra":["vocales"]}
    {"hola":["o","a"]}
    Args:
        num (INT): numero que recorre los versos 4x4
    """
    temp=versosFormateados[num]
    for ultimaPalabra in  temp:
        #ultima palabra de cada verso
        ultimaPalabra = ultimaPalabra[-1].replace('"','')
        #print(ultimaPalabra)
        listVocalTemp = []
        for letra in ultimaPalabra:
            if "a" == letra or "á" == letra:
                listVocalTemp += letra
            elif "e" == letra or "é" == letra:
                listVocalTemp += letra
            elif "i" == letra or "í" == letra:
                listVocalTemp += letra
            elif "o" == letra or "ó" == letra:
                listVocalTemp += letra
            elif "u" == letra or "ú" == letra:
                listVocalTemp += letra
            diccionario[ultimaPalabra] = listVocalTemp

def iterador(num):
    global versosTextoPlano
    """
    for key, value in diccionario.items():
        print(f"{key} -> {value}")
    """
    #ultima palabra(-1) del verso 1(0)
    #selector / limpia el dato de alguna impureza y lo almacena
    selector1 = versosFormateados[num][0][-1].replace('"','')
    selector2 = versosFormateados[num][1][-1].replace('"','')
    selector3 = versosFormateados[num][2][-1].replace('"','')
    selector4 = versosFormateados[num][3][-1].replace('"','')
    
    #Buscar el selector dentro del diccionario
    vocales1 = diccionario.get(selector1)
    vocales2 = diccionario.get(selector2)
    vocales3 = diccionario.get(selector3)
    vocales4 = diccionario.get(selector4)

    # Comprueba si sexiste
    if vocales1[-1] == vocales2[-1]:
        versosTextoPlano = versosTextoPlano.replace(f"{selector1}",f"{Fore.RED}{selector1}{Style.RESET_ALL}")
        versosTextoPlano = versosTextoPlano.replace(f"{selector2}",f"{Fore.RED}{selector2}{Style.RESET_ALL}")
    if vocales1[-1] == vocales3[-1]:
        versosTextoPlano = versosTextoPlano.replace(f"{selector3}",f"{Fore.RED}{selector3}{Style.RESET_ALL}")
    if vocales1[-1] == vocales4[-1]:
        versosTextoPlano = versosTextoPlano.replace(f"{selector4}",f"{Fore.RED}{selector4}{Style.RESET_ALL}")
              
for i in range(len(versosFormateados)):
    diccionarioCreate(i)
    iterador(i)

#print(f"\t\t:..Texto Modificado..:\n{versosTextoPlano}")