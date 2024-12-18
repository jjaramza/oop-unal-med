from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from triangulo_rectangulo import TrianguloRectangulo

class PruebaFiguras:
    """
    Esta clase prueba diferentes acciones realizadas en diversas figuras geométricas.
    """
    
    @staticmethod
    def main() -> None:
        """
        Método main que crea un círculo, un rectángulo, un cuadrado y
        un triángulo rectángulo. Para cada uno de estas figuras geométricas,
        se calcula su área y perímetro.
        """
        figura1 = Circulo(radio=2)
        figura2 = Rectangulo(base=1, altura=2)
        figura3 = Cuadrado(lado=3)
        figura4 = TrianguloRectangulo(base=3, altura=5)
        
        print(f"El área del círculo es = {figura1.calcular_area()}")
        print(f"El perímetro del círculo es = {figura1.calcular_perimetro()}\n")
        
        print(f"El área del rectángulo es = {figura2.calcular_area()}")
        print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}\n")
        
        print(f"El área del cuadrado es = {figura3.calcular_area()}")
        print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}\n")
        
        print(f"El área del triángulo es = {figura4.calcular_area()}")
        print(f"El perímetro del triángulo es = {figura4.calcular_perimetro()}")
        figura4.determinar_tipo_triangulo()


if __name__ == "__main__":
    PruebaFiguras.main()
