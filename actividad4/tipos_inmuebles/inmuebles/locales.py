from inmueble import Inmueble
from enum import Enum


class TipoLocal(Enum):
    """
    Tipo de inmueble especificado como un valor enumerado (INTERNO o CALLE)
    """
    INTERNO = "INTERNO"
    CALLE = "CALLE"


class Local(Inmueble):
    """
    Esta clase denominada Local modela un tipo específico de inmueble
    que no está destinado para la vivienda que tiene como atributos un
    tipo que especifica si es un local interno o que da a la calle.
    
    Attributes:
        _tipo_local (TipoLocal): identifica el tipo de inmueble 
    """
    def __init__(self, identificador_inmobiliario: int, area: int,
                 direccion: str, tipo_local: TipoLocal) -> None:
        """
        Constructor de la clase Local
        
        Args:
            identificador_inmobiliario (int): define el identificador de un local
            area (int): define el área de un local
            direccion (str): define la dirección donde se encuentra localizado un local
            tipo_local (TipoLocal): define el tipo de local (interno o que da a la calle)
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion)
        self._tipo_local = tipo_local
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un local
        """
        super().imprimir()
        print(f"Tipo de local = {self._tipo_local}")


class LocalComercial(Local):
    """
    Esta clase denominada LocalComercial modela un tipo específico de
    Local destinado para un uso comercial con atributos como el valor
    por área y el centro comercial al cual pertenece.
    
    Attributes:
        VALOR_HORA (float): Constante que identifica el valor por área de un local comercial
        _centro_comercial (str): el centro comercial donde está ubicado el local comercial
    """
    VALOR_HORA: float = 3000000.0 # El valor por área de un local comercial
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, centro_comercial: str) -> None:
        """
        Constructor de la clase LocalComercial
        
        Args:
            identificador_inmobiliario (int): define el identificador de un local comercial
            area (int): define el área de un local comercial
            direccion (str): define la dirección donde se encuentra localizado un local comercial
            tipo_local (TipoLocal): define el tipo de local comercial (interno o que da a la calle)
            centro_comercial (str): el centro comercial donde está ubicado el local comercial
        """
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._centro_comercial = centro_comercial
        
    def imprimit(self) -> None:
        """
        Método que muestra en pantalla los datos de un local comercial
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
        print(f"Centro comercial = " + self._centro_comercial)


class Oficina(Local):
    """
    Esta clase denominada Oficina modela un tipo específico de local
    con atributos como el valor por área y un valor booleano para
    determinar si pertenece o no al gobierno.
    
    Attributes:
        VALOR_HORA (float): Constante que identifica el valor por área de una oficina
        _es_gobierno (bool): si una oficina pertenece o no al gobierno
    """
    VALOR_HORA: float = 3500000.0 # El valor por área de una oficina
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, es_gobierno: bool) -> None:
        """
        Constructor de la clase Oficina
        
        Args:
            identificador_inmobiliario (int): define el identificador de una oficina
            area (int): define el área de una oficina
            direccion (str): define la dirección donde se encuentra localizado una oficina
            tipo_local (TipoLocal): define el tipo de una oficina (interno o que da a la calle)
            es_gobierno (bool): si la oficina es del gobierno o no
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._es_gobierno = es_gobierno
    
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una oficina
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
        print(f"Es oficina gubernamental = {self._es_gobierno}")
