from math import sqrt

class TrianguloRectangulo:
    """
    Esta clase define objetos de tipo Triángulo Rectángulo con una
    base y una altura como atributos.
    """
    
    def __init__(self, base: int, altura: int) -> None:
        """
        Constructor de la clase TriánguloRectángulo.
        
        Args:
            base (int): Parámetro que define la base de un triángulo rectángulo.
            altura (int): que define la altura de un triángulo rectángulo.
        """
        self.base = base # Atributo que define la base de un triángulo rectángulo.
        self.altura = altura # Atributo que define la altura de un triángulo rectángulo.
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un triángulo rectángulo
        como la base multiplicada por la altura sobre 2.
        
        Returns:
            float: Área de un triángulo rectángulo.
        """
        return (self.base * self.altura) / 2
    
    def calcular_hipotenusa(self) -> float:
        """
        Método que calcula y devuelve la hipotenusa de un triángulo 
        rectángulo utilizando el teorema de Pitágoras.
        
        Returs:
            float: Hipotenusa de un triángulo rectángulo.
        """
        return sqrt(self.base ** 2 + self.altura ** 2)
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un triángulo
        rectángulo como la suma de la base, la altura y la hipotenusa.
        
        Returns:
            float: Perímetro de un triángulo rectángulo.
        """
        hipotenusa = self.calcular_hipotenusa() # Invoca al método calcular hipotenusa.
        return self.base + self.altura + hipotenusa
    
    def determinar_tipo_triangulo(self) -> None:
        """
        Método que determina si un triángulo es:
        - Equilatero: si sus tres lados son iguales.
        - Escaleno: si sus tres lados son todos diferentes.
        - Escaleno: si dos de sus lados son iguales y el otro es diferente de los demás.
        """
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.altura == hipotenusa:
            print("Es un triángulo equilátero.") # Todos sus lados son iguales.
        elif self.base != self.altura and self.altura != hipotenusa and self.base != hipotenusa:
            print("Es un triángulo escaleno.") # Todos sus lados son diferentes.
        else:
            print("Es un triángulo isósceles.") # De otra manera, es isósceles.
