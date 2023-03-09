from clearwindow import clearWindow
from colorama import init, Fore, Back, Style
import unidecode
init()
clearWindow()

#entrada
archivo = "instrocpecion.txt"

#salida
diccionario = {} 
versosTextoPlano = ""

def reader(archivo):
    """
    Recorre la informacion de un archivo linea por linea
    almacena en formato list
    Se espera la informacion este correctamente formateada
    
    Returns:
        return: type(tuple)
        versosLista: type(list) versos sin agrupar // sin formato
    """    
    versosLista = [] 
    versosFormateadosTemp = []
    
    with open(f'letras/{archivo}', 'r',
              encoding="utf-8") as fichero:
        temp = fichero.readlines()
        for linea in temp:
            linea = linea.lower()
            # Elimina las tildes
            linea = unidecode.unidecode(linea)
            versosLista.append(linea.split())
    
    num_min = 0
    num_max = 4
    while num_max <= len(versosLista):
        versosFormateadosTemp.append(versosLista[num_min:num_max])
        num_min = num_max + 1
        num_max += 5
    
    return versosFormateadosTemp
    
versosFormateados = reader(archivo)

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

def rimador(num):
    """
    Esta funcion se encarga de dar el ultimo formado y de rimar(colorear) los veros

    Args:
        num (INT): Indica el numero del parrafo sobre el cual trabaja la funcion

    Returns:
        versosTextoPlano: Salida final, parrafos estructurados y rimados
    """
    global versosTextoPlano
    estrofa = ""    

    """
    # Imprime el diccionario
    for key, value in diccionario.items():
        print(f"{key} -> {value}")
    """
    # ultima palabra(-1) del verso 1(0)
    # selectorVerso / selecciona el verso completo
    # selector / limpia el dato y lo almacena
    selectorVerso1 = versosFormateados[num][0]
    selector1 = versosFormateados[num][0][-1].replace('"','')
    
    selectorVerso2 = versosFormateados[num][1]
    selector2 = versosFormateados[num][1][-1].replace('"','')
    
    selectorVerso3 = versosFormateados[num][2]
    selector3 = versosFormateados[num][2][-1].replace('"','')
    
    selectorVerso4 = versosFormateados[num][3]
    selector4 = versosFormateados[num][3][-1].replace('"','')
    
    #Buscar el selector dentro del diccionario
    vocales1 = diccionario.get(selector1)
    vocales2 = diccionario.get(selector2)
    vocales3 = diccionario.get(selector3)
    vocales4 = diccionario.get(selector4)
    
    def ejemploFuncion(parametro):
        """
        Recorre un verso(lista) y lo convierte a str con las modificaciones de color

        Args:
            parametro (list): indica el verso exacto el cual sera recorrido

        Returns:
            versosTemp (str): verso individual para posterior union en una sola estrofa 4x4
        """
        global versosTextoPlano
        contadorVerso=0
        versosTemp = ""
        
        for i in parametro:
            contadorVerso+=1
            i = i.replace('"','')
            if contadorVerso != len(parametro):
                versosTemp += i+" "
            elif contadorVerso == len(parametro):
                versosTemp += f"{i}\n"
                contadorVerso=0
        return versosTemp
        
    verso1=ejemploFuncion(selectorVerso1)
    verso2=ejemploFuncion(selectorVerso2)
    verso3=ejemploFuncion(selectorVerso3)
    verso4=ejemploFuncion(selectorVerso4)
    
    estrofa += verso1+verso2+verso3+verso4

    # Logica de rimas
    # Verso 1 - Verso 2
    # si tiene 3 vocales o mas y todas riman
    if len(vocales1) >= 3 and len(vocales2) >= 3 and vocales1[-1] == vocales2[-1] and vocales1[-2] == vocales2[-2] and vocales1[-3] == vocales2[-3]:
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector2}{Style.RESET_ALL}")
    # si tiene 2 vocales o mas y todas riman
    elif len(vocales1) >= 2 and len(vocales2) >= 2 and vocales1[-1] == vocales2[-1] and vocales1[-2] == vocales2[-2]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector2}{Style.RESET_ALL}")
    # Rima solo 1 vocal
    elif len(vocales1) >= 1 and len(vocales2) >= 1 and vocales1[-1] == vocales2[-1]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Fore.WHITE}{selector2}{Style.RESET_ALL}")
    else: # Si no riman Comprueba otro verso
        if len(vocales2) >= 3 and len(vocales4) >= 3 and vocales2[-1] == vocales4[-1] and vocales2[-2] == vocales4[-2] and vocales2[-3] == vocales4[-3]:
            estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Style.BRIGHT + Fore.GREEN}{selector2}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.BRIGHT + Fore.GREEN}{selector4}{Style.RESET_ALL}")
            # si tiene 2 vocales o mas y todas riman
        elif len(vocales2) >= 2 and len(vocales4) >= 2 and vocales2[-1] == vocales4[-1] and vocales2[-2] == vocales4[-2]: 
            estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Style.NORMAL + Fore.GREEN}{selector2}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.NORMAL + Fore.GREEN}{selector4}{Style.RESET_ALL}")
        # Rima solo 1 vocal
        elif len(vocales2) >= 1 and len(vocales4) >= 1 and vocales2[-1] == vocales4[-1]: 
            estrofa = estrofa.replace(f"{selector2}",f"{Back.RED + Fore.GREEN}{selector2}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Fore.GREEN}{selector4}{Style.RESET_ALL}")
    
    # Verso 1 - Verso 3
    # si tiene 3 vocales o mas y todas riman
    if len(vocales1) >= 3 and len(vocales3) >= 3 and vocales1[-1] == vocales3[-1] and vocales1[-2] == vocales3[-2] and vocales1[-3] == vocales3[-3]:
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector3}{Style.RESET_ALL}")
    # si tiene 2 vocales o mas y todas riman
    elif len(vocales1) >= 2 and len(vocales3) >= 2 and vocales1[-1] == vocales3[-1] and vocales1[-2] == vocales3[-2]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector3}{Style.RESET_ALL}")
    # Rima solo 1 vocal
    elif len(vocales1) >= 1 and len(vocales3) >= 1 and vocales1[-1] == vocales3[-1]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.DIM + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.DIM + Fore.WHITE}{selector3}{Style.RESET_ALL}")
    else: # Si no riman comprueba otro verso
        if len(vocales3) >= 3 and len(vocales4) >= 3 and vocales3[-1] == vocales4[-1] and vocales3[-2] == vocales4[-2] and vocales3[-3] == vocales4[-3]:
            estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.BRIGHT + Fore.GREEN}{selector3}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.BRIGHT + Fore.GREEN}{selector4}{Style.RESET_ALL}")
        # si tiene 2 vocales o mas y todas riman
        elif len(vocales3) >= 2 and len(vocales4) >= 2 and vocales3[-1] == vocales4[-1] and vocales3[-2] == vocales4[-2]: 
            estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.NORMAL + Fore.GREEN}{selector3}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.NORMAL + Fore.GREEN}{selector4}{Style.RESET_ALL}")
        # Rima solo 1 vocal
        elif len(vocales3) >= 1 and len(vocales4) >= 1 and vocales3[-1] == vocales4[-1]: 
            estrofa = estrofa.replace(f"{selector3}",f"{Back.RED + Style.DIM + Fore.GREEN}{selector3}{Style.RESET_ALL}")
            estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.DIM + Fore.GREEN}{selector4}{Style.RESET_ALL}")
        
    # Verso 1 - Verso 4
    # si tiene 3 vocales o mas y todas riman
    if len(vocales1) >= 3 and len(vocales4) >= 3 and vocales1[-1] == vocales4[-1] and vocales1[-2] == vocales4[-2] and vocales1[-3] == vocales4[-3]:
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.BRIGHT + Fore.WHITE}{selector4}{Style.RESET_ALL}")
    # si tiene 2 vocales o mas y todas riman
    elif len(vocales1) >= 2 and len(vocales4) >= 2 and vocales1[-1] == vocales4[-1] and vocales1[-2] == vocales4[-2]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.NORMAL + Fore.WHITE}{selector4}{Style.RESET_ALL}")
    # Rima solo 1 vocal
    elif len(vocales1) >= 1 and len(vocales4) >= 1 and vocales1[-1] == vocales4[-1]: 
        estrofa = estrofa.replace(f"{selector1}",f"{Back.RED + Style.DIM + Fore.WHITE}{selector1}{Style.RESET_ALL}")
        estrofa = estrofa.replace(f"{selector4}",f"{Back.RED + Style.DIM + Fore.WHITE}{selector4}{Style.RESET_ALL}")
    
                
   

    versosTextoPlano += estrofa+"\n"

for i in range(len(versosFormateados)):
    diccionarioCreate(i)
    rimador(i)
    diccionario.clear()
""" 

diccionarioCreate(7)
rimador(7)   

"""
print(versosTextoPlano)