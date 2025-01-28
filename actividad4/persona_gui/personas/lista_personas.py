from personas.persona import Persona

class ListaPersonas:
    """
    Esta clase denominada ListaPersonas define una lista de Personas.
    """
    def __init__(self):
        """
        Constructor de la clase ListaPersonas.
        """
        self.lista_personas = []

    def añadir_persona(self, persona: Persona):
        """
        Método que permite agregar una persona a la lista de personas.
        
        Args:
            persona (Persona): Define la persona a agregar a lista de personas.
        """
        self.lista_personas.append(persona)

    def eliminar_persona(self, indice: int):
        """
        Método que permite eliminar una persona de la lista de personas.
        
        Args:
            indice (int): Define la posición a eliminar en la lista de personas.
        """
        if 0 <= indice < len(self.lista_personas):
            self.lista_personas.pop(indice)

    def borrar_lista(self):
        """Método que permite eliminar todos los elementos de la lista de personas."""
        self.lista_personas.clear()
