class Boleta(): #Declaramos la clase Boleta, la cual deriva de la clase Worker
    
    def __init__(self, category, exhours, mxt): #se inicializa el constructor con los atributos

        self.exhours =exhours
        self.mxt = mxt
        self.category = category
    
    
    def fijarSB(self): # creamos la funcion "fijarSB", para identicar el tipo de sueldo básico dependiendo de su categoría

        if self.category == 'A':
            sb = 3000
            
        elif self.category == 'B':
            sb = 2500
            
        else:
            sb = 2000
            
        return sb # retornar resultado a la función
    
    
    def calcularph(self): #creamos la función "calcularph", aquí calculamos el pago por hora del trabajador 

        if self.category == 'A': #Utilizamos la formula "PH" para relizar el cálculo 
            ph = round(self.fijarSB() / 240,2) #usamos la funcion round() y para redondear a solo 2 decimales
            
        elif self.category == 'B':
            ph = round(self.fijarSB() / 240,2)
            
        else:
            ph = round(self.fijarSB() / 240,2)

        return ph
    

    def calcularphx(self):#creamos la funcion "calcularphx", para calcular el pago por horas extras

        if self.category == 'A':
            phx = round(self.calcularph() * self.exhours, 2)
            
        elif self.category == 'B':
            phx = round(self.calcularph() * self.exhours, 2)
            
        else:
            phx = round(self.calcularph() * self.exhours, 2)
        
        return phx
    
    
    def descontarTar(self):#  Creamos la funcion descontarTar= Descontar Tardanza 
        
        dxt = round(((self.fijarSB() / 240) / 60) * self.mxt, 2)

        return dxt


    def calcularSN(self):#  Creamos la funcion calcularSN= calcular sueldo neto
        
        sueldon = round(self.fijarSB() - self.descontarTar() + self.calcularphx(), 2)
        
        return sueldon

    


