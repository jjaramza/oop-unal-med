class FiguraGeometrica:
    """
    Esta clase denominada FiguraGeométrica modela un figura
    geométrica que cuenta con un volumen y una superficie a ser
    calculados de acuerdo al tipo de figura geométrica.
    
    Attributes:
        __volumen (float): Identifica el volumen de una figura geométrica.
        __superficie (float): Identifica la superficie de una figura geométrica.
    """
    def __init__(self):
        """
        Constructor de la clase FiguraGeometrica.
        """
        self.__volumen: float = 0.0
        self.__superficie: float =  0.0
    
    @property
    def volumen(self) -> float:
        """
        Método para obtener el volumen de una figura geométrica.
        
        Returns:
            float: El volumen de una figura geométrica
        """
        return self.__volumen
    
    @volumen.setter
    def volumen(self, volumen: float) -> None:
        """
        Método para establecer el volumen de una figura geométrica.
        
        Args:
            volumen (float): Parámetro que define el volumen de una figura geométrica.
        """
        self.__volumen = volumen
    
    @property
    def superficie(self) -> float:
        """
        Método para obtener la superficie de una figura geométrica.
        
        Returns:
            float: La superficie de una figura geométrica
        """
        return self.__superficie
    
    @superficie.setter
    def superficie(self, superficie: float) -> None:
        """
        Método para establecer la superficie de una figura geométrica.
        
        Args:
            Parámetro que define la superficie de una figura geométrica.
        """
        self.__superficie = superficie
