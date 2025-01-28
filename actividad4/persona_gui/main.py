from personas.ventana_principal import VentanaPrincipal

class Principal:
    """
    Esta clase define el punto de ingreso al programa de gestión de personas.
    Por lo tanto, cuenta con un método main de acceso al programa.
    """
    
    @staticmethod
    def main():
        """Método main que sirve de punto de entrada al programa"""
        app = VentanaPrincipal()
        app.mainloop()
        
if __name__ == '__main__':
    Principal.main()
