from animales.canidos import Perro, Lobo
from animales.felinos import Leon, Gato

class Prueba:
    """
    Esta clase prueba diferentes animales y sus métodos.
    """

    @staticmethod
    def main():
        """
        Método main que crea un array de varios animales y para cada uno
        muestra en pantalla su nombre científico, su sonido, alimentos y
        hábitat
        """
        animales = [Gato(), Perro(), Lobo(), Leon()]
        
        for animal in animales:
            print(animal.get_nombre_cientifico())
            print(f"Sonido: {animal.get_sonido()}")
            print(f"Alimentos: {animal.get_alimentos()}")
            print(f"Hábitat: {animal.get_habitat()}")
            print()
            

if __name__ == '__main__':
    Prueba.main()
