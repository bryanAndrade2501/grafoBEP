class Nodo:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        #Nuevas variables
        self.color='blanco'
        self.predecesor=-1
        self.tiempoDescubrimiento = 0
        self.tiempoFinalizacion = 0

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado A: ' + str([x.id for x in self.conectadoA]) +" predecesor: "+ str([self.predecesor])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
    
    def asignarColor(self,valorColor):
        self.color = valorColor
    
    def obtenerColor(self):
        return self.color
    
    def asignarPredecesor(self, valorPredecesor):
        self.predecesor = valorPredecesor
    
    def obtenerPredecesor(self):
        return self.predecesor
    
    def asignarDescubrimiento(self, tiempoDes):
        self.tiempoDescubrimiento = tiempoDes
    
    def obtenerDescubrimiento(self):
        return self.tiempoDescubrimiento
    
    def asignarFinalizacion(self,tiempoFin):
        self.tiempoFinalizacion = tiempoFin

    def obtenerFinalizacion(self):
        return self.tiempoFinalizacion

    
