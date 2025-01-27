from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Esta clase abstracta denominada Animal modela un animal genérico
    que cuenta con atributos como un sonido, alimentos que consume,
    un hábitat y un nombre científico.
    
    Attributes:
        _sonido (str): Identifica el sonido emitido por un animal.
        _alimentos (str): Identifica los alimentos que consume un animal.
        _habitat (str): Identifica el hábitat de un animal.
        _nombre_cientifico (str): Identifica el nombre científico de un animal.
    """
    _sonido: str = ""
    _alimentos: str = ""
    _habitat: str = ""
    _nombre_cientifico: str = ""
    
    @abstractmethod
    def get_nombre_cientifico(self) -> str:
        """
        Método abstracto que permite obtener el nombre científico del animal.
        
        Returns:
            str: El nombre científico del animal.
        """
        pass
        
    @abstractmethod
    def get_sonido(self) -> str:
        """
        Método abstracto que permite obtener el sonido producido por el animal.
        
        Returns:
            str: El sonido producido por el animal.
        """
        pass
    
    @abstractmethod
    def get_alimentos(self) -> str:
        """
        Método abstracto que permite obtener los alimentos que consume un animal.
        
        Returns:
            str: Los alimentos que consume el animal.
        """
        pass
    
    @abstractmethod    
    def get_habitat(self) -> str:
        """
        Método abstracto que permite obtener el hábitat de un animal.
        
        Returns:
            str: El hábitat del animal.
        """
        pass


class Canido(Animal):
    """
    Esta clase abstracta denominada Cánido modela esta familia de
    animales. Es una subclase de Animal.
    """
    pass
    

class Felino(Animal):
    """
    Esta clase abstracta denominada Felino modela esta familia de
    animales. Es una subclase de Animal.
    """
    pass
