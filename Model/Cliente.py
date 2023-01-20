import pickle

class Cliente:
    def __init__(self, DNI, nombre, apellidos, num_tarjeta, tipo_abono, email):
        self.DNI = DNI
        self.nombre = nombre
        self.apellidos = apellidos
        self.num_tarjeta = num_tarjeta
        self.tipo_abono = tipo_abono
        self.email = email

    def guardar_cliente(self):
        with open("clientes.pickle", "wb") as f:
            pickle.dump(self, f)
        