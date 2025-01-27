from animales.animal import Felino

class Leon(Felino):
    """
    Esta clase concreta denominada León es una subclase de Felino.
    """
    
    def get_sonido(self) -> str:
        """
        Método que devuelve un String con el sonido de un león.
        
        Returns:
            str: Un valor con el sonido de un león: "Rugido".
        """
        return "Rugido"
    
    def get_alimentos(self) -> str:
        """
        Método que devuelve un String con los alimentos de un león.
        
        Returns:
            str: Un valor con la alimentación de un león: "Carnívoro".
        """
        return "Carnívoro"
    
    def get_habitat(self) -> str:
        """
        Método que devuelve un String con el hábitat de un león.
        
        Returns:
            str: Un valor con el hábitat de un león: "Praderas".
        """
        return "Praderas"
    
    def get_nombre_cientifico(self) -> str:
        """
        Método que devuelve un String con el nombre científico de un león.
        
        Returns:
            str: Un valor con el nombre científico de un león: "Panthera leo"
        """
        return "Panthera leo"


class Gato(Felino):
    """
    Esta clase concreta denominada Gato es una subclase de Felino.
    """
    
    def get_sonido(self) -> str:
        """
        Método que devuelve un String con el sonido de un gato.
        
        Returns:
            str: Un valor con el sonido de un gato: "Maullido".
        """
        return "Maullido"
    
    def get_alimentos(self) -> str:
        """
        Método que devuelve un String con los alimentos de un gato.
        
        Returns:
            str: Un valor con la alimentación de un gato: "Ratones".
        """
        return "Ratones"
    
    def get_habitat(self) -> str:
        """
        Método que devuelve un String con el hábitat de un gato.
        
        Returns:
            str: Un valor con el hábitat de un gato: "Doméstico".
        """
        return "Doméstico"
    
    def get_nombre_cientifico(self) -> str:
        """
        Método que devuelve un String con el nombre científico de un gato.
        
        Returns:
            str: Un valor con el nombre científico de un gato: "Felis silvestris catus"
        """
        return "Felis silvestris catus"
