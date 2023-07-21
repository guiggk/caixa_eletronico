from Conta import Conta

minhaConta = Conta("00667676", "Itau")
minhaConta.depositar(10000)

print("Valor antes do saque")
print(minhaConta.getSaldo())


minhaConta.sacar(11000)
print("Valor depois do saque")
print(minhaConta.getSaldo())

"""
    1 - Depositar
    2 - Sacar
    3 - Saldo
    4 - Sair
"""

while option != 4:
    