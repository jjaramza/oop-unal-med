# Ejercicio propuesto No 14 del libro de Lógica de Programación de Efrain Oviedo

class Potencia:
    """
    A partir de un número dado, calcula su cuadrado y su cubo.
    """
    def __init__(self, numero: int):
        """Inicializa el número dado"""
        self.numero = numero
        
    def calcular_cuadrado(self) -> int:
        """Calcula el cuadrado de un número"""
        return self.numero ** 2
    
    def calcular_cubo(self) -> int:
        """Calcula el cubo de un número"""
        return self.numero ** 3


if __name__ == "__main__":
    # Se solicita el número al usuario
    numero = int(input("Ingrese un número: "))
    
    # Se crea un objeto de la clase Potencia
    potencia = Potencia(numero)
    
    # Se muestra por pantalla el resultado
    print(f"El cuadrado de {numero} es {potencia.calcular_cuadrado()}")
    print(f"El cubo de {numero} es {potencia.calcular_cubo()}")
