from enum import Enum

class ResultadoComparacion(Enum):
    """
    Representa los posibles resultados de comparar dos números enteros.

    Attributes:
        MAYOR (str): Indica que el primer número es mayor que el segundo.
        IGUAL (str): Indica que los dos números son iguales.
        MENOR (str): Indica que el primer número es menor que el segundo.
    """
    MAYOR = "mayor"
    IGUAL = "igual"
    MENOR = "menor"


class ComparacionNumero:
    """
    Esta clase define objetos de tipo de ComparacionNumero la cual tiene como
    atributos dos números enteros.

    Attributes:
        valor_a (int): Primer valor numérico
        valor_b (int): Segundo valor numérico
    """
    def __init__(self, valor_a: int, valor_b: int) -> None:
        """
        Constructor de la clase ComparacionNumero.

        Args:
            valor_a (int): Parámetro que define el primer valor numérico
            valor_b (int): Parámetro que define el segundo valor numérico
        """
        self.valor_a = valor_a
        self.valor_b = valor_b

    def comparar(self) -> ResultadoComparacion:
        """
        Compara dos números enteros y devuelve el resultado como un enumerado.

        Returns:
            ResultadoComparacion: Resultado de la comparación.
        """
        if self.valor_a > self.valor_b:
            return ResultadoComparacion.MAYOR
        elif self.valor_a == self.valor_b:
            return ResultadoComparacion.IGUAL
        else:
            return ResultadoComparacion.MENOR

    def comparar_numeros(self) -> str:
        """
        Compara dos números enteros y devuelve una cada de texto.

        Returns:
            str: Cadena que indica si el número A es mayor, igual o menor que el número B.
        """
        resultado = self.comparar()
        return f"{self.valor_a} es {resultado} que {self.valor_b}"