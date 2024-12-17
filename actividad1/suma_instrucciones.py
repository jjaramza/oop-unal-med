# Ejercicio resuelto No 5 del libro de Lógica de Programación de Efrain Oviedo

class SumaInstrucciones:
    """
    Realiza una suma a partir de ciertas instrucciones.
    """
    def __init__(self):
        """
        Constructor para inicializar las variables a emplear
        """
        self.SUMA = 0
        self.X = 20
        self.Y = 40
        
    def realizar_calculos(self):
        """
        Método para realizar los cálculos
        """
        self.SUMA += self.X
        self.X += self.Y ** 2
        self.SUMA += self.X / self.Y
        return self.SUMA


if __name__ == "__main__":
    # Crear instancia de clase
    sumar_ins = SumaInstrucciones()
    
    # Mostrar resultado
    print(f"El valor de la suma es: {sumar_ins.realizar_calculos()}")
