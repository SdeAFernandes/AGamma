#Revisão Dicionários:
#Definindo um dicionário vazio e o atualizando:
estoque = {}

estoque = {"caneta azul": 10, "caderno": 10, "lapis": 40}
print(f"Estoque Inicial: {estoque}")

# Adicioanar/Modificar items:

chave = "cola"
quantidade = 20 
estoque[chave] = quantidade
print(f"Estoque Atualizado: {estoque}")

chave = "cola"
quantidade = 1
estoque[chave] = quantidade
print(f"Estoque Atualizado: {estoque}")

#remover Itens:
def remover(estoque):
 remover_item = input("Item: ")
 if remover_item in estoque:
    estoque.pop(remover_item)
    print(f"Item: {remover_item} REMOVIDO!!")
    print(f"Estoque Atualizado: {estoque}")
 else:
    print(f"Item: {remover_item} NÃO ENCONTRADO!!")
"""
Listar Itens de um dicionário:
dic.keys() - Retorna uma lista com as chaves do dicionário.
dic.values() - Retorna uma lista com os valores do dicionário.
dic.items() - Retorna uma lista com os pares chave-valor do dicionário.
dic.get(chave) - Retorna o valor associado a uma chave específica. Se a chave nnão existir, retorna None (ou um valor padrão especificado).

"""
#dic.keys()
print(f"\n=== Chaves ===")
for chave in estoque.keys():
  print(f"{chave}")
  #print(f"{chave} - {estoque[chave]}")

#dic.values()
print(f"\n==== Valores ===")
for valor in estoque.values():
  print(f"{valor}")



