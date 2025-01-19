from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente

class PruebaCuenta:
    """
    Esta clase prueba diferentes acciones realizadas por cuentas bancarias
    de tipo Cuenta de ahorros y Cuenta corriente
    """
    
    @staticmethod
    def main():
        """
        Método main que crea una cuenta de ahorros con un saldo inicial
        y una tasa de interés solicitados por teclado, a la cual se realiza una
        consignación y un retiro, y luego se le genera el extracto mensual
        """
        print("\nCuenta de ahorros")
        saldo_inicial_ahorros = float(input("Ingrese saldo inicial: $ "))
        tasa_ahorros = float(input("Ingrese tasa de interés: "))
        
        cuenta1 = CuentaAhorros(saldo_inicial_ahorros, tasa_ahorros)
        
        cantidad_depositar = float(input("Ingresar cantidad a consignar: $ "))
        cuenta1.consignar(cantidad_depositar)
        
        cantidad_retirar = float(input("Ingresar cantidad a retirar: $ "))
        cuenta1.retirar(cantidad_retirar)
        
        cuenta1.extracto_mensual()
        
        cuenta1.imprimir()
        
        
if __name__ == '__main__':
    PruebaCuenta.main()
