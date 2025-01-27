from inmuebles.inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    """
    Esta clase denominada InmuebleVivienda modela un inmueble
    destinado para la vivienda con atributos como el número de
    habitaciones y el número de baños que posee
    
    Attributes:
        _numero_habitaciones (int): el número de habitaciones de un inmueble para vivienda
        _numero_banos (int): el número de baños de un inmueble para vivienda
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int) -> None:
        """
        Constructor de la clase InmuebleVivienda
        
        Args:
            identificador_inmobiliario (int): identificador de un inmueble para vivienda
            area (int): el área de un inmueble para la vivienda
            direccion (str): la dirección donde se encuentra localizado un inmueble para la vivienda
            numero_habitaciones (int): el número de habitaciones que tiene un inmueble para la vivienda
            numero_banos (int): el número de baños que tiene un inmueble para la vivienda
        """
        # Invoca el constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion)
        self._numero_habitaciones = numero_habitaciones
        self._numero_banos = numero_banos
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un inmueble para la vivienda
        """
        # Invocar al método imprimir de la clase padre
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_banos}")
    