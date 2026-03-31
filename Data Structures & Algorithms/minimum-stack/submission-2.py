class MinStack:

    def __init__(self):
        self.lista = []
        self.min_lista = []
        
        
#Apilar    
    def push(self, val: int) -> None:
        self.lista.append(val)

        if self.min_lista:
            val = min(val, self.min_lista[-1])

            self.min_lista.append(val)

        else:
            self.min_lista.append(min(val, val))
    



        
#Eliminar
    def pop(self) -> None:
        self.lista.pop()
        self.min_lista.pop()
        
#Obtener el último
    def top(self) -> int:
        return self.lista[-1]

        
#Obtner el minimo valor de la pila
    def getMin(self) -> int:
        return self.min_lista[-1]



    # [5,1,2]
        
