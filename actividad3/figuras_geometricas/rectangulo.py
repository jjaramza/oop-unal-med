class Rectangulo:
    """
    Esta clase define objetos de tipo Rectángulo con una base 
    y una altura como atributos.
    
    Args:
        base (float): Parámetro que define la base de un rectángulo.
        altura (float): Parámetro que define la altura de un rectángulo.
        
    Raises:
        ValueError: Si la base o la altura no son un número positivo.
    """
    def __init__(self, base: float, altura: float) -> None:
        """
        Constructor de la clase Rectangulo
        """
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser números positivos.")
        self.base = base # Atributo que define la base de un rectángulo.
        self.altura = altura # Atributo que define la altura de un rectángulo.
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un rectángulo como la
        multiplicación de la base por la altura.
        
        Returns:
            float: Área de un rectángulo.
        """
        return self.base * self.altura
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un rectángulo 
        como (2 * base) + (2 * altura).
        
        Returns:
            float: Perímetro de un rectángulo.
        """
        return (2 * self.base) + (2 * self.altura)
