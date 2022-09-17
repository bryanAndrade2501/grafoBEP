from Nodo import Nodo
class Grafo:
    def __init__(self,directed=False):
        self.listaNodos = {}
        self.numNodos = 0
        self._outgoing = { }
# only create second map for directed graph; use alias for undirected
        self._incoming = { } if directed else self._outgoing

    def agregarNodo(self,clave):
        self.numNodos = self.numNodos + 1
        nuevoNodo = Nodo(clave)
        self.listaNodos[clave] = nuevoNodo
        return nuevoNodo

    def obtenerNodo(self,n):
        if n in self.listaNodos:
            return self.listaNodos[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaNodos

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaNodos:
            nv = self.agregarNodo(de)
        if a not in self.listaNodos:
            nv = self.agregarNodo(a)
        self.listaNodos[de].agregarVecino(self.listaNodos[a], costo)

    def obtenerNodos(self):
        return self.listaNodos.keys()

    def __iter__(self):
        return iter(self.listaNodos.values())
    