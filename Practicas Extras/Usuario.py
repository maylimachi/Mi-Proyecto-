class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        self.saldo_pagar += monto

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    # BONUS
    def transferir_deuda(self, otro_usuario, monto):
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto

        if self.saldo_pagar < 0:
            self.saldo_pagar = 0


# Crear usuarios
usuario1 = Usuario("Juan", "Perez", "juan@mail.com")
usuario2 = Usuario("Ana", "Gomez", "ana@mail.com")
usuario3 = Usuario("Luis", "Martinez", "luis@mail.com")


# Usuario 1: 2 compras y paga
usuario1.hacer_compra(5000)
usuario1.hacer_compra(3000)
usuario1.pagar_tarjeta(4000)
usuario1.mostrar_saldo_usuario()


# Usuario 2: 1 compra y paga 2 veces
usuario2.hacer_compra(7000)
usuario2.pagar_tarjeta(2000)
usuario2.pagar_tarjeta(1000)
usuario2.mostrar_saldo_usuario()


# Usuario 3: 3 compras y paga 4 veces
usuario3.hacer_compra(2000)
usuario3.hacer_compra(1500)
usuario3.hacer_compra(2500)

usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(500)

usuario3.mostrar_saldo_usuario()