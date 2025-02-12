import math
from figuras.figura_geometrica import FiguraGeometrica

class Esfera(FiguraGeometrica):
    """
    Esta clase denominada Esfera es una subclase de FiguraGeométrica
    que cuenta con un radio.
    """
    def __init__(self, radio: float):
        """
        Constructor de la clase Esfera.
        
        Args:
            radio (float): Define el radio de una esfera.
        """
        super().__init__()
        self.__radio = radio
        self.volumen =  self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self) -> float:
        """
        Método para calcular el volumen de una esfera.
        
        Returns:
            float: El volumen de una esfera.
        """
        volumen: float = (4/3) * math.pi * (self.__radio ** 3)
        return volumen
    
    def calcular_superficie(self) -> float:
        """
        Método para calcular la superficie de una esfera.
        
        Returns:
            float: La superficie de una esfera.
        """
        superficie: float = 4 * math.pi * (self.__radio ** 2)
        return superficie
