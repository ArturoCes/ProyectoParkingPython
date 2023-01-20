import pickle

class Cobro:
    def __init__(self, matricula, fecha_salida, identificador_plaza, coste, pin):
        self.matricula = matricula
        self.fecha_salida = fecha_salida
        self.identificador_plaza = identificador_plaza
        self.coste = coste
        self.pin = pin

    def guardar_cobro(self):
        with open("cobros.pickle", "wb") as f:
            pickle.dump(self, f)
