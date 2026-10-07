#Questao 02: Carrinho de Compras

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.__preco = float(preco)
        self.__quantidade = int(quantidade)

    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = novo_nome.strip()

    @property
    def preco(self) -> float:
        return self.__preco
    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = float(novo_preco)

    @property
    def quantidade(self) -> int:
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, nova_qtd: int):
        if nova_qtd < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        self.__quantidade = int(nova_qtd)

    def subtotal(self) -> float:
        return self.__preco * self.__quantidade

    def __str__(self) -> str:
        return f"{self.__nome} | Preço: RS {self.__preco:.2f} | Quantidade: {self.__quantidade} | Subtotal: RS {self.subtotal():.2f}"

class CarrinhoDeCompras:
        def __init__(self):
            self.__produtos = [] # Lista para armazenar os Objetos da classe Produto

        def adicionar_produto(self, produto: Produto):
            for p in self.__produtos:
                if p.nome.lower() == produto.nome.lower():
                    p.quantidade += produto.quantidade
                    print(f"Quantidade do produto '{p.nome}' Atualizada para {p.quantidade} Unidades.")
                    return
            self.__produtos.append(produto)
            print(f"Produto: '{produto.nome}' Adicionado ao Carrinho")

        def remover_produto(self, nome_produto: str) -> bool:
            for p in self.__produtos:
                if p.nome.lower() == nome_produto.strip().lower():
                    self.__produtos.remove(p)
                    print(f"Produto: '{p.nome}' Removido do Carrinho")
                    return True
            print(f"Produto: '{nome_produto}' Não Encontrado no Carrinho")
            return False

        def total_carrinho(self) -> float:
            return sum(p.subtotal() for p in self.__produtos)

        def exibir_carrinho(self):
            if not self.__produtos:
                print(f"O seu Carrinho está vazio, por favor inicie suas compras.")
            print("\n CARRNHO DE COMPRAS: ")
            for idx, p in enumerate(self.__produtos, start=1):
                print(f"{idx}. {p}")
                print("-" * 40)
                print(f"Total da Compra: RS {self.total_carrinho():.2f}")

# Menu do Carrinho de Compras

def menu():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n--- Menu de Compras ---")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Exibir Carrinho")
        print("4. Sair")
        opcao = input("Escolha uma Opção (1-4): ").strip()

        if opcao == "1":
            try:
                nome = input("Nome do Produto: ").strip()
                preco = float(input("Preço da Unidade (RS): "))
                quantidade = int(input("Quantidade: "))

                novo_produto = Produto(nome, preco, quantidade)
                carrinho.adicionar_produto(novo_produto)
            except ValueError as e:
                print(f"Erro ao Adicionar Produto: {e}")
        elif opcao == "2":
            remover_item = input("Nome do Produto a ser Removido: ")
            carrinho.remover_produto(remover_item)
        elif opcao == "3":
            carrinho.exibir_carrinho()
        elif opcao == "4":
            print("Encerrando o Programa. Obrigado pela Preferência, Volte Sempre!")
            break
        else:
            print("Opção Inválida. Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    menu()

            
        