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
            return self.balance
    
    def generar_interés(self):
        self.balance += (self.balance*self.tasa_interés)
        return self
    
    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas: 
            print(f"Balance: {cuenta.balance}, Tasa de Interés: {cuenta.tasa_interés}")

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(0.02, 0)
    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.cuenta.depósito(amount)	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self

    # agregando método de retiro de dinero
    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)
        return self

    #agregando método de reetiro
    def mostrar_balance_usuario(self): 
        print("Usuario:", self.name, ", Balance:", self.cuenta.mostrar_info_cuenta())
        return self

    #agregando método de transferencia de dinero 
    def transfer_dinero(self, other_user, amount):
        self.cuenta.retiro(amount)
        other_user.cuenta.depósito(amount)
        print(self.name, "ha tranferido", amount, "a", other_user.name)
        


guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
rafael = Usuario("Rafael Escobar", "rafael@python.com")

guido.hacer_depósito(100).hacer_depósito(200).hacer_depósito(300).hacer_retiro(50).mostrar_balance_usuario()
monty.hacer_depósito(60).hacer_depósito(121).hacer_retiro(16).hacer_retiro(24).mostrar_balance_usuario()
rafael.hacer_depósito(200).hacer_retiro(35).hacer_retiro(62).hacer_retiro(25).mostrar_balance_usuario()

monty.transfer_dinero(rafael, 25)