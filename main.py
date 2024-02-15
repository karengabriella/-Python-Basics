import sistema_bancario


#Operacoes Bancárias

# 1 - Deposito
# 2 - Saque
# 3-  Extrato
# 4 - Sair

#REGRAS: 
 #Limite por saque de 500
 #Limite diario de 3 saques
 #Extrato de valor sacado


operacao = 0
saldo = 0
extrato = 0
limite_diario = 0

while operacao != 4:
  operacao = int(input("Qual operação deseja realizar? "))
  if operacao == 1:
    print("Deposito Selecionado")
    saldo = sistema_bancario.deposito(saldo)
  elif operacao == 2:
    print("Saque Selecionado")
    saldo, limite_diario, extrato = sistema_bancario.saque(saldo, limite_diario, extrato)
  elif operacao == 3:
    print("Extrato Selecionado")
    extrato = sistema_bancario.consulta_extrato(extrato)
  elif operacao == 4:
    print("Saindo...")
  else:
    print("Operação inválida, tente novamente.")
