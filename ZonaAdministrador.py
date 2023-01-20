import pickle
parking=None

class ZonaAdministrador:
    def consultar_plazas_libres(self):
        # Recuperar información de las plazas libres del parking
        num_plazas_libres_turismo = 0
        num_plazas_libres_motocicletas = 0
        num_plazas_libres_movilidad_reducida = 0
        for plaza in parking.lista_plazas:

            if plaza.estado == "libre":
                if plaza.tipo == "turismo":
                    num_plazas_libres_turismo += 1
                elif plaza.tipo == "motocicleta":
                    num_plazas_libres_motocicletas += 1
                elif plaza.tipo == "movilidad reducida":
                    num_plazas_libres_movilidad_reducida += 1

                    print("Plazas libres:")
                    print("Turismo: {}".format(num_plazas_libres_turismo))
                    print("Motocicletas: {}".format(num_plazas_libres_motocicletas))
                    print("Movilidad reducida: {}".format(num_plazas_libres_movilidad_reducida))

    def consultar_cobros_realizados(self):
        # Recuperar información de los cobros realizados
        with open("cobros.pickle", "rb") as f:
            while True:

                try:
                    cobro = pickle.load(f)
                    print("Cobro generado:")

                    print("Matrícula: {}".format(cobro.matricula))
                    print("Fecha de salida: {}".format(cobro.fecha_salida))
                    print("Identificador de plaza: {}".format(cobro.identificador_plaza))
                    print("Coste: {:.2f} €".format(cobro.coste))
                except EOFError:
                    break

    def consultar_abonados(self):

        #Recuperar información de los clientes abonados

        with open("clientes.pickle", "rb") as f:

            while True:

                try:

                    cliente = pickle.load(f)

                    print("Información del cliente abonado:")

                    print("DNI: {}".format(cliente.DNI))
                    print("Nombre: {}".format(cliente.nombre))
                    print("Apellidos: {}".format(cliente.apellidos))
                    print("Número de tarjeta de crédito: {}".format(cliente.num_tarjeta_credito))
                    print("Tipo de abono: {}".format(cliente.tipo_abono))
                    print("Email: {}".format(cliente.email))
                except EOFError:
                    break
                    