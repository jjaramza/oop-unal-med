class Cuadrado:
    """
    Esta clase define objetos de tipo Cuadrado con un lado como atributo.
    
    Args:
        lado (float): Parámetro que define la longitud de la base de un cuadrado.
        
    Raises:
        ValueError: Si el lado no es un número positivo.
    """
    def __init__(self, lado: float) -> None:
        """
        Constructor de la clase Cuadrado.
        """
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
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
        