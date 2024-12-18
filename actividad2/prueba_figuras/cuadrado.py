class Cuadrado:
    """
    Esta clase define objetos de tipo Cuadrado con un lado como atributo.
    """
    
    def __init__(self, lado: int) -> None:
        """
        Constructor de la clase Cuadrado.
        
        Args:
            lado (int): Parámetro que define la longitud de la base de un cuadrado.
        """
        self.lado = lado # Atributo que define el lado de un cuadrado.
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un cuadrado como el
        lado elevado al cuadrado.
        
        Returns:
            float: Área de un Cuadrado
        """
        return self.lado * self.lado
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un cuadrado como 
        cuatro veces su lado.
        
        Returns:
            float: Perímetro de un cuadrado.
        """
        return 4 * self.lado
        