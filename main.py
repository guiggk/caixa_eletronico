from Conta import Conta

minhaConta = Conta("00667676", "Itau","Arthur Amorim")
minhaConta.depositar(0)

print("Valor antes do saque")
print(minhaConta.getSaldo())


minhaConta.sacar(0)
print("Valor depois do saque")
print(minhaConta.getSaldo())

option= 0
back="n"
while option != 4 and back != "N":
    print("===MENU===")
    print("acessando a conta de {}".format(minhaConta.NomeTitular))
    print("\033[1;37m[1]\033[m-Depositar\n\033[1;37m[2]\033[m-Sacar\n\033[1;37m[3]\033[m-Verificar o Saldo\n\033[1;37m[4]\033[m-Sair")
    option=int(input("Qual opção deseja executar?\n").strip())
    if option == 1:
        saldo=float(input("Quanto deseja depositar?\nR$").strip())
        saldo=minhaConta.depositar(saldo)
        print("foi depositado R${:.2f} na sua conta".format(minhaConta.getSaldo()))
        back=str(input("Deseja continuar?[S/N]\n")).upper().strip()
    if option == 2:
        minhaConta.sacar(float(input("Digite o valor do saque: R$")))
        back=str(input("Deseja continuar?[S/N]\n")).upper().strip()
    if option == 3:
        print("Você tem R${}".format(minhaConta.getSaldo()))
print("fim do programa")
        