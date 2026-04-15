class TarjetaCredito:
    tarjetas = []  

    def __init__(self, saldo_pagar=0, limite_credito=10000, intereses=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas.append(self) 

    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    # BONUS
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("\n--- Todas las tarjetas ---")
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {i}: Saldo: ${tarjeta.saldo_pagar}, Límite: ${tarjeta.limite_credito}")


# Crear tarjetas
tarjeta1 = TarjetaCredito(0, 10000, 0.02)
tarjeta2 = TarjetaCredito(0, 15000, 0.03)
tarjeta3 = TarjetaCredito(0, 5000, 0.01)


# Tarjeta 1: 2 compras, 1 pago, intereses y mostrar (encadenado)
tarjeta1.compra(2000).compra(3000).pago(1000).cobrar_interes().mostrar_info_tarjeta()


# Tarjeta 2: 3 compras, 2 pagos, intereses y mostrar (encadenado)
tarjeta2.compra(4000).compra(2000).compra(1000).pago(1500).pago(500).cobrar_interes().mostrar_info_tarjeta()


# Tarjeta 3: 5 compras y excede límite (encadenado)
tarjeta3.compra(2000).compra(2000).compra(1500).compra(1000).compra(500).mostrar_info_tarjeta()


# BONUS: mostrar todas
TarjetaCredito.mostrar_todas_las_tarjetas()