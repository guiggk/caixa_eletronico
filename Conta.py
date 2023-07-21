class Conta:
    def __init__(self, conta: str,  banco: str):
        self.conta = conta
        self.banco = banco
        self.saldo = 0
        
    def depositar(self, valorADepositar):
        self.saldo += valorADepositar
        
    def getSaldo(self):
        return self.saldo 
    
    def sacar(self, valorASacar):
        if self.saldo >= valorASacar:
            self.saldo -= valorASacar
        else:
            print("Se lasque, vc está sem saldo!")
                  





    