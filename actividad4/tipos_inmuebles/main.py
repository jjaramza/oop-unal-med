from inmuebles.apartamentos import ApartamentoFamiliar, Apartaestudio


class Prueba:
    """
    Esta clase prueba diferentes inmuebles, se calcula su precio de
    acuerdo al área y se muestran sus datos en pantalla
    """
    
    @staticmethod
    def main():
        """
        Método main que crea dos inmuebles, calcula su precio de
        acuerdo al área y se muestran sus datos en pantalla
        """
        apto1 = ApartamentoFamiliar(
            identificador_inmobiliario=103067,
            area=120,
            direccion="Avenida Santander 45-45",
            numero_habitaciones=3,
            numero_banos=2,
            valor_administracion=200000
        )
        print("\nDatos apartamento familiar")
        apto1.calcular_precio_venta(valor_area=apto1.VALOR_AREA)
        apto1.imprimir()
        
        aptestudio1 = Apartaestudio(
            identificador_inmobiliario=12354,
            area=50,
            direccion="Avenida Caracas 30-15"
        )
        print("\nDatos apartaestudio")
        aptestudio1.calcular_precio_venta(valor_area=aptestudio1.VALOR_AREA)
        aptestudio1.imprimir()


if __name__ == '__main__':
    Prueba.main()
