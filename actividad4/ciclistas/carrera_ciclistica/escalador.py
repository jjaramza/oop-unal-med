from carrera_ciclistica.ciclista import Ciclista

class Escalador(Ciclista):
    """
    Esta clase denominada Escalador es un tipo de Ciclista que se
    encuentra mejor adaptado y se destaca cuando las carreteras son en
    ascenso, ya sea en colinas o montañas. Posee nuevos atributos como
    su aceleración promedio y el grado de rampa que soporta.
    
    Attributes:
        __aceleracion_promedio (float): Define la acelaración promedio de un escalador.
        __grado_rampa (float): Define el grado de rampa soportado por un escalador.
    """
    def __init__(self,
                identificador: int,
                nombre: str,
                aceleracion_promedio: float,
                grado_rampa: float) -> None:
        """
        Constructor de la clase Escalador.
        
        Args:
            identificador (int): Define el identificador de un escalador.
            nombre (str): Define el nombre completo de un escalador.
            aceleracion_promedio (float): Define la acelaración promedio de un escalador.
            grado_rampa (float): Define el grado de rampa de un escalador.
        """
        super().__init__(identificador, nombre)
        self.__aceleracion_promedio = aceleracion_promedio
        self.__grado_rampa = grado_rampa
    
    @property
    def _aceleracion_promedio(self) -> float:
        """
        Método que devuelve la aceleración promedio de un escalador.
        
        Returns:
            float: La aceleración promedio de un escalador
        """
        return self.__aceleracion_promedio
    
    @_aceleracion_promedio.setter
    def _aceleracion_promedio(self, aceleracion_promedio: float) -> None:
        """
        Método que establece la aceleración promedio de un escalador.
        
        Args:
            aceleracion_promedio (float): Especifica la aceleración promedio de un escalador.
        """
        self.__aceleracion_promedio = aceleracion_promedio
        
    @property
    def _grado_rampa(self) -> float:
        """
        Método que devuelve el grado de rampa soportado de un escalador.
        
        Returns:
            float: El grado de rampa soportado de un escalador
        """
        return self.__grado_rampa
    
    @_grado_rampa.setter
    def _grado_rampa(self, grado_rampa: float) -> None:
        """
        Método que establece el grado de rampa soportado por un escalador.
        
        Args:
            grado_rampa (float): Especifica el grado de rampa soportado por un escalador.
        """
        self.__grado_rampa = grado_rampa
    
    def _imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un escalador.
        """
        super()._imprimir()
        print(f"Aceleración promedio = {self.__aceleracion_promedio}")
        print(f"Grado de rampa = {self.__grado_rampa}")
    
    def _imprimir_tipo(self) -> str:
        """
        Método que devuelve el tipo de ciclista.
        
        Returns:
            str: Un valor String con el texto "Es un escalador"
        """
        return "Es un escalador"
    