from abc import ABC, abstractmethod

class Ciclista(ABC):
    """
    Esta clase abstracta denominada Ciclista posee como atributos un
    identificador, un nombre y un tiempo acumulado en una carrera
    ciclística.
    
    Attributes:
        __identificador (int): Define el identificador de un ciclista.
        __nombre (str): Define el nombre del ciclista.
        __tiempo_acumulado (int): Define el tiempo acumulado de un ciclista.
        __posicion_general (int): Define la posición general de un ciclista.
    """
    def __init__(self, identificador: int, nombre: str) -> None:
        """
        Constructor de la clase Ciclista.
        
        Args:
            identificador (int): Define el identificador de un ciclista.
            nombre (str): Define el nombre completo de un ciclista.
        """
        self.__identificador = identificador
        self.__nombre = nombre
        self.__tiempo_acumulado: int = 0
        self.__posicion_general: int = 0
    
    @abstractmethod
    def _imprimir_tipo(self) -> str:
        """
        Método abstracto que muestra en pantalla el tipo específico de un ciclista.
        
        Returns:
            str: Tipo de ciclista
        """
        pass
    
    @property
    def _identificador(self) -> int:
        """
        Método que devuelve el identificador de un ciclista.
        
        Returns:
            int: El identificador de un ciclista.
        """
        return self.__identificador
    
    @_identificador.setter
    def _identificador(self, identificador: int) -> None:
        """
        Método que establece el identificador de un ciclista.
        
        Args:
            identificador (int): Especifica el identificador de un ciclista
        """
        self.__identificador = identificador
        
    @property
    def _nombre(self) -> str:
        """
        Método que devuelve el nombre de un ciclista.
        
        Returns:
            str: El nombre de un ciclista
        """
        return self.__nombre
    
    @_nombre.setter
    def _nombre(self, nombre: str) -> None:
        """
        Método que establece el nombre de un ciclista.
        
        Args:
            nombre (str): Especifica el nombre de un ciclista
        """
        self.__nombre = nombre
    
    @property
    def _posicion_general(self) -> int:
        """
        Método que devuelve el puesto que ocupa un ciclista en la
        posición general de la competencia.
        
        Returns:
            int: El puesto del ciclista en la posición general.
        """
        return self.__posicion_general
    
    @_posicion_general.setter
    def _posicion_general(self, posicion_general: int) -> None:
        """
        Método que establece el puesto que ocupa un ciclista en la
        posición general.
        
        Args:
            posicion_general (int): Especifica el puesto que ocupa un ciclista 
            en la posición general.
        """
        self.__posicion_general = posicion_general
        
    @property
    def _tiempo_acumulado(self) -> int:
        """
        Método que devuelve el tiempo acumulado de un ciclista en una competencia.
        
        Returns:
            int: El tiempo acumulado de un ciclista en una competencia.
        """
        return self.__tiempo_acumulado
    
    @_tiempo_acumulado.setter
    def _tiempo_acumulado(self, tiempo_acumulado: int) -> None:
        """
        Método que establece el tiempo acumulado por un ciclista.
        
        Args:
            int: Especifica el tiempo acumulado por un ciclista.
        """
        self.__tiempo_acumulado = tiempo_acumulado
        
    def _imprimir(self) -> None:
        """
        Método muestra en pantalla los datos de un ciclista.
        """
        print(f"\nIdentificador = {self.__identificador}")
        print(f"Nombre = {self.__nombre}")
        print(f"Tiempo Acumulado = {self.__tiempo_acumulado}")
