import pickle
from datetime import datetime
from random import randint

from sqlalchemy import true

from Model.Cobro import Cobro
from Model.Parking import Parking
from Model.Ticket import Ticket
from ZonaAdministrador import parking




class ZonaCliente:

    def depositar_vehiculo(self, matricula, tipo,parking):
        # Buscar una plaza libre del tipo especificado
        plaza_libre = None

        for plaza in parking.lista_plazas:
            if plaza.estado == "libre" and plaza.tipo == 'turismo':
                plaza_libre = plaza

                break
                # Si no hay plazas libres del tipo especificado, informar al usuario
            if plaza_libre is None:
                print("No hay plazas libres para este tipo de vehículo.")
                return

            # Asignar la plaza al vehículo y generar un ticket
            plaza_libre.estado = "ocupado"
            parking.num_plazas_libres -= 1
            parking.num_plazas_ocupadas += 1

            ticket = Ticket(matricula, datetime.now(), plaza_libre.identificador, randint(100000, 999999))
            ticket.guardar_ticket()

            print("Se ha asignado la plaza {} al vehículo con matrícula {}.".format(plaza_libre.identificador, matricula))
            print("Ticket generado:")
            print("Matrícula: {}".format(ticket.matricula))
            print("Fecha de depósito: {}".format(ticket.fecha_deposito))
            print("Identificador de plaza: {}".format(ticket.identificador_plaza))
            print("Pin: {}".format(ticket.pin))
            return

    def retirar_vehiculo(self, matricula, identificador_plaza, pin):
        # Buscar el ticket correspondiente al vehículo y plaza especificados
        ticket_encontrado = None
        with open("tickets.pickle", "rb") as f:
            while True:
                try:
                    ticket = pickle.load(f)
                    if ticket.matricula == matricula and ticket.identificador_plaza == identificador_plaza and ticket.pin == pin:
                        ticket_encontrado = ticket
                        break
                except EOFError:
                    break
        # Si no se encuentra el ticket, informar al usuario
        if ticket_encontrado is None:
            print("No se ha encontrado un ticket válido para este vehículo y plaza.")
            return

            # Calcular el coste y actualizar el estado de la plaza

            tiempo_estacionado = datetime.now() - ticket_encontrado.fecha_deposito

            coste = 0

            if tipo == "turismo":
                coste = tiempo_estacionado.total_seconds() * 0.12
            elif tipo == "motocicleta":
                coste = tiempo_estacionado.total_seconds() * 0.08
            elif tipo == "movilidad reducida":
                coste = tiempo_estacionado.total_seconds() * 0.10

                # Actualizar el estado de la plaza y generar un cobro

                for plaza in parking.lista_plazas:

                    if plaza.identificador == identificador_plaza:
                        plaza.estado = "libre"
                        parking.num_plazas_libres += 1
                        parking.num_plazas_ocupadas -= 1
                    break
            cobro = Cobro(matricula, datetime.now(), identificador_plaza, coste, pin)
            cobro.guardar_cobro()

            print("El coste total es: {:.2f} €".format(coste))
            print("El vehículo con matrícula {} ha sido retirado del parking.".format(matricula))

    def depositar_abonado(self, matricula, DNI):

        # Buscar el cliente abonado correspondiente al DNI especificado

        cliente_encontrado = None

        with open("clientes.pickle", "rb") as f:

            while true:
                try:

                    cliente = pickle.load(f)

                    if cliente.DNI == DNI:
                        cliente_encontrado = cliente
                        break

                except EOFError:
                    break
                    # Si no se encuentra el cliente abonado, informar al usuario
        if cliente_encontrado is None:
            print("No se ha encontrado un cliente abonado con este DNI.")
        return

        # Buscar una plaza libre

        plaza_libre = None

        for plaza in parking.lista_plazas:

            if plaza.estado == "libre":
                plaza_libre = plaza

                break

            # Si no hay plazas libres, informar al usuario

            if plaza_libre is None:
                print("No hay plazas libres en este momento.")

                return

                # Asignar la plaza al cliente abonado y generar un pin

                plaza_libre.estado = "ocupado"

                parking.num_plazas_libres -= 1

                parking.num_plazas_ocupadas += 1

                pin = randint(100000, 999999)

                cliente_encontrado.pin = pin

                print("Se ha asignado la plaza {} al cliente abonado con DNI {}.".format(plaza_libre.identificador,
                                                                                         DNI))

                print("Pin generado: {}".format(pin))

    def retirar_abonado(self, matricula, identificador_plaza, pin):

        # Buscar el cliente abonado correspondiente a la matrícula especificada

        cliente_encontrado = None

        with open("clientes.pickle", "rb") as f:

            while True:

                try:
                    cliente = pickle.load(f)

                    if cliente.matricula == matricula and cliente.pin == pin:
                        cliente_encontrado = cliente

                        break


                except EOFError:

                    break

        # Si no se encuentra el cliente abonado, informar al usuario
        if cliente_encontrado is None:
            print("No se ha encontrado un cliente abonado con esta matrícula y pin.")

            return

        # Actualizar el estado de la plaza

        for plaza in parking.lista_plazas:

            if plaza.identificador == identificador_plaza:
                plaza.estado = "ocupado"

                parking.num_plazas_libres += 1

                parking.num_plazas_ocupadas -= 1

                break

        print("El vehículo con matrícula {} ha sido retirado del parking.".format(matricula))
