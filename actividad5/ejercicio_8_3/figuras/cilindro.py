import math
from figuras.figura_geometrica import FiguraGeometrica

class Cilindro(FiguraGeometrica):
    """
    Esta clase denominada Cilindro es una subclase de FiguraGeométrica
    que cuenta con un radio y una altura.
    """
    def __init__(self, radio: float, altura: float):
        """
        Constructor de la clase Cilindro.
        
        Args:
            radio (float): Define el radio de un cilindro.
            altura (float): Define la altura de un cilindro.
        """
        super().__init__()
        self.__radio = radio
        self.__altura = altura
        self.volumen =  self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self) -> float:
        """
        Método para calcular el volumen de un cilindro.
        
        Returns:
            float: El volumen de un cilindro.
        """
        volumen: float = math.pi * self.__altura * (self.__radio ** 2)
        return volumen
    
    def calcular_superficie(self) -> float:
        """
        Método para calcular la superficie de un cilindro.
        
        Returns:
            float: La superficie de un cilindro.
        """
        superficie: float = 2 * math.pi * self.__radio * (self.__radio + self.__altura)
        return superficie
