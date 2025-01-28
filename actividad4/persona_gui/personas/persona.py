class Persona:
    """
    Esta clase denominada Persona modela una persona que cuenta con
    los atributos: nombre, apellidos, teléfono y dirección.
    """
    def __init__(self, nombre: str, apellidos: str, telefono: str, direccion: str):
        """
        Constructor de la clase Persona.
        
        Args:
            nombre (str): Define el nombre de una persona.
            apellidos (str): Define los apellidos de una persona.
            telefono (str): Define el teléfono de una persona.
            direccion (str): Define la dirección de una persona.
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
