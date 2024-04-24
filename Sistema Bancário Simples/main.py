import sistema_bancario


#Operacoes Bancárias

# 0 - Criar/Logar usuário
# 1 - Deposito
# 2 - Saque
# 3-  Extrato
# 4 - Criar conta
# 5 - Sair

#REGRAS: 
 #Limite por saque de 500
 #Limite diario de 3 saques
 #Extrato de valor sacado
 #


operacao = 0
saldo = 0
extrato = 0
limite_diario = 0
usuarios = {}
contas = {}


while operacao != 4:

  print("\n 0 - Criar usuário"
        
        "\n 1 - Deposito"
        "\n 2 - Saque"
        "\n 3-  Extrato"
        "\n 4 - Criar Conta"
        "\n 5 - Sair")
  
  operacao = int(input("Qual operação deseja realizar? "))
  
  if operacao == 0:
    
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    nascimento = input("Digite a data de nascimento: ")
    
    usuarios = sistema_bancario.criar_usuario(usuarios, cpf, nome, nascimento)
  
  
  elif operacao == 1:
    print("Deposito Selecionado")
    saldo = sistema_bancario.deposito(saldo)
  elif operacao == 2:
    print("Saque Selecionado")
    saldo, limite_diario, extrato = sistema_bancario.saque(saldo, limite_diario, extrato)
  elif operacao == 3:
    print("Extrato Selecionado")
    extrato = sistema_bancario.consulta_extrato(extrato)
  elif operacao == 4:
     numero = input("Digite o número da conta: ")
     usuarios = sistema_bancario.criar_conta(usuarios, cpf, contas, numero, saldo)
     print(usuarios[cpf][conta])

  elif operacao == 5:
    print("Saindo...")
  else:
    print("Operação inválida, tente novamente.")


