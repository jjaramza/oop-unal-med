from math import pi

class Circulo:
    """
    Esta clase define objetos de tipo Círculo con su radio como atributo.
    """
    
    def __init__(self, radio: int) -> None:
        """
        Constructor de la clase Círculo.
        
        Args:
            radio (int): Parámetro que define el radio de un círculo.
        """
        self.radio = radio # Atributo que define el radio de un círculo
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un círculo como pi 
        multiplicado por el radio al cuadrado.
        
        Returns:
            float: Área de un círculo.
        """
        return pi * (self.radio ** 2)
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un círculo como la
        multiplicación de pi por el radio por 2.
        
        Returns:
            float: Perímetro de un círculo.
        """
        return 2 * pi * self.radio
