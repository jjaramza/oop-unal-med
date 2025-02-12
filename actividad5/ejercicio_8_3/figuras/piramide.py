from figuras.figura_geometrica import FiguraGeometrica

class Piramide(FiguraGeometrica):
    """
    Esta clase denominada Pirámide es una subclase de FiguraGeométrica
    que cuenta con una base, una altura y un apotema.
    """
    def __init__(self, base: float, altura: float, apotema: float):
        """
        Constructor de la clase Pirámide.
        
        Args:
            base (float): Define la base de una pirámide.
            altura (float): Define la altura de una pirámide.
            apotema (float): Define el apotema de una pirámide.
        """
        super().__init__()
        self.__base = base
        self.__altura = altura
        self.__apotema = apotema
        self.volumen =  self.calcular_volumen()
        self.superficie = self.calcular_superficie()
    
    def calcular_volumen(self) -> float:
        """
        Método para calcular el volumen de una pirámide.
        
        Returns:
            float: El volumen de una pirámide.
        """
        volumen: float = (1/3) * (self.__base ** 2) * self.__altura
        return volumen
    
    def calcular_superficie(self) -> float:
        """
        Método para calcular la superficie de una pirámide.
        
        Returns:
            float: La superficie de una pirámide.
        """
        area_base: float = self.__base ** 2
        area_lado:float = 2 * self.__base * self.__apotema
        return area_base + area_lado
