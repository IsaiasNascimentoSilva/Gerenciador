#Author: Isaías Silva
#Vertion: 1.0 
#Date: 24/08/2023
import random

exit = True
while exit:
  print("Digite a Opção")
  print("")
  print("(1) Consultar Senha")
  print("(2) Gerar Senha")
  print("(3) modificar senha")
  option = input("Opção: ")
  if int(option) == 1:
    app = input("Qual Aplicação? ")
    password = input("Digite a senha: ")
    passApp = consult(password)

  elif int(option) == 2:
    app = input("Nome da Aplicação")
    password = gerator()
    print("Senha Gerada: {password} aplicação: {app}")

  elif int(option) == 3:
    prevPassord = input("digite a senha anterior")
    newPassword = input("Digite a nova senha")

def consult(password):
  pass

def gerator():
  pass

def comparator(params):
  pass

def set(params):
  pass

def gat(params):
  pass

def VadationPass(params):
  pass