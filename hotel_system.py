from datetime import date
from typing import List, Optional
import os

class Cliente:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class ClienteHabitual(Cliente):
    def __init__(self, nombre: str, direccion: str, telefono: str, descuento: float = 0.1):
        super().__init__(nombre, direccion, telefono)
        self.descuento = descuento

class ClienteEsporadico(Cliente):
    def __init__(self, nombre: str, direccion: str, telefono: str, quiere_ofertas: bool = True):
        super().__init__(nombre, direccion, telefono)
        self.quiere_ofertas = quiere_ofertas

class Habitacion:
    def __init__(self, numero: int, precio: float, foto: str):
        self.numero = numero
        self.precio = precio
        self.foto = foto
        self.esta_reservada = False

    def reservar(self):
        self.esta_reservada = True

    def cambiar_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio

class HabitacionSencilla(Habitacion):
    def __init__(self, numero: int, precio: float, foto: str, exterior: bool):
        super().__init__(numero, precio, foto)
        self.exterior = exterior

class HabitacionDoble(Habitacion):
    def __init__(self, numero: int, precio: float, foto: str, cama_matrimonial: bool):
        super().__init__(numero, precio, foto)
        self.cama_matrimonial = cama_matrimonial
class HabitacionSuite(Habitacion):
    def __init__(self, numero: int, precio: float, foto: str, banera: bool, sauna: bool, mirador: bool):
        super().__init__(numero, precio, foto)
        self.banera = banera
        self.sauna = sauna
        self.mirador = mirador

class Reserva:
    def __init__(self, fecha_entrada: date, numero_dias: int, habitacion: Habitacion, cliente: Cliente):
        self.fecha_entrada = fecha_entrada
        self.numero_dias = numero_dias
        self.habitacion = habitacion
        self.cliente = cliente

class Hotel:
    def __init__(self, nombre: str, numero_estrellas: int):
        self.nombre = nombre
        self.numero_estrellas = numero_estrellas
        self.habitaciones: List[Habitacion] = []
        self.reservas: List[Reserva] = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def listar_habitaciones_disponibles_por_tipo(self, tipo: type) -> List[str]:
        disponibles = []
        for h in self.habitaciones:
            if isinstance(h, tipo) and not h.esta_reservada:
                info = f"Número: {h.numero}, Precio: {h.precio}, Tipo: {tipo.__name__}"
                # Agregar detalles específicos según el tipo
                if isinstance(h, HabitacionSencilla):
                    info += f", Exterior: {'Sí' if h.exterior else 'No'}"
                elif isinstance(h, HabitacionDoble):
                    info += f", Cama matrimonial: {'Sí' if h.cama_matrimonial else 'No'}"
                elif isinstance(h, HabitacionSuite):
                    info += f", Bañera: {'Sí' if h.banera else 'No'}, Sauna: {'Sí' if h.sauna else 'No'}, Mirador: {'Sí' if h.mirador else 'No'}"
                disponibles.append(info)
        return disponibles

    def consultar_precio_por_tipo(self, tipo: type) -> List[str]:
        precios_info = []
        for h in self.habitaciones:
            if isinstance(h, tipo):
                info = f"Número: {h.numero} Precio: {h.precio} Tipo: {tipo.__name__}"
                if isinstance(h, HabitacionSencilla):
                    info += f"Exterior: {'Sí' if h.exterior else 'No'}"
                elif isinstance(h, HabitacionDoble):
                    info += f"Cama matrimonial: {'Sí' if h.cama_matrimonial else 'No'}"
                elif isinstance(h, HabitacionSuite):
                    info += f"Bañera: {'Sí' if h.banera else 'No'}"
                    info += f"Sauna: {'Sí' if h.sauna else 'No'}"
                    info += f"Mirador: {'Sí' if h.mirador else 'No'}"
                precios_info.append(info.strip())
        return precios_info


    def reservar_habitacion_por_numero(self, numero: int, cliente: Cliente, fecha_entrada: date, numero_dias: int) -> Optional[Reserva]:
        for h in self.habitaciones:
            if h.numero == numero and not h.esta_reservada:
                h.reservar()
                reserva = Reserva(fecha_entrada, numero_dias, h, cliente)
                self.reservas.append(reserva)
                return reserva
        return None

    def cambiar_precio_por_tipo(self, tipo: type, nuevo_precio: float):
        for h in self.habitaciones:
            if isinstance(h, tipo):
                h.cambiar_precio(nuevo_precio)

def mostrar_menu():
    os.system('cls')
    print("\n--- Menú del Hotel ---")
    print("1. Listar habitaciones disponibles por tipo")
    print("2. Consultar precio por tipo de habitación")
    print("3. Mostrar descuentos de clientes habituales")
    print("4. Reservar una habitación por número")
    print("5. Cambiar precio por tipo de habitación")
    print("6. Salir")

def seleccionar_tipo_habitacion():
    print("Tipos de habitación:")
    print("1. Sencilla")
    print("2. Doble")
    print("3. Suite")
    opcion = input("Seleccione el tipo de habitación (1-3): ")
    if opcion == "1":
        return HabitacionSencilla
    elif opcion == "2":
        return HabitacionDoble
    elif opcion == "3":
        return HabitacionSuite
    else:
        print("Opción inválida.")
        return None

def main():
    hotel = Hotel("Hotel Sol", 4)
    hotel.agregar_habitacion(HabitacionSencilla(101, 70.0, "foto101.jpg", True))
    hotel.agregar_habitacion(HabitacionSencilla(102, 50.0, "foto102.jpg", False))
    hotel.agregar_habitacion(HabitacionSencilla(103, 70.0, "foto103.jpg", True))
    hotel.agregar_habitacion(HabitacionDoble(201, 100.0, "foto201.jpg", False))
    hotel.agregar_habitacion(HabitacionDoble(202, 150.0, "foto202.jpg", True))
    hotel.agregar_habitacion(HabitacionDoble(203, 100.0, "foto203.jpg", False))
    hotel.agregar_habitacion(HabitacionSuite(301, 800.0, "foto302.jpg", True, True, True))
    hotel.agregar_habitacion(HabitacionSuite(302, 700.0, "foto303.jpg", True, True, False))
    hotel.agregar_habitacion(HabitacionSuite(303, 700.0, "foto303.jpg", True, False, True))
    hotel.agregar_habitacion(HabitacionSuite(304, 600.0, "foto303.jpg", True, False, False))
    hotel.agregar_habitacion(HabitacionSuite(305, 500.0, "foto301.jpg", False, False, False))
    hotel.agregar_habitacion(HabitacionSuite(306, 600.0, "foto301.jpg", False, False, True))
    hotel.agregar_habitacion(HabitacionSuite(307, 700.0, "foto301.jpg", False, True, True))
    hotel.agregar_habitacion(HabitacionSuite(308, 600.0, "foto301.jpg", False, True, False))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        os.system('cls')

        if opcion == "1":
            tipo = seleccionar_tipo_habitacion()
            if tipo:
                disponibles = hotel.listar_habitaciones_disponibles_por_tipo(tipo)
                if disponibles:
                    print("\n--- Habitaciones disponibles ---")
                    for habitacion in disponibles:
                        print(habitacion)
                else:
                    print("No hay habitaciones disponibles de este tipo.")
            input("Presiona Enter para volver...")

        elif opcion == "2":
            tipo = seleccionar_tipo_habitacion()
            if tipo:
                preferencias = {}
                if tipo == HabitacionSencilla:
                    exterior = input("¿Quiere que sea exterior? (s/n): ").lower() == 's'
                    preferencias['exterior'] = exterior
                elif tipo == HabitacionDoble:
                    cama = input("¿Quiere cama matrimonial? (s/n): ").lower() == 's'
                    preferencias['cama_matrimonial'] = cama
                elif tipo == HabitacionSuite:
                    banera = input("¿Quiere bañera? (s/n): ").lower() == 's'
                    sauna = input("¿Quiere sauna? (s/n): ").lower() == 's'
                    mirador = input("¿Quiere mirador? (s/n): ").lower() == 's'
                    preferencias.update({'banera': banera, 'sauna': sauna, 'mirador': mirador})

                coincidencias = []
                for h in hotel.habitaciones:
                    if isinstance(h, tipo):
                        cumple = True
                        if tipo == HabitacionSencilla and h.exterior != preferencias['exterior']:
                            cumple = False
                        elif tipo == HabitacionDoble and h.cama_matrimonial != preferencias['cama_matrimonial']:
                            cumple = False
                        elif tipo == HabitacionSuite:
                            if h.banera != preferencias['banera'] or h.sauna != preferencias['sauna'] or h.mirador != preferencias['mirador']:
                                cumple = False
                        if cumple:
                            info = f"Número: {h.numero}\nPrecio: {h.precio}\nTipo: {tipo.__name__}\n"
                            if tipo == HabitacionSencilla:
                                info += f"Exterior: {'Sí' if h.exterior else 'No'}\n"
                            elif tipo == HabitacionDoble:
                                info += f"Cama matrimonial: {'Sí' if h.cama_matrimonial else 'No'}\n"
                            elif tipo == HabitacionSuite:
                                info += f"Bañera: {'Sí' if h.banera else 'No'}\nSauna: {'Sí' if h.sauna else 'No'}\nMirador: {'Sí' if h.mirador else 'No'}\n"
                            coincidencias.append(info.strip())

                if coincidencias:
                    print("\n--- Habitaciones que cumplen sus preferencias ---")
                    for habitacion in coincidencias:
                        print(habitacion)
                        print("-" * 30)
                else:
                    print("No hay habitaciones que cumplan esas características.")
            input("Presiona Enter para volver...")

        elif opcion == "3":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            
            cliente_habitual = None
            for r in hotel.reservas:
                if r.cliente.nombre.lower() == nombre_cliente.lower() and isinstance(r.cliente, ClienteHabitual):
                    cliente_habitual = r.cliente
                    break

            print("\n--- Precios de habitaciones ---")
            for h in hotel.habitaciones:
                info = f"Habitación {h.numero} ({h.__class__.__name__})\nPrecio normal: {h.precio}"
                if cliente_habitual:
                    precio_descuento = h.precio * (1 - cliente_habitual.descuento)
                    info += f"\nPrecio con descuento (20%): {precio_descuento}"
                print(info)
                print("-" * 30)
            input("Presiona Enter para volver...")

        elif opcion == "4":
            tipo = seleccionar_tipo_habitacion()
            if tipo:
                disponibles = hotel.listar_habitaciones_disponibles_por_tipo(tipo)
                if disponibles:
                    print("\n--- Habitaciones disponibles ---")
                    for habitacion in disponibles:
                        print(habitacion)
                else:
                    print("No hay habitaciones disponibles de este tipo.")
            numero = int(input("Número de habitación a reservar: "))
            nombre = input("Nombre del cliente: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            habitual = input("¿Es cliente habitual? (s/n): ").lower() == 's'
            if habitual:
                cliente = ClienteHabitual(nombre, direccion, telefono)
            else:
                cliente = ClienteEsporadico(nombre, direccion, telefono)
            dias = int(input("Número de días de la reserva: "))
            reserva = hotel.reservar_habitacion_por_numero(numero, cliente, date.today(), dias)
            if reserva:
                print(f"Habitación {numero} reservada para {cliente.nombre}")
            else:
                print("No se pudo realizar la reserva. Verifique el número de habitación.")
            input("Presiona Enter para volver...")

        elif opcion == "5":
            tipo = seleccionar_tipo_habitacion()
            if tipo:
                disponibles = hotel.listar_habitaciones_disponibles_por_tipo(tipo)
                if disponibles:
                    print("\n--- Habitaciones disponibles ---")
                    for habitacion in disponibles:
                        print(habitacion)
                else:
                    print("No hay habitaciones disponibles de este tipo.")
            numero = int(input("Ingrese el número de la habitación: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            habitacion_encontrada = False

            for h in hotel.habitaciones:
                if h.numero == numero and h.esta_reservada == False:
                    h.cambiar_precio(nuevo_precio)
                    habitacion_encontrada = True
                    print(f"Precio actualizado para la habitación {numero}. Nuevo precio: {nuevo_precio}")
                    break

            if not habitacion_encontrada:
                print("No se encontró una habitación disponible con ese número.")
            input("Presiona Enter para volver...")

        elif opcion == "6":
            print("Gracias por usar el sistema del hotel.")
            input("Presiona Enter para volver...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()