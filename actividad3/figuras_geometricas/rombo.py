from math import sqrt

class Rombo:
    """
    Esta clase define objetos de tipo Rombo con una
    diagonal mayor y una diagonal menor como atributos.
    
    Args:
        diagonal_mayor (float): Longitud de la diagonal mayor del rombo
        diagonal_menor (float): Longitud de la diagonal menor del rombo
    
    Raises:
        ValueError: Si las diagonales no son un número positivo.
    """
    def __init__(self, diagonal_mayor: float, diagonal_menor: float) -> None:
        """
        Constructor de la clase Rombo.
        """
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser números positivos.")
        self.diagonal_mayor = diagonal_mayor # Atributo que define la diagonal mayor del rombo.
        self.diagonal_menor = diagonal_menor # Atributo que define la diagonal menor del rombo.
        
    def calcular_lado(self) -> float:
        """
        Método que calcula y devuelve el lado de un rombo,
        con base en sus diagonales y el Teorema de Pitágoras.
        
        Returns:
            float: Longitud del lado de un rombo.
        """
        return sqrt(self.diagonal_mayor ** 2 + self.diagonal_menor ** 2) / 2
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un rombo
        como la diagonal mayor multiplicada por la diagonal menor sobre 2.
        
        Returns:
            float: Área de un rombo.
        """
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un rombo
        como la suma de sus 4 lados.
        
        Returns:
            float: Perímetro de un rombo.
        """
        return 4 * self.calcular_lado()
    