"""

assentos = {
    "Assento - 1": False,
    "Assento - 2": False,
    "Assento - 3": False,
    "Assento - 4": False,
    "Assento - 5": False,
    "Assento - 6": False,
    "Assento - 7": False,
    "Assento - 8": False,
    "Assento - 9": False,
    "Assento - 10": False, 
    }



def exibir_assentos():
 print(f"Mapa de Assentos: ")
 for chave, valor in assentos.items():
  print(f"{chave}: {valor}")

exibir_assentos()

def reservar_assentos():
 reservar = input("Insira o Assento a ser Reservado: ")

"""

"""

def exibir_menu():
    print(" Ranking de Notas")
    print("=*" * 30)
    print("1 - Adicionar Nota")
    print("2 - Ranking por Disciplina")
    print("3 - Melhor Aluno por Disciplina")
    print("4 - Ranking Geral")
    print("5 - Ranking de Notasdo Aluno")
    print("6 - Sair")

def main():
    notas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ")
        if opcao == "1":
            nome = input("Nome do Aluno: ").strip()
            try:
                nota = float(input("Nota do Aluno: "))
            except ValueError:
                print("Nota Inválida. Por favor, insira um número.")
                continue
            disciplina = input("Disciplina: ").strip()
            notas.append({"nome": nome, "nota": nota, "disciplina": disciplina})
        elif opcao == "2":

"""

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.preco = preco            # Utiliza o setter para validação inicial
        self.quantidade = quantidade  # Utiliza o setter para validação inicial

    # --- Getters e Setters para __nome ---
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = novo_nome.strip()

    # --- Getters e Setters para __preco ---
    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = float(novo_preco)

    # --- Getters e Setters para __quantidade ---
    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_qtd: int):
        if nova_qtd < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self.__quantidade = int(nova_qtd)

    # Método utilitário para calcular o subtotal deste produto
    def calcular_subtotal(self) -> float:
        return self.__preco * self.__quantidade

    def __str__(self) -> str:
        return f"{self.__nome} | Preço: R$ {self.__preco:.2f} | Qtd: {self.__quantidade} | Subtotal: R$ {self.calcular_subtotal():.2f}"


class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []  # Lista privada para armazenar os objetos Produto

    def adicionar_produto(self, produto: Produto):
        """Adiciona um novo produto ou atualiza a quantidade se já existir."""
        for p in self.__produtos:
            if p.nome.lower() == produto.nome.lower():
                # Se o produto já existe, apenas incrementa a quantidade
                p.quantidade += produto.quantidade
                print(f"Quantidade do produto '{p.nome}' atualizada com sucesso!")
                return
        
        self.__produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho com sucesso!")

    def remover_produto(self, nome_produto: str) -> bool:
        """Remove um produto do carrinho pelo nome."""
        for p in self.__produtos:
            if p.nome.lower() == nome_produto.strip().lower():
                self.__produtos.remove(p)
                print(f"Produto '{p.nome}' removido do carrinho com sucesso!")
                return True
        print(f"Erro: Produto '{nome_produto}' não encontrado no carrinho.")
        return False

    def calcular_total(self) -> float:
        """Soma o subtotal de todos os produtos do carrinho."""
        return sum(p.calcular_subtotal() for p in self.__produtos)

    def listar_produtos(self):
        """Exibe todos os produtos cadastrados e o valor total."""
        if not self.__produtos:
            print("\nO carrinho está vazio.")
            return

        print("\n--- ITENS NO CARRINHO ---")
        for idx, p in enumerate(self.__produtos, start=1):
            print(f"{idx}. {p}")
        print("-" * 40)
        print(f"TOTAL DA COMPRA: R$ {self.calcular_total():.2f}")


# --- Programa Principal (Menu Interativo) ---
def menu():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n=== GERENCIADOR DE CARRINHO DE COMPRAS ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Visualizar carrinho e total")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            try:
                nome = input("Nome do produto: ").strip()
                preco = float(input("Preço unitário (R$): "))
                quantidade = int(input("Quantidade: "))

                novo_produto = Produto(nome, preco, quantidade)
                carrinho.adicionar_produto(novo_produto)
            except ValueError as e:
                print(f"Erro ao cadastrar produto: {e}")

        elif opcao == "2":
            nome_remover = input("Digite o nome do produto que deseja remover: ")
            carrinho.remover_produto(nome_remover)

        elif opcao == "3":
            carrinho.listar_produtos()

        elif opcao == "4":
            print("\nEncerrando o programa. Obrigado!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()