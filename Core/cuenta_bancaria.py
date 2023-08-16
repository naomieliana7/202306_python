class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance += amount 
        return self
    
    def retiro(self, amount):
        self.balance -= amount
        return self
    
    def mostrar_info_cuenta(self):
        print("Balance: ", self.balance)
        return self
    
    def generar_interés(self):
        self.balance += (self.balance*self.tasa_interés)
        return self
    
    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas: 
            print(f"Balance: {cuenta.balance}, Tasa de Interés: {cuenta.tasa_interés}")

cuenta1 = CuentaBancaria(0.01, 0)
cuenta2 = CuentaBancaria(0.015, 0)

cuenta1.depósito(50).depósito(100).depósito(150).retiro(25).generar_interés().mostrar_info_cuenta()
cuenta2.depósito(150).depósito(200).retiro(35).retiro(15).retiro(20).retiro(50).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()