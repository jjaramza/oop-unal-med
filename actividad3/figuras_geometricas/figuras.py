from math import pi, sqrt


class Circulo:
    """
    Esta clase define objetos de tipo Círculo con su radio como atributo.
    
    Args:
        radio (float): Parámetro que define el radio de un círculo.
            
    Raises:
        ValueError: Si el radio no es un número positivo.
    """
    def __init__(self, radio: float) -> None:
        """
        Constructor de la clase Círculo.
        """
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio # Atributo que define el radio de un círculo
        
    def calcular_area(self) -> float:
        """
        Método que calcula y devuelve el área de un círculo como pi 
        multiplicado por el radio al cuadrado.
        
        Returns:
            float: Área de un círculo.
        """
        return pi * (self.radio ** 2)
    
    def calcular_perimetro(self) -> float:
        """
        Método que calcula y devuelve el perímetro de un círculo como la
        multiplicación de pi por el radio por 2.
        
        Returns:
            float: Perímetro de un círculo.
        """
        return 2 * pi * self.radio


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
    

class TrianguloRectangulo:
    """
    Esta clase define objetos de tipo Triángulo Rectángulo con una
    base y una altura como atributos.
    
    Args:
        base (float): Parámetro que define la base de un triángulo rectángulo.
        altura (float): que define la altura de un triángulo rectángulo.
    
    Raises:
        ValueError: Si la base o la altura no son un número positivo.
    """
    def __init__(self, base: float, altura: float) -> None:
        """
        Constructor de la clase TriánguloRectángulo.
        """
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser números positivos.")
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
    
    @property
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
        return self.base + self.altura + self.calcular_hipotenusa
    
    def determinar_tipo_triangulo(self) -> None:
        """
        Método que determina si un triángulo es:
        - Equilatero: si sus tres lados son iguales.
        - Escaleno: si sus tres lados son todos diferentes.
        - Escaleno: si dos de sus lados son iguales y el otro es diferente de los demás.
        """
        hipotenusa = self.calcular_hipotenusa
        if self.base == self.altura and self.altura == hipotenusa:
            return "Es un triángulo equilátero." # Todos sus lados son iguales.
        elif self.base != self.altura and self.altura != hipotenusa and self.base != hipotenusa:
            return "Es un triángulo escaleno." # Todos sus lados son diferentes.
        else:
            return "Es un triángulo isósceles." # De otra manera, es isósceles.
