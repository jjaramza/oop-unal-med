from animales.animal import Canido

class Perro(Canido):
    """
    Esta clase concreta denominada Perro es una subclase de Cánido.
    """
    
    def get_sonido(self) -> str:
        """
        Método que devuelve un String con el sonido de un perro.
        
        Returns:
            str: Un valor con el sonido de un perro: "Ladrido".
        """
        return "Ladrido"
    
    def get_alimentos(self) -> str:
        """
        Método que devuelve un String con los alimentos de un perro.
        
        Returns:
            str: Un valor con la alimentación de un perro: "Carnívoro".
        """
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        """
        Método que devuelve un String con el hábitat de un perro.
        
        Returns:
            str: Un valor con el hábitat de un perro: "Doméstico".
        """
        return "Doméstico"
    
    def get_nombre_cientifico(self) -> str:
        """
        Método que devuelve un String con el nombre científico de un perro.
        
        Returns:
            str: Un valor con el nombre científico de un perro: "Canis lupus familiaris"
        """
        return "Canis lupus familiaris"


class Lobo(Canido):
    """
    Esta clase concreta denominada Lobo es una subclase de Cánido.
    """
    
    def get_sonido(self) -> str:
        """
        Método que devuelve un String con el sonido de un lobo.
        
        Returns:
            str: Un valor con el sonido de un lobo: "Aullido".
        """
        return "Aullido"
    
    def get_alimentos(self) -> str:
        """
        Método que devuelve un String con los alimentos de un lobo.
        
        Returns:
            str: Un valor con la alimentación de un lobo: "Carnívoro".
        """
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        """
        Método que devuelve un String con el hábitat de un lobo.
        
        Returns:
            str: Un valor con el hábitat de un lobo: "Bosque".
        """
        return "Bosque"
    
    def get_nombre_cientifico(self) -> str:
        """
        Método que devuelve un String con el nombre científico de un lobo.
        
        Returns:
            str: Un valor con el nombre científico de un lobo: "Canis lupus"
        """
        return "Canis lupus"
