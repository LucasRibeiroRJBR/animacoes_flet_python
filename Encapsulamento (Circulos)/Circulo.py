class Circulo():
    # Controlando a quantidade de círculos
    # Valor único para todos os objetos da classe
    total_circulos = 0

    def __init__(self,pontox,pontoy,raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        self.total_circulos += 1

    @classmethod
    def get_total_circulos(cls):
        return cls._total_circulos

