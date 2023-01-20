from Model.Parking import Parking
from ZonaAdministrador import ZonaAdministrador
from ZonaCliente import ZonaCliente

if __name__ == "__main__":
    n_plazas=100
    num = 1
    parking = Parking(70, 15, 15, n_plazas)
    parking.crear_plazas(num)

    # Crear un objeto de la clase ZonaCliente y ZonaAdministrador
    zona_cliente = ZonaCliente()
    zona_administrador = ZonaAdministrador()

    while True:
        # Menú principal
        print("\nMenú principal:")
        print("1. Zona cliente")
        print("2. Zona administrador")
        print("3. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # Menú zona cliente
            while True:
                print("\nZona cliente:")
                print("1. Depositar vehículo")
                print("2. Retirar vehículo")
                print("3. Depositar abonado")
                print("4. Retirar abonado")
                print("5. Volver al menú principal")
                opcion_cliente = int(input("Seleccione una opción: "))

                if opcion_cliente == 1:
                    matricula = input("Introduzca la matrícula del vehículo: ")
                    tipo = input("Introduzca el tipo de vehículo (turismo, motocicleta o movilidad reducida): ")
                    zona_cliente.depositar_vehiculo(matricula, tipo,parking)
                elif opcion_cliente == 2:
                    matricula = input("Introduzca la matrícula del vehículo: ")
                    identificador_plaza = int(input("Introduzca el identificador de la plaza: "))
                    pin = int(input("Introduzca el pin asociado: "))
                    zona_cliente.retirar_vehiculo(matricula, identificador_plaza, pin)
                elif opcion_cliente == 3:
                    matricula = input("Introduzca la matrícula del vehículo: ")
                    DNI = input("Introduzca el DNI del cliente abonado: ")
                    zona_cliente.depositar_abonado(matricula, DNI)
                elif opcion_cliente == 4:
                    matricula = input("Introduzca la matricula del vehiculo: ")
                    identificador_plaza = int(input("Introduzca el identificador de la plaza: "))
                    pin = int(input("Introduzca el pin asociado "))
                    zona_cliente.retirar_abonado(matricula, identificador_plaza, pin)
                elif opcion_cliente == 5:
                    break
        elif opcion == 2:
            # Menu zona de administrador
            while True:
                print("\nZona administrador:")
                print("1. Consultar plazas libres")
                print("2. Consultar cobros realizados")
                print("3. Consultar clientes abonados")
                print("4. Volver al menú principal")
                opcion_admin = int(input("Seleccione una opción: "))

                if opcion_admin == 1:
                    zona_administrador.consultar_plazas_libres()
                elif opcion_admin == 2:
                    zona_administrador.consultar_cobros_realizados()
                elif opcion_admin == 3:
                    zona_administrador.consultar_abonados()
                elif opcion_admin == 4:
                    break
        elif opcion == 3:
            break
