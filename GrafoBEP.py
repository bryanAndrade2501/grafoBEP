from Grafo import Grafo

class grafoBEP(Grafo):

    def __init__(self):
        super().__init__()
        self.tiempo=0
    
    def busquedaEnProfundidad(self):
        for nodoX in self:
            if nodoX.obtenerColor() == 'blanco':
                self.visitaBusquedaEnProfundidad(nodoX)

    def visitaBusquedaEnProfundidad(self,nodoInicio):
        nodoInicio.asignarColor('gris')
        self.tiempo += 1
        nodoInicio.asignarDescubrimiento(self.tiempo)
        for proximoNodo in nodoInicio.obtenerConexiones():
            if proximoNodo.obtenerColor() == 'blanco':
                proximoNodo.asignarPredecesor(nodoInicio.id)
                self.visitaBusquedaEnProfundidad(proximoNodo)
        nodoInicio.asignarColor('negro')
        self.tiempo += 1
        nodoInicio.asignarFinalizacion(self.tiempo)
