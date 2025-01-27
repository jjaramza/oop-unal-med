class Inmueble:
    """
    Esta clase denominada Inmueble modela un inmueble que posee
    como atributos un identificador, un área, una dirección y un precio
    de venta. Es la clase raíz de una jerarquía de herencia
    
    Attributes:
        _identificador_inmobiliario (int): identificador inmobiliario de un inmueble
        _area (int): identifica el área de un inmueble
        _direccion (str): identifica la dirección de un inmueble
        _precio_venta (float): identifica el precio de venta de un inmueble
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str) -> None:
        """
        Constructor de la clase Inmueble
        
        Args:
            identificador_inmobiliario (int): define el identificador de un inmueble
            area (int): define el área de un inmueble
            direccion (str): define la dirección donde se encuentra localizado un inmueble
        """
        self._identificador_inmobiliario: int = identificador_inmobiliario
        self._area: int = area
        self._direccion: str = direccion
        self._precio_venta: float = 0.0
        
    def calcular_precio_venta(self, valor_area: float) -> float:
        """
        Método que a partir del valor del área de un inmueble, calcula su
        precio de venta
        
        Args:
            valor_area (float): El valor unitario por área de un determinado inmueble
            
        Returns:
            float: Precio de venta del inmueble
        """
        self._precio_venta = self._area * valor_area
        return self._precio_venta
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un inmueble
        """
        print(f"\nIdentificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Área = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = $ {self._precio_venta}")
