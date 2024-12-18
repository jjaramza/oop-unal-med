# Ejercicio resuelto No 7 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class ComparacionNumero:
    
    def __init__(self, valor_a: int, valor_b: int) -> None:
        self.valor_a = valor_a
        self.valor_b = valor_b
        
    def comparar_numeros(self) -> str:
        mensaje = ""
        if self.valor_a > self.valor_b:
            mensaje = f"{self.valor_a} es mayor que {self.valor_b}"
        elif self.valor_a == self.valor_b:
            mensaje = f"{self.valor_a} es igual a {self.valor_b}"
        else:
            mensaje = f"{self.valor_a} es menor que {self.valor_b}"
        return mensaje
    

def main() -> None:
    # Se solicita los números al usuario
    numero_a = int(input("Ingrese un número: "))
    numero_b = int(input("Ingrese otro número: "))
    
    # Se crea un objeto de la case MayorQue
    comparar = ComparacionNumero(numero_a, numero_b)
    
    # Se muestra el mensaje de quién es mayor, menor o igual
    print(comparar.comparar_numeros())
    
    
if __name__ == "__main__":
    main()
