from carrera_ciclistica.ciclista import Ciclista

class Velocista(Ciclista):
    """
    Esta clase denominada Velocista es un tipo de Ciclista caracterizado
    por poseer gran potencia y alta velocidad punta en esfuerzos cortos.
    Posee nuevos atributos como la potencia promedio y la velocidad promedio.
    
    Attributes:
        __potencia_promedio (float): Define la potencia promedio de un velocista.
        __velocidad_promedio (float): Define la velocidad promedio de un velocista.
    """
    def __init__(self, 
                identificador: int, 
                nombre: str,
                potencia_promedio: float,
                velocidad_promedio: float) -> None:
        """
        Constructor de la clase Velocista.
        
        Args:
            identificador (int): Define el identificador de un velocista.
            nombre (str): Define el nombre completo de un velocista.
            potencia_promedio (float): Define la potencia promedio de un velocista.
            velocidad_promedio (float): Define la velocidad promedio de un velocista.
        """
        super().__init__(identificador, nombre)
        self.__potencia_promedio = potencia_promedio
        self.__velocidad_promedio = velocidad_promedio
        
    @property
    def _potencia_promedio(self) -> float:
        """
        Método que devuelve la potencia promedio de un velocista.
        
        Returns:
            float: La potencia promedio de un velocista.
        """
        return self.__potencia_promedio
    
    @_potencia_promedio.setter
    def _potencia_promedio(self, potencia_promedio: float):
        """
        Método que establece la potencia promedio de un velocista.
        
        Args:
            potencia_promedio (float): Especifica la potencia promedio de un velocista
        """
        self.__potencia_promedio = potencia_promedio
    
    @property
    def _velocidad_promedio(self) -> float:
        """
        Método que devuelve la velocidad promedio de un velocista.
        
        Returns:
            float: La velocidad promedio de un velocista.
        """
        return self.__velocidad_promedio
    
    @_velocidad_promedio.setter
    def _velocidad_promedio(self, velocidad_promedio: float) -> None:
        """
        Método que establece la velocidad promedio de un velocista.
        
        Args:
            velocidad_promedio (float): Especifica la velocidad promedio de un velocista.
        """
        self.__velocidad_promedio = velocidad_promedio
        
    def _imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un velocista.
        """
        super()._imprimir()
        print(f"Potencia promedio = {self.__potencia_promedio}")
        print(f"Velocidad promedio = {self.__velocidad_promedio}")
    
    def _imprimir_tipo(self) -> str:
        """
        Método que devuelve el tipo de ciclista.
        
        Returns:
            str: Un valor String con el texto "Es un velocista"
        """
        return "Es un velocista"
