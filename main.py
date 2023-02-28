import os
from clearwindow import clearWindow
clearWindow() 

class Menu:
    #Esta clase define el estado y el comportamiento del menu
    
    def __init__(self):
        self.header= "\t\t:..Analizar Rimas..:\n"
        self.opcion = None

    def selector(self):
        if self.opcion == None:
            self.menuPrincipal()
        elif self.opcion == 1:
            self.listaArchivos()
        elif self.opcion == 0:
            print("Ctrl + C")            
            
        try:
            self.opcion = int(input("\nIngrese una Opcion: "))
        except ValueError:
            print("Ops... Ingrese una opcion valida (Base 10)")

    def menuPrincipal(self):
        """
        Menu Principal
        """
        clearWindow() 
        print(self.header)
        print("1: Listar canciones")
        print("0: Salir")
    
    def listaArchivos(self):

        self.direccionArchivo = ""
        clearWindow() #limpia la pantalla
        print(self.header) # imprime un header global
        
        
        ls = os.listdir("letras/") # enlista archivos dentro de una lista
        indice = 0 # enumera los archivos para el menu / sirve como index para seleccionar dentro de la lista
        for archivo in ls:
            indice += 1
            print(f"{indice}: {archivo}")
        print("\n0: <- Retroceder")
        print(f"indice: {indice}")
        while True:
            try:
                self.opcion = int(input("\nIngrese una Opcion: "))
                if self.opcion > 0 and self.opcion <= indice:
                    self.direccionArchivo = f"letras/{ls[self.opcion-1]}"
                elif self.opcion == 0:
                    self.menuPrincipal()
            except ValueError:
                print("Ops... Ingrese una opcion valida (Base 10)")
 

menu = Menu()



while True:
    menu.selector()