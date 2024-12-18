# Ejercicio resuelto No 13 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Venta:
    
    def __init__(self, valor_compra: int, color_bolita: str) -> None:
        self.valor_compra = valor_compra
        self.color_bolita = color_bolita
        
    def calculo_compra_descuento(self) -> float:
        """Se calcula el valor final de compra de acuerdo al descuento obtenido."""
        color = self.color_bolita.upper()
        porc_descuento: int
        if color == "BLANCO":
            porc_descuento = 0
        elif color == "VERDE":
            porc_descuento = 10
        elif color == "AMARILLO":
            porc_descuento = 25
        elif color == "AZUL":
            porc_descuento = 50
        else:
            porc_descuento = 100
        return self.valor_compra * (1 - porc_descuento / 100)
    
    def mostrar_valor_pagar(self) -> str:
        """Se muestra el valor final a pagar."""
        valor = f"{'{:,.0f}'.format(self.calculo_compra_descuento())}"
        return f"El cliente debe pagar ${valor.replace(",", ".")}"
    

def main() -> None:
    # Se solicita los datos por pantalla
    valor = int(input("Ingrese el valor de la compra: "))
    color = input("Ingrese el valor de la bolita: ")
    
    # Se crea el objeto de clase
    compra = Venta(valor_compra=valor, color_bolita=color)
    
    # Se muestra la información
    print(compra.mostrar_valor_pagar())
    

if __name__ == "__main__":
    main()
