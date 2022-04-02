from Worker import Worker
from Boleta import Boleta

def imprimir(): 
      print(f"""----------------------------------------------------------------            
                        DATOS INGRESADOS
                  
                  TRABAJADOR:          {worker1.worker}
                  
                  CATEGORÍA:           {worker1.category}
                  
                  HORAS EXTRAS:        {boleta1.exhours}
                  
                  TARDANZA(minutos):   {boleta1.mxt}
                  
----------------------------------------------------------------
                        BOLETA DE PAGO          

            NOMBRE:                   {worker1.worker}

            CATEGORÍA:                {worker1.category}

            SUELDO BÁSICO:            S/.{boleta1.fijarSB()}

            DESCUENTO POR TARDANZA:   S/.{boleta1.descontarTar()}

            PAGO POR HORAS EXTRAS:    S/.{boleta1.calcularphx()}

            SUELDO NETO:              S/.{boleta1.calcularSN()}
                        
                  
----------------------------------------------------------------
      """) 

#Bloque principal
worker1 = Worker()
worker1.inicio()
worker1.iworker()

category = worker1.icategory()
exhours = worker1.iexhours()
mxt = worker1.imxt()

boleta1 = Boleta(category, exhours, mxt)
#Salida
imprimir()

