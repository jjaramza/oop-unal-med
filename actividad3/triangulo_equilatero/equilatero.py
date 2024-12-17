from math import sqrt

class Equilatero:
    """
    Esta clase define objetos de tipo Equilatero la cual tiene el atributo lado.

    Attributes:
        lado (float): Parámetro que define el lado de un triángulo rectángulo
        RAIZ_DE_TRES (float): Constante que presenta la raíz cuadrada de 3
    """
    
    RAIZ_DE_TRES = sqrt(3) # Constante de clase: cálculo de la raíz cuadrada de 3.
    
    def __init__(self, lado: float) -> None:
        """
        Constructor de la clase Equilatero

        Args:
            lado (float): Parámetro que define el lado de un triángulo rectángulo
        """
        self.lado = lado
        
    def perimetro_equilatero(self) -> float:
        """
        Calcula y devuelve el perímetro de un triángulo equilátero
        como la suma de sus tres lados.

        Returns:
            float: Perímetro de un triángulo rectángulo
        """
        return 3 * self.lado
    
    def altura_equilatero(self) -> float:
        """
        Calcula y devuelve la altura de un triángulo equilátero
        como el lado multiplicado por la raíz cuadrada de 3, sobre 2.

        Returns:
            float: Altura de un triángulo rectángulo
        """
        return (self.RAIZ_DE_TRES / 2) * self.lado
    
    def area_equilatero(self) -> float:
        """
        Calcula y devuelve el área de un triángulo equilátero
        como el cuadrado del lado multiplicado por la raíz cuadrada de 3, sobre 4.

        Returns:
            float: Área de un triángulo rectángulo
        """
        return (self.RAIZ_DE_TRES / 4) * (self.lado ** 2)
