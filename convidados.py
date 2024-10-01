# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

convidados = []

for pessoas in range(1, 8):
    nome = input(f"digite o nome do convidado {pessoas}: ")
    convidados.append(nome)
    if pessoas == 7:
        print(f"lista atual de convidados: {convidados}")
remover = input("deseja remover algum convidado da lista? (sim/não): ")
if remover == "sim":
    quem = input("quem voce quer remover?")
    convidados.remove(quem)
    print(f"esse convidado foi removido, nova lista: {convidados}")
else:
    print("nenhum convidado será removido")
