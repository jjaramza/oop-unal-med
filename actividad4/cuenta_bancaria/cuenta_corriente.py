from cuenta import Cuenta

class CuentaCorriente(Cuenta):
    """
    Esta clase denominada CuentaCorriente modela una cuenta bancaria
    que es una subclase de Cuenta. Tiene un nuevo atributo: sobregiro.
    
    Attributes:
        sobregiro (float): Sobregiro de la cuenta que surge cuando el saldo de la cuenta es negativo.
    """
    def __init__(self, saldo: float, tasa_anual: float) -> None:
        """
        Constructor de la clase CuentaCorriente.
        
        Args:
            _saldo (float): Saldo de la cuenta corriente.
            _tasa_anual (float): Tasa anual de interés de la cuenta corriente.
        """
        # Invoca al constructor de la clase padre
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0 # Inicialmente no hay sobregiro
    
    def retirar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a retirar y actualiza el
        saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar de la cuenta corriente.
        """
        resultado: float = self._saldo - cantidad # Se actualiza un saldo temporal
        
        # Si el valor a retirar supera el saldo de la cuenta, el valor
        # excedente se convierte en sobregiro y el saldo es cero
        if resultado < 0:
            self.sobregiro -= resultado
            self._saldo = 0
        else:
            # Si no hay sobregiro, se realiza un retiro normal
            super().retirar(cantidad)
            
    def consignar(self, cantidad: float) -> None:
        """
        Método que recibe una cantidad de dinero a consignar y actualiza 
        el saldo de la cuenta.
        
        Args:
            cantidad (float): Cantidad a consignar en la cuenta corriente.
        """
        residuo: float = cantidad - self.sobregiro
        
        # Si existe sobregiro la cantidad consignada se resta al sobregiro
        if self.sobregiro > 0:
            # Si el residuo es mayor que cero, se libera el sobregiro
            if residuo > 0:
                self.sobregiro = 0
                self._saldo = residuo
            else:
                # Si el residuo es menor que cero, el saldo es cero y surge un sobregiro
                self.sobregiro = -residuo
                self._saldo = 0
        else:
            # Si no hay sobregiro, se reliza una consignación normal
            super().consignar(cantidad)
            
    def extracto_mensual(self) -> None:
        """
        Método que genera un extracto mensual de la cuenta
        """
        super().extracto_mensual() # Invoca el método de la clase padre
            
    def imprimir(self) -> None:
        """
        Método que muestra en pantalla los datos de una cuenta de ahorros
        """
        print(f"\nSaldo = $ {self._saldo:.2f}")
        print(f"Comisión mensual = $ {self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._numero_consignaciones + self._numero_retiros}")
        print(f"Sobregiro = $ {self.sobregiro}\n")
