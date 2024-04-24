import re

def criar_usuario(usuarios, cpf, nome, nascimento):
  
  cpf = re.sub(r'\D', '', cpf)
  
  if cpf in usuarios:
    print("Usuário já cadastrado")
  else:
    usuarios[cpf] = cpf
    usuarios[cpf] = {'nome': nome, 'nascimento': nascimento}
  return usuarios


def criar_conta(usuario, cpf, contas, numero, saldo):
  
  if cpf in contas:
    print("Conta já cadastrada")
  else:
    contas[cpf] = cpf
    contas[cpf] = {'numero': numero, 'saldo': saldo}
    usuario[cpf]['conta'] = contas[cpf]
  return usuario

def deposito(saldo):
  valor = int(input("Qual valor irá depositar?  "))
  if(valor <= 0):
    print("Valor inválido, deposite um valor positivo.")
  else:
    saldo = saldo + valor
    print("Depósito realizado com sucesso.")
    print("Saldo atual: ", saldo)
    return saldo



def saque(saldo, limite_diario, extrato):
  valor = int(input("Qual valor irá sacar?  "))
  
  if(limite_diario >= 3):
    print("Limite diário excedido.")
    return saldo, limite_diario, extrato
  else:
    
    if(valor > 500 or valor > saldo):
      print("Valor inválido, saque não pode ser maior que o saldo ou maior que 500.")
      print("Limite diário: ", limite_diario)
      print("Saldo: ", saldo)
      return saldo, limite_diario, extrato

    else:
      saldo = saldo - valor
      extrato = extrato + valor
      limite_diario += 1
      print("Saque realizado com sucesso.")
      print("Limite diário: ", limite_diario)
      print("Saldo: ", saldo)

      return saldo, limite_diario, extrato
    

def consulta_extrato(extrato):
  print("Extrato: ", extrato)
  return extrato