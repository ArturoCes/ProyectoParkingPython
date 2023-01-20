import pickle

class Ticket:
    def __init__(self, matricula, fecha_deposito, identificador_plaza, pin):
        self.matricula = matricula
        self.fecha_deposito = fecha_deposito
        self.identificador_plaza = identificador_plaza
        self.pin = pin

    def guardar_ticket(self):
        with open("tickets.pickle", "wb") as f:
            pickle.dump(self, f)
