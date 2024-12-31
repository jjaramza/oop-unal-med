from math import sqrt

class Trapecio:
    """
    Esta clase define objetos de tipo Trapecio con una
    base mayor, una base menor y sus lados no paralelos como atributos.
    
    Args:
        base_mayor (float): Longitud de la base mayor del trapecio
        base_menor (float): Longitud de la base menor del trapecio
        lado_1 (float): Longitud de un lado no paralelo del trapecio
        lado_2 (float): Longitud de un lado no paralelo del trapecio
        altura (float): Longitud de la altura del trapecio
        
    Raises:
        ValueError: Si las bases, lados o altura no son un número positivo.
    """
    def __init__(
        self,
        base_mayor: float,
        base_menor: float,
        lado_1: float,
        lado_2: float,
        altura: float
    ) -> None:
        """
        Constructor de la clase Trapecio.
        """
        if base_mayor <= 0 or base_menor <= 0 or lado_1 <= 0 or lado_2 <= 0:
            raise ValueError("Los valores deben ser números positivos.")
        self.base_mayor = base_mayor # Atributo que define la base mayor del trapecio.
        self.base_menor = base_menor # Atributo que define la base menor del trapecio.
        self.lado_1 = lado_1 # Atributo que define un lado no paralelo del trapecio.
        self.lado_2 = lado_2 # Atributo que define un lado no paralelo del trapecio.
        self.altura = altura # Atributo que define un lado no paralelo del trapecio.
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un trapecio
        como la suma de sus bases entre dos, por la altura,
        es decir, la distancia perpendicular entre las bases.
        
        Returns:
            float: Área de un trapecio.
        """
        return ((self.base_mayor + self.base_menor) / 2) * self.altura
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un trapecio
        como la suma de sus 2 bases y sus 2 lados.
        
        Returns:
            float: Perímetro de un trapecio.
        """
        return self.base_mayor + self.base_menor + self.lado_1 + self.lado_2
    