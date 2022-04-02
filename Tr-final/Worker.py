from colorama import *

class Worker: #Declaramos la clase worker= Trabajador

    def __init__(self): 

        self.worker = None
        self.category = None
        self.exhours = None
        self.mxt = None
        
    def inicio(self):    
        print(f"""
                            ----------------------------- 
                            |  RAZON SOCIAL:  FERROTEK  |
                            ----------------------------- 
                    
                INGRESAR DATOS:
                """) 
       
    def iworker(self):  
            
            self.worker = str(input("TRABAJADOR :  ").upper())# la funcion upper sirve para que el contenido se convierta en mayúscula
            
            return self.worker
            
            
    def icategory(self):   
            
        while True: #se usa el bucle "WHILE" para que el programa pregunte hasta que se ingrese un dato valido
            try:
                self.category= str(input("CATEGORÍA (A, B o C) :  ").upper())
                if self.category == 'A' or self.category == 'B' or self.category == 'C':
                    break 
                else:
                    print(Fore.CYAN,'EL CARÁCTER INGRESADO NO PERTENECE A LAS CATEGORÍAS ESTABLECIDAS',Fore.RESET)
            except:
                print(Fore.CYAN,'EL CARÁCTER INGRESADO NO PERTENECE A LAS CATEGORÍAS ESTABLECIDAS',Fore.RESET)
                
        return self.category
    
    
    def iexhours(self):
        
        while True:
            try:
                self.exhours= int(input("HORAS EXTRAS :  "))
                break  # Si introduce el dato correcto, se detiene el "while" con "break"
            except ValueError:
                    print(Fore.CYAN,"DATO INVALIDO",Fore.RESET)
        return self.exhours


    def imxt(self):
        
        while True:
            try:
                self.mxt= int(input("TARDANZAS (minutos) :  "))
                break  # Si introduce el dato correcto, se detiene el "while" con "break"# Si no da error, corto el while con break
            except ValueError:
                print(Fore.CYAN,"DATO INVALIDO",Fore.RESET)
                
        return self.mxt
    
    
    
        
        
