# Ejercicio propuesto No 17 del libro de Lógica de Programación de Efrain Oviedo

from math import pi

class Circulo:
    """
    Permite calcular el área del círculo y la longitud de la circunferencia
    """
    def __init__(self, radio: float):
        """Inicializa el radio del círculo."""
        self.radio = radio
        
    def area_circulo(self) -> float:
        """Calcula el área de un círculo de un radio dado."""
        return pi * self.radio ** 2
    
    def longitud_circunferencia(self) -> float:
        """Calcula la longitud de una circunferencia a partir de su radio."""
        return 2 * pi * self.radio
    
    
if __name__ == "__main__":
    # Se solicita el radio de un círculo
    radio = float(input("Ingrese el radio de un círculo: "))
    
    # Se crea un objeto de la clase Circulo
    circulo = Circulo(radio)
    
    # Muestra el área del círculo y la longitud de su circunferencia con 4 decimales
    print(f"Área del círculo de radio {radio} es {circulo.area_circulo():.4f}")
    print(f"Longitud de la circunferencia de radio {radio} es {circulo.longitud_circunferencia():.4f}")
