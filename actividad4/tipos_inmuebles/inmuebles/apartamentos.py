from inmuebles.inmueble_vivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    """
    Esta clase denominada Apartamento modela un tipo de inmueble
    específico destinado para la vivienda.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int) -> None:
        """
        Constructor de la clase Apartamento
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de un apartamento
            area (int): el área de un apartamento
            direccion (str): la dirección donde se encuentra localizado un apartamento
            numero_habitaciones (int): el número de habitaciones que tiene un apartamento
            numero_banos (int): el número de baños que tiene un apartamento
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un apartamento
        """
        # Invocar al método imprimir de la clase padre
        super().imprimir()


class ApartamentoFamiliar(Apartamento):
    """
    Esta clase denominada ApartamentoFamiliar modela un tipo
    específico de apartamento con atributos como el valor por área y el
    valor de la administración.
    
    Attributes:
        VALOR_AREA (float): el valor por área de un apartamento familiar
        _valor_administracion (int): el valor de la administración de un apartamento familiar
    """
    VALOR_AREA: float = 2000000.0 # El valor por área de un apartamento familiar
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, valor_administracion: str) -> None:
        """
        Constructor de la clase ApartamentoFamiliar
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de un apartamento familiar
            area (int): el área de un apartamento familiar
            direccion (str): la dirección donde se encuentra localizado un apartamento familiar
            numero_habitaciones (int): el número de habitaciones que tiene un apartamento familiar
            numero_banos (int): el número de baños que tiene un apartamento familiar
            valor_administracion (int): el valor de la administración de un apartamento familiar
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        self._valor_administracion = valor_administracion
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un apartamento familiar
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
        print(f"Valor de la administración = $ {self._valor_administracion}")


class Apartaestudio(Apartamento):
    """
    Esta clase denominada Apartaestudio modela un tipo específico de
    apartamento que tiene una sola habitación.
    
    Attributes:
        VALOR_AREA (float): Constante que identifica el valor por área de un apartaestudio
    """
    VALOR_AREA: float = 1500000.0 # El valor por área de un apartaestudio
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int = 1, numero_banos: int = 1) -> None:
        """
        Constructor de la clase Apartaestudio
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de un apartaestudio
            area (int): el área de un apartaestudio
            direccion (str): la dirección donde se encuentra localizado un apartaestudio
            numero_habitaciones (int): el número de habitaciones que tiene un apartaestudio
            numero_banos (int): el número de baños que tiene un apartaestudio
        """
        # Invoca al constructor de la clase padre
        # Los apartaestudios tienen una sola habitación y un solo baño
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un apartaestudio
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
