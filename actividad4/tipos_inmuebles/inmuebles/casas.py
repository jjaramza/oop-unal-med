from inmuebles.inmueble_vivienda import InmuebleVivienda

class Casa(InmuebleVivienda):
    """
    Esta clase denominada Casa modela un tipo específico de inmueble
    destinado para la vivienda con atributos como el número de pisos
    que tiene una casa.
    
    Attributes:
        _numero_pisos (int): el número de pisos que tiene una casa
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int) -> None:
        """
        Constructor de la clase Casa
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de una casa
            area (int): el área de una casa
            direccion (str): la dirección donde se encuentra localizado una casa
            numero_habitaciones (int): el número de habitaciones que tiene una casa
            numero_banos (int): el número de baños que tiene una casa
            numero_pisos (int): el número de pisos que tiene una casa
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        self._numero_pisos = numero_pisos
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una casa
        """
        # Invocar al método imprimir de la clase padre
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")


class CasaRural(Casa):
    """
    Esta clase denominada CasaRural modela un tipo específico de casa
    ubicada en el sector rural
    
    Attributes:
        VALOR_AREA (float): Constante que identifica el valor por área para una casa rural
        _distancia_cabecera (int): la distancia a la que se encuentra la casa rural de la cabecera municipal
        _altitud (int): la altitud a la que se encuentra una casa rural
    """
    VALOR_AREA: float = 1500000.0 # El valor por área para una casa rural
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 distancia_cabecera: int, altitud: int) -> None:
        """
        Constructor de la clase CasaRural
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de una casa rural
            area (int): el área de una casa rural
            direccion (str): la dirección donde se encuentra localizado una casa rural
            numero_habitaciones (int): el número de habitaciones que tiene una casa rural
            numero_banos (int): el número de baños que tiene una casa rural
            numero_pisos (int): el número de pisos que tiene una casa rural
            distancia_cabecera (int): la distancia de la casa rural a la cabecera municipal
            altitud (int): la altitud sobre el nivel del mar en que se encuentra una casa rural
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud
    
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una casa rural
        """
        # Invocar al método imprimir de la clase padre
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self._distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros")


class CasaUrbana(Casa):
    """
    Esta clase denominada CasaUrbana modela un tipo específico de casa
    destinada para la vivienda localizada en el sector urbano.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int) -> None:
        """
        Constructor de la clase CasaUrbana
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de una casa urbana
            area (int): el área de una casa urbana
            direccion (str): la dirección donde se encuentra localizado una casa urbana
            numero_habitaciones (int): el número de habitaciones que tiene una casa urbana
            numero_banos (int): el número de baños que tiene una casa urbana
            numero_pisos (int): el número de pisos que tiene una casa urbana
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
    
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una casa urbana
        """
        # Invocar al método imprimir de la clase padre
        super().imprimir()


class CasaConjuntoCerrado(CasaUrbana):
    """
    Esta clase denominada CasaConjuntoCerrado modela un tipo
    específico de casa urbana que se encuentra en un conjunto cerrado
    con atributos como el valor por área, valor de la administración y
    valores booleanos para especificar si tiene piscina y campos deportivos.
    
    Attributes:
        VALOR_AREA (float): Constante que define el valor por área de una casa en conjunto cerrado
        _valor_administracion (int): el valor de administración de una casa en conjunto cerrado
        _tiene_piscina (bool): si una casa en conjunto cerrado tiene piscina
        _tiene_campos_deportivos (bool): si una casa en conjunto cerrado tiene campos deportivos
    """
    VALOR_AREA: float = 2500000.0 # El valor por área de una casa en conjunto cerrado
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 valor_administracion: bool, tiene_piscina: bool, tiene_campos_deportivos: bool) -> None:
        """
        Constructor de la clase CasaConjuntoCerrado
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de una casa en conjunto cerrado
            area (int): el área de una casa en conjunto cerrado
            direccion (str): la dirección donde se encuentra localizado una casa en conjunto cerrado
            numero_habitaciones (int): el número de habitaciones que tiene una casa en conjunto cerrado
            numero_banos (int): el número de baños que tiene una casa en conjunto cerrado
            numero_pisos (int): el número de pisos que tiene una casa en conjunto cerrado
            valor_administracion (int): el valor de administración de una casa en conjunto cerrado
            tiene_piscina (bool): si una casa en conjunto cerrado tiene piscina
            tiene_campos_deportivos (bool): si una casa en conjunto cerrado tiene campos deportivos
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._valor_administracion = valor_administracion
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una casa en conjunto cerrado
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
        print(f"Valor de la administración = {self._valor_administracion}")
        print(f"¿Tiene piscina? = {self._tiene_piscina}")
        print(f"¿Tiene campos deportivos? = {self._tiene_campos_deportivos}")


class CasaIndependiente(CasaUrbana):
    """
    Esta clase denominada CasaIndependiente modela un tipo específico
    de casa urbana que no está en conjunto cerrado y es completamente
    independiente de otras casas. Tiene un atributo estático para
    especificar un valor del área del inmueble.
    
    Attributes:
        VALOR_AREA (float): Constante que define el valor por área de una casa independiente
    """
    VALOR_AREA: float = 3000000.0 # El valor por área de una casa independiente
    
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int) -> None:
        """
        Constructor de la clase CasaIndependiente
        
        Args:
            identificador_inmobiliario (int): identificador inmobiliario de una casa independiente
            area (int): el área de una casa independiente
            direccion (str): la dirección donde se encuentra localizado una casa independiente
            numero_habitaciones (int): el número de habitaciones que tiene una casa independiente
            numero_banos (int): el número de baños que tiene una casa independiente
            numero_pisos (int): el número de pisos que tiene una casa independiente
        """
        # Invoca al constructor de la clase padre
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una casa independiente
        """
        # Invoca al método imprimir de la clase padre
        super().imprimir()
