#Exercício 01:
"""

def calcular_custo():
    fabricante = float(input("Custo de fábrica: "))
    distribuidor = 0.12
    impostos = 0.30
    custo_F = fabricante + (fabricante * distribuidor) + (fabricante * impostos)
    print(f"O custo final do automóvel é: RS{custo_F:.2f}")
#Exercício 02:
a = 4
b = 14
print(f"A variável A é: {a}, e a variável B é: {b}")
def trocar_valores(a,b):
    a, b = b, a
    print(f"Após a troca, a variável A é: {a}, e a variável B é: {b}.")

#Exercício 03:
def download_time():
    tamanho = float(input("Digite o tamanho do arquivo em MB: "))
    velocidade = float(input("Digite a velocidade do link em Mbps: "))
    tempo = ((tamanho * 8) / velocidade) / 60
    print(f"O tempo estimado de download é: {tempo:.2f} minutos.")

#Exercício 04:
def calcular_media():
    P1 = float(input("Digite a nota da P1: "))
    P2 = float(input("Digite a nota da P2: "))
    mediaP = (P1 + P2) / 2
    T1 = float(input("Digite a nota do primeiro trabalho: "))
    T2 = float(input("Digite a nota do segundo trabalho: "))
    mediaT = (T1 + T2) / 2
    media_final = (0.8 * mediaP) + (0.2 * mediaT)
    if media_final >= 6:
        print(f"Aluno Aprovado com Nota Final: {media_final:.2f}")
    else:
        print(f"Aluno Reprovado com Nota final: {media_final:.2f}")

#Exercício 05:
def temperatura():
    celsius = float(input("Insira a temperatura em Celsius: "))
    if celsius < 0:
        print("Frio Extremo, no safe")
    elif 0 <= celsius <= 10:
        print("Frio, use casaco")
    elif 11 <= celsius < 25:
        print("Ameno, use roupas leves")
    elif 25 <= celsius < 35:
        print("Quente, use roupas leves e se hidrate")
    elif celsius >= 35:
        print("Muito Quente, saia do Piauí e vá para o Sul.")

#Exercício 06:
Real = float(input("Insira o valor em Reais: "))
Dolar = Real * 0.19
Euro = Real *0.17
Libra = Real * 0.15
Iene = Real * 25
Yuan = Real * 1.33


opcao = 0
while opcao != 6:
    print("Escolha uma opção para conversão:")
    print("1 - Dolar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Iene")
    print("5 - Yuan")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada (1-6): "))

    if opcao == 1:
        print(f"Valor em Dolar: {Dolar:.2f}")
    elif opcao == 2:
        print(f"Valor em Euro: {Euro:.2f}")
    elif opcao == 3:
        print(f"Valor em Libra: {Libra:.2f}")
    elif opcao == 4:
        print(f"valor em Iene: {Iene:.2f}")
    elif opcao == 5:   
        print(f"Valor em Yuan: {Yuan:.2f}")
    elif opcao == 6:
        print("Encerrando o programa...")

#Exercício 06: Segunda forma de realizar o mesmo exercício:
def money_casting():
    Real = float(input("Insira o valor em Reais: "))
    Dolar = Real * 0.19
    Euro = Real *0.17
    Libra = Real * 0.15
    Iene = Real * 25
    Yuan = Real * 1.33

    while True:
        print("\n===Escolha uma opção para conversão:===")
        print("1 - Dolar")
        print("2 - Euro")
        print("3 - Libra")
        print("4 - Iene")
        print("5 - Yuan")
        print("6 - Sair")
        opcao = int(input("Digite a opção desejada (1-6): "))

        match opcao:
            case 1:
                print(f"Valor em Dolar: {Dolar:.2f}")
            case 2:
                print(f"Valor em Euro: {Euro:.2f}")
            case 3:
                print(f"Valor em Libra: {Libra:.2f}")
            case 4:
                print(f"valor em Iene: {Iene:.2f}")
            case 5:
                print(f"Valor em Yuan: {Yuan:.2f}")
            case 6:
                print("Encerrando o programa...")
                break

#Exercício 07:

saldo = 1000

opcao = 0

while opcao != 4:
  print("\n===Escolha uma opção:===")
  print("1 - Consultar Saldo")
  print("2 - Depositar")
  print("3 - Sacar")
  print("4 - Sair")
  opcao = int(input("Digite a opção desejada (1-4): "))

  if opcao == 1:
     print(f"Saldo Atual: RS {saldo:.2f}")
  elif opcao == 2:
     valor_deposito = float(input("Insira o valor a ser depositado: "))
     saldo += valor_deposito
     print(f"Depósito realizado com sucesso! Saldo Atual: RS {saldo:.2f}")
  elif opcao == 3:
     valor_saque = float(input("Insira o valor a ser sacado: "))
     if valor_saque <= saldo:
         saldo -= valor_saque
         print(f"Saque realizado com sucesso! Saldo Atual: RS {saldo:.2f}")
     else:
        print("Saldo Insuficiente, trabalhe mais e tente novamente!")
  elif opcao == 4:
     print("Encerrando a Operação...")

#Exercício 08:

x = float(input("Insira um valor para X: "))
y = float(input("Insira um valor para Y: "))

def potencia(x, y):
 return x ** y

print(f"O valor de X: {x} elevado a Y: {y} é: {potencia(x, y)}")    

#Exercício 09:
def multiplos():

 x = int(input("Insira um valor para X: "))
 print(f"\nOs múltiplos de X: {x}, entre 1 e 100 são: ")
 if x > 0 and x < 100:
  for i in range(1, 101):
     if i % x == 0:
      print(i)

#Exercício 09: Segunda forma de realizar o mesmo exercício:

def multiplos_lista():
 x = int(input("Insira um valor para X: "))
 multiplos_list = list(range(x, 101, x))
 print(f"\nOs múltiplos de X: {x}, entre 1 e 100 são: {multiplos_list}")

def multiplos_listaF():
  x = int(input("Insira um valor para X: "))
  if x > 0 and x <= 100:
      multiplos_list2 = [i for i in range(x, 101, x) ]
      print(f"Os multiplos de X: {x}, entre 1 e 100 são: {multiplos_list2}")
  else:
    print("Insira um valor válido para X (entre 1 e 100)")

#Exercício 10:

tarefas = []
def adicionar_tarefa():
    nova_tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(nova_tarefa)

def remover_tarefa():
    if len(tarefas) == 0:
        print("Não há tarefas para remover.")
        return
    print(f"Lista de Tarefas: {', '.join(f'{i} - {tarefa}' for i, tarefa in enumerate(tarefas, start = 1))}")
    remover = input("Digite a tarefa que deseja remover:")
    if remover in tarefas:
        tarefas.remove(remover)
        print(f"Tarefa '{remover}' removida com sucesso.")
    else:
        print(f"Tarefa '{remover}' não encontrada na lista.")

def exibir_tarefas():
    if len(tarefas) == 0:
        print("Não há tarefas na lista.")
    else:
        print(f"Lista de Tarefas: {', '.join(f'{i} - {tarefa}' for i, tarefa in enumerate(tarefas, start = 1))}")
      

while True:
    print("\n===lista de Tarefas===")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefas")
    print("3 - Exibir Lista de Tarefas")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada (1-4): "))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        remover_tarefa()
    elif opcao == 3:
        exibir_tarefas()
    elif opcao == 4:
        print("Encerrando o programa...")
        break


"""