import pickle

from Model.Plaza import Plaza

class Parking:
    def __init__(self, porcentaje_plazas_turismo, porcentaje_plazas_motocicletas, porcentaje_plazas_movilidad_reducida,
                 n_plazas):
        self.porcentaje_plazas_turismo = porcentaje_plazas_turismo
        self.porcentaje_plazas_motocicletas = porcentaje_plazas_motocicletas
        self.porcentaje_plazas_movilidad_reducida = porcentaje_plazas_movilidad_reducida
        self.lista_plazas = []
        self.n_plazas = n_plazas

    def crear_plazas(self, num=None):
        n_plazas_turismo = int(self.n_plazas * self.porcentaje_plazas_turismo / 100)
        n_plazas_motocicletas = int(self.n_plazas * self.porcentaje_plazas_motocicletas / 100)
        n_plazas_movilidad_reducida = int(self.n_plazas * self.porcentaje_plazas_movilidad_reducida / 100)
        num += num
        for i in range(n_plazas_turismo):
            self.lista_plazas.append(Plaza(num,"libre", "turismo"))

        for i in range(n_plazas_motocicletas):
            self.lista_plazas.append(Plaza(num,"libre", "motocicleta"))

        for i in range(n_plazas_movilidad_reducida):
            self.lista_plazas.append(Plaza(num,"libre", "movilidad reducida"))

            return print(self.lista_plazas)

    def guardar_parking(self):
        with open("parking.pickle", "wb") as f:
            pickle.dump(self, f)
