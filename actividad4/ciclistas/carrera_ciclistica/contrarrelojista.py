from carrera_ciclistica.ciclista import Ciclista

class Contrarrelojista(Ciclista):
    """
    Esta clase denominada Contrarrelojista es un tipo de Ciclista que se
    encuentra mejor adaptado a las etapas contrarreloj. Posee un nuevo
    atributo: su velocidad máxima.
    
    Attributes:
        __velocidad_maxima (float): Define la velocidad máxima de un contrarrelojista.
    """
    def __init__(self,
                identificador: int,
                nombre: str,
                velocidad_maxima: float) -> None:
        """
        Constructor de la clase Escalador.
        
        Args:
            identificador (int): Define el identificador de un contrarrelojista.
            nombre (str): Define el nombre completo de un contrarrelojista.
            velocidad_maxima (float): Define la velocidad máxima de un contrarrelojista.
        """
        super().__init__(identificador, nombre)
        self.__velocidad_maxima = velocidad_maxima
    
    @property
    def _velocidad_maxima(self) -> float:
        """
        Método que devuelve la velocidad máxima de un contrarrelojista.
        
        Returns:
            float: La velocidad máxima de un contrarrelojista.
        """
        return self.__velocidad_maxima
    
    @_velocidad_maxima.setter
    def _velocidad_maxima(self, velocidad_maxima: float) -> None:
        """
        Método que establece la velocidad máxima de un contrarrelojista.
        
        Args:
            velocidad_maxima (float): Especifica la velocidad máxima de un contrarrelojista.
        """
        self.__velocidad_maxima = velocidad_maxima
        
    def _imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un contrarrelojista.
        """
        super()._imprimir()
        print(f"Velocidad máxima = {self.__velocidad_maxima}")
    
    def _imprimir_tipo(self) -> str:
        """
        Método que devuelve el tipo de ciclista.
        
        Returns:
            str: Un valor String con el texto "Es un constrarrelojista"
        """
        return "Es un constrarrelojista"
