import numpy as np
import sys

def contaConsumo():
  


  totalConsumo = int(input("informe o valor total do consumo: "))

  percentualServico = int(input("Informe o percentual do serviço, entre 0 e 100: "))
  if percentualServico < 0 or percentualServico > 100 :
    print("Percentual invalido")
    sys.exit()

  qtdPessoas = int(input("Informe o total de pessoas: "))

  if qtdPessoas <= 0:
    print("Quantidade de pessoas Invalida")
    sys.exit() 



  total = (totalConsumo + percentualServico) / qtdPessoas
  total = str(total)
  total = total.replace('.', ',')

  print(f"Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$:{total}")


  
def podeVotar():

  idade = int(input("Informe a idade: "))

  if idade >= 18 and idade < 70:
      print("Tem obrigação de votar.")
  elif idade >=16 and idade < 18 or idade > 70:
      print('Não tem obrigação de votar.')
  elif idade < 16 :
      print("Não tem direito a voto.")






def calculaConcurso():

  nomes = []
  notas = []

  for n in range(5):
    nome = input(f"Informe nome do {n+1}º participante: ")
    nomes.append(nome)
    nota = float(input(f"Informe nota do {n+1}º participante: "))
    notas.append(nota)

  
  nomeGanhador = notas.index(max(notas))
  print(nomeGanhador)
  print(f"O(a) vencedor(a) foi {nomes[nomeGanhador]} com nota {max(notas)}!")



#contaConsumo()
#podeVotar()
calculaConcurso() 