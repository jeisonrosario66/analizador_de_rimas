from colorama import init, Fore, Back, Style
init()

def logica(estrofa, vocales1, vocales2, vocales3, vocales4, selector1, selector2, selector3, selector4):

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
         
    versos = ""
    versos += estrofa+"\n"
    return versos
        
def logica2(dicc, versosFormateados, num):
    diccionarioCreate(dicc, versosFormateados, num)
    selectVerso1 = versosFormateados[num][0]
    selectVerso2 = versosFormateados[num][1]
    selectVerso3 = versosFormateados[num][2]
    selectVerso4 = versosFormateados[num][3]
    
    
    
    print(f"{selectVerso1} Len: {len(selectVerso1)}")
    for pal in range(len(selectVerso1)):
        #variable = versosFormateados[num][0][pal].replace('"',''),f"--> index: [{pal}]"
        palabra = versosFormateados[num][0][pal].replace('"','')
        print(palabra,dicc.get(palabra))     
    print("---------------------------------------------------------------------------------\n")   
    
    print(f"{selectVerso2} Len: {len(selectVerso2)}")
    for pal in range(len(selectVerso2)):
        #variable = versosFormateados[num][0][pal].replace('"',''),f"--> index: [{pal}]"
        palabra = versosFormateados[num][1][pal].replace('"','')
        print(palabra,dicc.get(palabra))     
    print("---------------------------------------------------------------------------------\n")   
    
    print(f"{selectVerso3} Len: {len(selectVerso3)}")
    for pal in range(len(selectVerso3)):
        #variable = versosFormateados[num][0][pal].replace('"',''),f"--> index: [{pal}]"
        palabra = versosFormateados[num][2][pal].replace('"','')
        print(palabra,dicc.get(palabra))     
    print("---------------------------------------------------------------------------------\n")   
    
    print(f"{selectVerso4} Len: {len(selectVerso4)}")
    for pal in range(len(selectVerso4)):
        #variable = versosFormateados[num][0][pal].replace('"',''),f"--> index: [{pal}]"
        palabra = versosFormateados[num][3][pal].replace('"','')
        print(palabra,dicc.get(palabra))     
    print("---------------------------------------------------------------------------------\n")   
        
    selectVerso2 = versosFormateados[num][1]
    selectpalabra2 = versosFormateados[num][1][-1].replace('"','')
        
    selectVerso3 = versosFormateados[num][2]
    selectpalabra3 = versosFormateados[num][2][-1].replace('"','')
        
    selectVerso4 = versosFormateados[num][3]
    selectpalabra4 = versosFormateados[num][3][-1].replace('"','')
    
def diccionarioCreate(dicc, versosFormateados, num):
        """
        - recorre la estructura 4x4, parrafo por parrafo
        - se detiene en la ultima palabra de cada verso
        - la recorre y la almacera en diccionario
        - {"palabra":["vocales"]}
        - {"hola":["o","a"]}
        Args:
            num (INT): numero que recorre los versos 4x4, dicho argumento debe ser iterado segun la cantidad de versos
        """
        def iterador(selectVerso):
            for palIndex in range(len(selectVerso)):
                temp=versosFormateados[num]
                for palabra in  temp:
                    #ultima palabra de cada verso
                    palabra = palabra[palIndex].replace('"','')
                    #print(ultimaPalabra)
                    listVocalTemp = []
                    for letra in palabra:
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
                        
                        if palabra in dicc:
                            pass
                        else:
                            dicc[palabra] = listVocalTemp
        
        selectVerso1 = versosFormateados[num][0]
        selectVerso2 = versosFormateados[num][1]
        selectVerso3 = versosFormateados[num][2]
        selectVerso4 = versosFormateados[num][3]
        
        iterador(selectVerso1)
        iterador(selectVerso2)
        iterador(selectVerso3)
        iterador(selectVerso4)

class DiccionarioCreador():
    """
       Divicion de responsavilidades 
       esta clase se encarga de de toda la logida de rima,
       separandola asi de la logica de lectura
    """
    def __init__(self, versosList) -> None:
        """_summary_

        Args:
            versosList (list): versosFormateados
        """
        self.versosList = versosList
        self.diccionario = {}
        
        
        
    def recorreVerso(self,num):
        verso1=self.versosList[num][0]
        verso2=self.versosList[num][1]
        verso3=self.versosList[num][2]
        verso4=self.versosList[num][3]
        self.varIndexVar = 0
        
        
        print("--------------------------------- Patron 4x4 Str ---------------------------------")
        verso1Str = str(verso1).replace("[","").replace("]","").replace("'","").replace(",","")
        verso2Str = str(verso2).replace("[","").replace("]","").replace("'","").replace(",","")
        verso3Str = str(verso3).replace("[","").replace("]","").replace("'","").replace(",","")
        verso4Str = str(verso4).replace("[","").replace("]","").replace("'","").replace(",","")
        print(verso1Str)
        print(verso2Str)
        print(verso3Str)
        print(verso4Str)
        versos = f"{verso1Str}\n{verso2Str}\n{verso3Str}\n{verso4Str}"
        
        
        print("\n--------------------------------- Patron 4x4 List ---------------------------------")
        print(verso1)
        print(verso2)
        print(verso3)
        print(verso4)
        print()
        """ 
        Logica Principal
        """
        
        """ Selectores de palabras (Posiciones**) """
        varIndex1 = -1
        varIndex2 = -1
        select1 = self.diccionario.get(verso1[varIndex1])
        select2 = self.diccionario.get(verso2[varIndex2])
        
        def comprobador(select1, select2,verso1,verso2, varIndex1, varIndex2):
            """Logica recursiva para identificar las rimas de manera mas eficiente sin tanto bloque condicional
            
            

            Args:
                select1 (List): Valor devuelto por el diccionario
                select2 (list): Valor devuelto por el diccionario
                verso1 (_type_): _description_
                verso2 (_type_): _description_
                varIndex1 (_type_): _description_
                varIndex2 (_type_): _description_
            """
            
            """ Variables """
            selectorVerso1 = verso1[varIndex1]
            selectorVerso2 = verso2[varIndex2]
            
            
            
            if len(select1) == 4 and len(select2) == 4 and select1[-1] == select2[-1] and select1[-2] == select2[-2] and select1[-3] == select2[-3] and select1[-4] == select2[-4]:
                print(f"{verso1[-1]} - {verso2[varIndex2]}: Riman 4 silaba")
            elif len(select1) == 3 and len(select2) == 3 and  select1[-1] == select2[-1] and select1[-2] == select2[-2] and select1[-3] == select2[-3]:
                print(f"{verso1[-1]} - {verso2[varIndex2]}: Riman 3 silaba")
            elif len(select1) == 2 and len(select2) == 2 and select1[-1] == select2[-1] and select1[-2] == select2[-2]:
                print(f"{select1} - {verso2[varIndex2]}: Riman 2 silaba")
            elif len(select1) == 1 and len(select2) == 1 and select1[-1] == select2[-1]:
                print(f"{select1} - {verso2[varIndex2]}: Riman 1 silaba")
            else:
                print(f"{selectorVerso1} - {selectorVerso2}: No riman")
                
            versos2=versos.replace(f"{selectorVerso1}",f"{Style.BRIGHT + Fore.BLUE}{selectorVerso1}{Style.RESET_ALL}")
            versos2=versos2.replace(f"{selectorVerso2}",f"{Style.BRIGHT + Fore.BLUE}{selectorVerso2}{Style.RESET_ALL}")
            
            
            
            self.varIndexVar += 1
            if self.varIndexVar < len(verso2    ):
                comprobador(select1, select2, verso1, verso2, varIndex1, varIndex2=self.varIndexVar)
            elif self.varIndexVar >= len(verso1):
                print("\n--------------------------------- Patron 4x4 Rimado ---------------------------------")
                print(versos2)
            
                
            

        comprobador(select1, select2, verso1, verso2, varIndex1, varIndex2)
        
        
        
        
    def almacenaSilabas(self, num):
        """
        - recorre la estructura 4x4, parrafo por parrafo
        - se detiene en cada palabra de cada verso
        - la recorre y la almacera en diccionario
        - {"palabra":["vocales"]}
        - {"hola":["o","a"]}
        Args:
            num (INT): numero que recorre los versos (patron) 4x4, dicho argumento debe ser iterado segun la cantidad de versos
        """
        temp=self.versosList[num]
        for patron in  temp:
            for palabra in patron:
                listVocalTemp = []
            
                for letra in palabra:
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
                        
                    self.diccionario[palabra] = listVocalTemp