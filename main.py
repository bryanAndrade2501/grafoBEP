class Nodo:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        self.listaNodos = {}
        self.numNodos = 0

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

g = Grafo()
for i in range(6):
    g.agregarNodo(i)
g.listaNodos

g.agregarArista(0,1,5)
g.agregarArista(0,5,2)
g.agregarArista(1,2,4)
g.agregarArista(2,3,9)
g.agregarArista(3,4,7)
g.agregarArista(3,5,3)
g.agregarArista(4,0,1)
g.agregarArista(5,4,8)
g.agregarArista(5,2,1)

for n in g:
    for w in n.obtenerConexiones():
        print("( %s , %s )" % (n.obtenerId(), w.obtenerId()))