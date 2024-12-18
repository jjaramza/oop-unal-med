# Ejercicio resuelto No 14 del Capítulo 4. Libro de Lógica de Programación de Efrain Oviedo.

class Nomina:
    
    def __init__(self,
                 ventas_dpto1: int,
                 ventas_dpto2: int,
                 ventas_dpto3: int,
                 salario_trabajador: int) -> None:
        self.ventas1 = ventas_dpto1
        self.ventas2 = ventas_dpto2
        self.ventas3 = ventas_dpto3
        self.salario1 =  salario_trabajador
        self.salario2 =  salario_trabajador
        self.salario3 =  salario_trabajador
        
    def calculo_salario(self) -> None:
        """
        Se calcula el salario de cada trabajador de acuerdo a las ventas
        de cada departamento. Se otorgan incentivos.
        """
        total_ventas = self.ventas1 + self.ventas2 + self.ventas3
        porc_ventas = 0.33 * total_ventas
        
        if self.ventas1 > porc_ventas:
            self.salario1 *= 1.2
            
        if self.ventas2 > porc_ventas:
            self.salario2 *= 1.2
        
        if self.ventas3 > porc_ventas:
            self.salario3 *= 1.2
            
    def mostrar_salarios(self) -> str:
        """Mostrar el salario de los vendedadores por departamento."""
        self.calculo_salario()
        return (
            f"Salario vendedores departamento 1: {self.salario1:.0f}\n"
            f"Salario vendedores departamento 2: {self.salario2:.0f}\n"
            f"Salario vendedores departamento 3: {self.salario3:.0f}"
        )
        

def main() -> None:
    # Solicitud de datos
    dpt1 = int(input("Ingrese las ventas del departamento 1: "))
    dpt2 = int(input("Ingrese las ventas del departamento 2: "))
    dpt3 = int(input("Ingrese las ventas del departamento 3: "))
    salario = int(input("Ingrese el salario de los trabajadores: "))
    
    # Se crea un objeto de tipo Nomina
    nomina = Nomina(ventas_dpto1=dpt1,
                    ventas_dpto2=dpt2,
                    ventas_dpto3=dpt3,
                    salario_trabajador=salario)
    
    # Se muestra la información
    print(nomina.mostrar_salarios())
    

if __name__ == "__main__":
    main()
