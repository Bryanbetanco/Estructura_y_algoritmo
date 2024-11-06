class ColaEspecial:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.inicio = 0
        self.fin = 0
        self.lleno = False
        self.direccion = 1  # 1 indica dirección hacia adelante, -1 hacia atrás
    
    def insertar(self, elemento):
        if self.lleno:
            # Si la cola está llena, sobreescribimos el elemento más antiguo
            if self.direccion == 1:
                # En caso de avanzar en la cola
                self.inicio = (self.inicio + 1) % self.capacidad
            else:
                # En caso de retroceder en la cola
                self.inicio = (self.inicio - 1 + self.capacidad) % self.capacidad
        
        # Insertamos el nuevo elemento
        self.cola[self.fin] = elemento
        self.fin = (self.fin + self.direccion) % self.capacidad
        
        # Verificamos si hemos llegado al final de la cola en ambas direcciones
        if self.fin == self.inicio:
            self.lleno = True
        
        # Cambiamos de dirección si llegamos al final
        if self.fin == 0 or self.fin == self.capacidad - 1:
            self.direccion *= -1
    
    def obtener_cola(self):
        if self.inicio < self.fin or not self.lleno:
            return self.cola[self.inicio:self.fin]
        else:
            return self.cola[self.inicio:] + self.cola[:self.fin]

# Prueba con el ejemplo del enunciado
def PruebaColaEspecial():
    secuencia = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cola = ColaEspecial()
    
    for letra in secuencia:
        cola.insertar(letra)
        print(f"Cola después de insertar '{letra}': {cola.obtener_cola()}")

# Ejecutamos la prueba
PruebaColaEspecial()
