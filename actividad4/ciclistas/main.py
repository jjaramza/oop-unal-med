from carrera_ciclistica.equipo import Equipo
from carrera_ciclistica.velocista import Velocista
from carrera_ciclistica.escalador import Escalador
from carrera_ciclistica.contrarrelojista import Contrarrelojista

class Prueba:
    """
    Esta clase prueba diferentes acciones realizadas por un equipo ciclístico
    y sus diferentes corredores.
    """
    
    @staticmethod
    def main():
        """
        Método main que crea un equipo. Luego, crea un escalador, un
        velocista y un contrarrelojista. Estos tipos de ciclistas son añadidos
        al equipo. Se asignan tiempos a cada ciclista para al final obtener el
        tiempo total del equipo.
        """
        equipo1 = Equipo("Sky", "Estados Unidos")
        velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
        escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
        contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)
        
        equipo1.anhadir_ciclista(velocista1)
        equipo1.anhadir_ciclista(escalador1)
        equipo1.anhadir_ciclista(contrarrelojista1)
        
        velocista1._tiempo_acumulado = 365
        escalador1._tiempo_acumulado = 385
        contrarrelojista1._tiempo_acumulado = 370
        
        equipo1.calcular_total_tiempo()
        equipo1.imprimir()
        equipo1.listar_equipo()
        
if __name__ == '__main__':
    Prueba.main()
