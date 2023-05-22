from clearwindow import clearWindow
import unidecode
from logica_rima import logica, logica2, DiccionarioCreador
clearWindow()

#entrada
archivo = "al2-kien.txt"

class Func:
    def __init__(self,archivo):
        self.diccionario = {}
        self.archivo = archivo 
        self.versosFormateados = self.reader() # = Estruptura 4x4
        self.versosTextoPlano = ""
        
    def reader(self):
        """
        - Se espera la informacion de entrada este correctamente formateada
        - Recorre la informacion de un archivo linea por linea
        - almacena en formato list
        
        Returns:
            return: type(tuple)
            versosLista: type(list) versos sin agrupar // sin formato
        """    
        versosLista = [] 
        versosFormateadosTemp = []
        
        # Habre "archivo" y lo lee linea por linea alcenandolo en "versosLista"
        # versosLista=["","","","","","","","","","","","","","","",""]
        with open(f'letras/{self.archivo}', 'r',
                encoding="utf-8") as fichero:
            temp = fichero.readlines()
            for linea in temp:
                linea = linea.lower()
                # Elimina las tildes
                linea = unidecode.unidecode(linea)
                versosLista.append(linea.split())
        
        # Recorre "versosLista" los almacena en "versosFormateadosTemp" de 4 en 4, generando la estruptura del RAP
        # versosFormateadosTemp=[["","","",""],["","","",""],["","","",""],["","","",""]] = Estruptura 4x4
        num_min = 0
        num_max = 4
        while num_max <= len(versosLista):
            versosFormateadosTemp.append(versosLista[num_min:num_max])
            num_min = num_max + 1
            num_max += 5
        
        return versosFormateadosTemp # = Estruptura 4x4    

    def diccionarioCreate(self, num):
        """
        - recorre la estructura 4x4, parrafo por parrafo
        - se detiene en la ultima palabra de cada verso
        - la recorre y la almacera en diccionario
        - {"palabra":["vocales"]}
        - {"hola":["o","a"]}
        Args:
            num (INT): numero que recorre los versos 4x4, dicho argumento debe ser iterado segun la cantidad de versos
        """
        temp=self.versosFormateados[num]
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
                self.diccionario[ultimaPalabra] = listVocalTemp

    def rimador_complemento(self, linea):
            """
            - Esta funcion solo tiene sentido llamada desde el metodo "rimador"
            - Recorre un verso(lista) y lo convierte a str

            Args:
                linea (list): indica el verso exacto el cual sera recorrido

            Returns:
                versosTemp (str): verso individual(1/4)  para posterior union en una sola estrofa(4/4)
            """
            contadorVerso=0
            parrafoTemp = ""
            
            """ 
            - linea = =["pal","pal","pal","pal","pal","pal","pal","pal"]
            - recorre palabra por palabra en "linea"
            - por cada iteracion = "contadorVerso += 1" (Cuenta cuantas palabras a recorrido)
            - if(Si la cantidad de palabras recorridas es diferente a la cantidad de palabras total en "linea")
            {entoncces agrega esa palabra a "parrafoTemp" mas un espacio en blanco} 
            else{De lo contrario agrega la palabra a "parrafoTemp" y agrega un salto de linea}
            """
            for palabra in linea:
                contadorVerso+=1
                palabra = palabra.replace('"','')
                if contadorVerso != len(linea):
                    parrafoTemp += palabra+" "
                elif contadorVerso == len(linea):
                    parrafoTemp += f"{palabra}\n"
                    contadorVerso=0
            return parrafoTemp

    def rimador(self, num):
        """
        - Esta funcion se encarga de dar el ultimo formado y de identificar la rimar y colorear los versos

        Args:
            num (INT): Indica el numero del parrafo sobre el cual trabaja la funcion

        Returns:
            versosTextoPlano: Salida final, parrafos estructurados y rimados
        """
        
        """
        estrofa = ""    

        # ultima palabra[-1] del verso 1[0]
        # selectorVerso / selecciona el verso completo
        # selector / limpia el dato y lo almacena
        selectorVerso1 = self.versosFormateados[num][0]
        selector1 = self.versosFormateados[num][0][-1].replace('"','')
        
        selectorVerso2 = self.versosFormateados[num][1]
        selector2 = self.versosFormateados[num][1][-1].replace('"','')
        
        selectorVerso3 = self.versosFormateados[num][2]
        selector3 = self.versosFormateados[num][2][-1].replace('"','')
        
        selectorVerso4 = self.versosFormateados[num][3]
        selector4 = self.versosFormateados[num][3][-1].replace('"','')
        
        #Buscar el selector dentro del diccionario
        vocales1 = self.diccionario.get(selector1)
        vocales2 = self.diccionario.get(selector2)
        vocales3 = self.diccionario.get(selector3)
        vocales4 = self.diccionario.get(selector4)
            
        verso1=self.rimador_complemento(selectorVerso1)
        verso2=self.rimador_complemento(selectorVerso2)
        verso3=self.rimador_complemento(selectorVerso3)
        verso4=self.rimador_complemento(selectorVerso4)
        
        estrofa += verso1+verso2+verso3+verso4
        """
        # Logica de rimas
        # Verso 1 - Verso 2
        # si tiene 3 vocales o mas y todas riman
        #self.versosTextoPlano += logica(estrofa, vocales1, vocales2, vocales3, vocales4, selector1, selector2, selector3, selector4)
        #logica2(self.diccionario, self.versosFormateados, num)
        
        recorreVersos = DiccionarioCreador(self.versosFormateados)
        recorreVersos.almacenaSilabas(num)
        recorreVersos.recorreVerso(num)
        
        print("\n----------------------------------- Diccionario ----------------------------------------------")
        for i,a in recorreVersos.diccionario.items():
            print(i,a)


    def run(self):
        for i in range(len(self.versosFormateados)):
            self.diccionarioCreate(i)
            self.rimador(i)
            self.diccionario.clear()
            
        print(self.versosTextoPlano)
        
    def run_debug(self,nun):
        self.diccionarioCreate(nun)
        self.rimador(nun)
        self.diccionario.clear()
            
        print(self.versosTextoPlano)

        
obj = Func(archivo)
obj.run_debug(2)