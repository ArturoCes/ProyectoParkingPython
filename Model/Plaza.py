import pickle

class Plaza:
    def __init__(self, identificador, tipo, estado):
        self.identificador = identificador
        self.tipo = tipo
        self.estado = estado

    def guardar_plaza(self):
        with open("plazas.pickle", "wb") as f:
            pickle.dump(self, f)
