from Conta import Conta

minhaConta = Conta("00667676", "Itau","Arthur Amorim")
minhaConta.depositar(0)

print("Valor antes do saque")
print(minhaConta.getSaldo())


minhaConta.sacar(0)
print("Valor depois do saque")
print(minhaConta.getSaldo())

back="N"
while True:
    print("===MENU===")
    print(f"acessando a conta de {minhaConta.NomeTitular}")
    print("\033[1;37m[1]\033[m-Depositar\n\033[1;37m[2]\033[m-Sacar\n\033[1;37m[3]\033[m-Verificar o Saldo\n\033[1;37m[4]\033[m-Sair")
    option=input("Qual opção deseja executar?\n").strip()
    if option == '4':
        print("fim do programa")
        break
    elif option == '1':
        while True:
            deposito=input("Quanto deseja depositar?\nR$").strip()

            if deposito.isdigit():
                deposito = float(deposito)
                minhaConta.depositar(deposito)
                print(f"Foi depositado R${deposito:.2f} na sua conta")
                break
            else:
                print("\033[1;31mOpção inválida. Por favor, digite apenas números!!\033[m")
    elif option == '2':
        while True:
            sacar=input("Digite o valor do saque: R$").strip()
            if sacar.isdigit():
                sacar=float(sacar)
                minhaConta.sacar(sacar)
                print(f"Você sacou {sacar:.2f} do seu saldo")
                break
            else:
                print("\033[1;31mOpção inválida. Por favor, digite apenas números!!\033[m")
    elif option == '3':
        print(f"Você tem R${minhaConta.getSaldo():.2f}")
    else:
        print("\033[1;31mOpção inválida,Por favor digite apenas oque esta sendo mostrado!!\033[m")
    while True:
        back = input("Deseja continuar? [S/N]\n").strip().upper()
        if back == "S" or back == "N":
            break
        print("\033[1;31mOpção inválida,Por favor digite apenas oque esta sendo mostrado!!\033[m")
    if back == 'N':
        print("fim do programa")
        break
        