from clearwindow import clearWindow
from colorama import init, Fore, Back, Style
init()
clearWindow()

def reader():
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
    with open('letras/taquigrafia.txt', 'r',
              encoding="utf-8") as fichero:
        temp = fichero.readlines()
        for linea in temp:
            linea = linea.lower()
            versosTexto += linea
            versosLista.append(linea.split())
            
        return versosLista, versosTexto

versosSinFormato, versosTextoPlano  = reader()
versosFormateados = []
diccionario = {}

def listaVersosAppendIterador():
    """
    Bucle: Agrega "versosSinformato" -> "versosFormateados"
    Formato: Para obtener una estructura de informacion 4(versos)
    """
    num_min = 0
    num_max = 4
    while num_max <= len(versosSinFormato):
        versosFormateados.append(versosSinFormato[num_min:num_max])
        num_min = num_max + 1
        num_max += 5
listaVersosAppendIterador()

def imprimirVerso(verso=None,enVerso=None,palabra=None):
    """
        Capa de abstaccion para buscar detro de una lista con sub-listas
    Args:
        verso (INT): index 1: Agrupacion de 4 versos(Estructura 4x4 RAP) Defaults to None.
        enVerso (INT): index 2: Lineas detro de la estructura. Defaults to None.
        palabra (INT): index 3: Palabra individual en cada linea. Defaults to None.

    Returns:
        type(list): resultado de busqueda abstracta
    """
    if verso != None and enVerso != None and palabra != None:
        return versosFormateados[verso][enVerso][palabra]
    elif verso != None and enVerso != None and palabra == None:
        return versosFormateados[verso][enVerso]
    elif verso != None and enVerso == None and palabra == None:
        return versosFormateados[verso]
    else:
        return "Todos los parametros vacios en 'imprimirVerso'!!\nverso=None,enVerso=None,palabra=None"

def diccionarioCreate(num):

    temp=imprimirVerso(num)
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
            
    #print(listVocalTemp)

def iterador(num):
    global versosTextoPlano
    #print(f"\t\t:..Texto plano..:\n{txt}")


    """
    for key, value in diccionario.items():
        print(f"{key} -> {value}")
    """
    #ultima palabra(-1) del verso 1(0)
    selector1 = imprimirVerso(num,0,-1).replace('"','')
    vocales1 = diccionario.get(selector1)
    selector2 = imprimirVerso(num,1,-1).replace('"','')
    vocales2 = diccionario.get(selector2)
    selector3 = imprimirVerso(num,2,-1).replace('"','')
    vocales3 = diccionario.get(selector3)
    selector4 = imprimirVerso(num,3,-1).replace('"','')
    vocales4 = diccionario.get(selector4)

    #Buscar el selector dentro del diccionario
    # Comprueba si sexiste
    if diccionario.get(selector1) != False:
        """
        print(f"\nSelector 1: {selector1}")
        print(vocales1)
        print(f"\nSelector 2: {selector2}")
        print(vocales2)
        print(f"\nSelector 3: {selector3}")
        print(vocales3)
        print(f"\nSelector 4: {selector4}")
        print(vocales4)
        """
        
        if vocales1[-1] == vocales2[-1]:
            versosTextoPlano = versosTextoPlano.replace(f"{selector1}",f"{Fore.RED}{selector1}{Style.RESET_ALL}")
            versosTextoPlano = versosTextoPlano.replace(f"{selector2}",f"{Fore.RED}{selector2}{Style.RESET_ALL}")
            if vocales1[-1] == vocales3[-1]:
                versosTextoPlano = versosTextoPlano.replace(f"{selector3}",f"{Fore.RED}{selector3}{Style.RESET_ALL}")
            elif vocales1[-1] == vocales4[-1]:
                versosTextoPlano = versosTextoPlano.replace(f"{selector4}",f"{Fore.RED}{selector4}{Style.RESET_ALL}")
        
    else:
        print(f"{selector1}: no existe en el diccionario")

for i in range(14):
    diccionarioCreate(i)
    iterador(i)
print(f"\t\t:..Texto Modificado..:\n{versosTextoPlano}")
