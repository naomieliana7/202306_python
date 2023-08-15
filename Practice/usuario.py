class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # agregando el método de depósito
    def hacer_depósito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

    # agregando método de retiro de dinero
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    #agregando método de reetiro
    def mostrar_balance_usuario(self): 
        print("Usuario:", self.name, ", Balance: ", self.balance_cuenta)

    #agregando método de transferencia de dinero 
    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        print(self.name, "ha tranferido", amount, "a", other_user.name)


guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
rafael = Usuario("Rafael Escobar", "rafael@python.com")

guido.hacer_depósito(20)
guido.hacer_depósito(50)
guido.hacer_depósito(100)
guido.hacer_retiro(35)
guido.mostrar_balance_usuario()

monty.hacer_depósito(60)
monty.hacer_depósito(121)
monty.hacer_retiro(16)
monty.hacer_retiro(24)
monty.mostrar_balance_usuario()

rafael.hacer_depósito(200)
rafael.hacer_retiro(35)
rafael.hacer_retiro(62)
rafael.hacer_retiro(25)
rafael.mostrar_balance_usuario()

monty.transfer_dinero(rafael, 25)