from carrera_ciclistica.ciclista import Ciclista

class Equipo:
    """
    Esta clase denominada Equipo modela un equipo de ciclismo
    conformado por un vector de ciclistas. La clase tiene atributos como
    el nombre del equipo, el país del equipo y el tiempo total acumulado
    del equipo.
    
    Attributes:
        __nombre (str): Define el nombre del equipo de ciclismo.
        __total_tiempo (float): Define el tiempo total obtenido por el equipo.
        __pais (str): Define el país al que pertenece el equipo.
        lista_ciclistas (list[Ciclista]): define una lista de objetos ciclista.
    """    
    def __init__(self, nombre: str, pais: str) -> None:
        """
        Constructor de la clase Equipo.
        
        Args:
            nombre (str): Define el nombre del equipo.
            pais (str): Define el país del equipo.
        """
        self.__nombre = nombre
        self.__pais = pais
        self.__total_tiempo = 0.0 # Se inicializa el tiempo del equipo en cero
        self.lista_ciclistas: list[Ciclista] = [] # Se crea la lista de ciclistas que conforma el equipo
        
    @property
    def nombre_equipo(self) -> str:
        """
        Método que devuelve el nombre del equipo.
        
        Returns:
            str: El nombre del equipo.
        """
        return self.__nombre
    
    @nombre_equipo.setter
    def nombre_equipo(self, nombre: str) -> None:
        """
        Método que establece el nombre de un equipo.
        
        Args:
            nombre (str): Especifica el nombre de un equipo.
        """
        self.__nombre = nombre
        
    @property
    def __pais_equipo(self) -> str:
        """
        Método que devuelve el país del equipo.
        
        Returns:
            str: El país del equipo.
        """
        return self.__pais
    
    @__pais_equipo.setter
    def __pais_equipo(self, pais: str) -> None:
        """
        Método que establece el país de un equipo.
        
        Args:
            pais (str): Especifica el país de un equipo.
        """
        self.__pais = pais
        
    def anhadir_ciclista(self, ciclista: Ciclista) -> None:
        """
        Método que añade un ciclista a la lista de ciclistas de un equipo.
        """
        self.lista_ciclistas.append(ciclista)
        
    def listar_equipo(self) -> None:
        """
        Método que muestra en pantalla los nombres de los ciclistas que
        conforman un equipo.
        """
        # Se recorre la lista de ciclistas y para cada elemento se
        # imprime el nombre del ciclista
        for ciclista in self.lista_ciclistas:
            print(ciclista._nombre)
            
    def buscar_ciclista(self) -> None:
        """
        Método que busca un ciclista ingresado por teclado
        """
        nombre_ciclista = input("Ingrese el nombre del cilista: ")
        
        for ciclista in self.lista_ciclistas:
            if nombre_ciclista == ciclista._nombre:
                print(ciclista._nombre)
                
    def calcular_total_tiempo(self) -> None:
        """
        Método que calcula el tiempo total de un equipo acumulando el
        tiempo obtenido por cada uno de sus ciclistas.
        """
        for ciclista in self.lista_ciclistas:
            self.__total_tiempo += ciclista._tiempo_acumulado
            
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de un equipo.
        """
        print(f"\nNombre del equipo = {self.__nombre}")
        print(f"País = {self.__pais}")
        print(f"Total tiempo del equipo = {self.__total_tiempo}")
