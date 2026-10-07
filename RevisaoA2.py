#Questao 01:


class ProgressaoAritmetica:
    def __init__(self, n: int, a1: float, r: float):
        self.n = n
        self.a1 = a1
        self.r = r

    def gerar_termos(self):
        termos = []
        for i in range(1, self.n+1):
            an = self.a1 + self.r * (i - 1)
            termos.append(an)
        return termos

    def calcular_soma(self, termos: list)-> float:
        if not termos:
            return 0
        an = termos[-1]
        soma = self.n * (self.a1 + an) / 2
        return soma
    def exibir_PA(self):
        termos = self.gerar_termos()
        soma = self.calcular_soma(termos)
        print("\n=== Progressão Aritmética ===")
        print(f"Termos da PA: {termos}")
        print(f"Soma dos termos da PA: {soma}")
"""
if __name__ == "__main__":
    print(f" Preencha os dados da PA: ")
    n = int(input("Digite o número de termos da PA: "))
    a1 = float(input("Digite o primeiro termo da PA: "))
    r = float(input("Digite a razão da PA: "))
    #Instânciado o objeto:
    pa = ProgressaoAritmetica(n, a1,r)
    pa.exibir_PA()

"""
#Questao 02:

class AnalizarTexto:
    def __init__(self, texto: str):
        self.texto = texto

    def contar_caracteres(self) -> int:
        return len(self.texto)

    def contar_palavras(self) -> int:
        palavras = self.texto.split()
        return len(palavras)

    def contar_frases(self) -> int:
        frases = self.texto.split('.')
        return len([frase for frase in frases if frase.split()])

    def contar_vogais(self) -> int:
        vogais = 'aeiouaáàâãéèêíìîóòôõúùû'
        return sum(1 for caractere in self.texto.lower() if caractere in vogais)

    def contar_consoantes(self) -> int:
        consoantes = 'bcdfghjklmnpqrstvwxyz'
        return sum(1 for caractere in self.texto.lower() if caractere in consoantes)

    def verificar_IFB(self) -> bool:
        return 'ifb' in self.texto.lower()
    
    def cast_maiusculas(self):
        return self.texto.upper()

    def cast_minusculas(self):
        return self.texto.lower()

    def exibir_resultados(self):
        print("\n=== Análise de Texto ===")
        print(f"Texto: {self.texto}")
        print(f"Número de caracteres: {self.contar_caracteres()}")
        print(f"Número de Palavras: {self.contar_palavras()}")
        print(f"Número de Frases: {self.contar_frases()}")
        print(f"Número de Vogais: {self.contar_vogais()}")
        print(f"Número de Consoantes: {self.contar_consoantes()}")
        print(f"Texto na forma maiúscula: {self.cast_maiusculas()}")
        print(f"Texto na forma minúscula: {self.cast_minusculas()}")
        print(f"Contém 'IFB': {'Sim' if self.verificar_IFB() else 'Não'}")

"""
if __name__ == "__main__":
    texto = input("Digite um texto para análise: ")
    analise = AnalizarTexto(texto)
    analise.exibir_resultados()
"""

#Questao 03:

class Criptografia:
    def __init__(self, texto: str):
        self.texto = texto
        self._mapa_cripto = {
            'A': 4, 'a': 2,
            'E': 3, 'e': 6,
            'I': 1, 'i': 10,
            '0': 0, 'o': 0,
            'U': 8, 'u': 16 
        }

    def criptografar(self) -> str:
        texto_criptografado = []
        for caractere in self.texto:
            novo_caractere = self._mapa_cripto.get(caractere, caractere)
            texto_criptografado.append(str(novo_caractere))
        return ''.join(texto_criptografado)

    def exibir_cripto(self):
        print("\n === Sistema Cripto ===")
        print(f"Texto Original: {self.texto}")
        print(f"Texto Criptografado: {self.criptografar()}")
        
"""
if __name__ == "__main__":
        texto = input("Digite um texto para ser criptografado: ")
        cripto = Criptografia(texto)
        cripto.exibir_cripto()    
"""   

#Questao 04:

class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.__nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome do Produto não pode ser vazio.")
        self.__nome = novo_nome.strip()

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O Preço do Produto deve ser maior que zero.")
        self.__preco = float(novo_preco)

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade: int):
        if nova_quantidade <= 0:
            raise ValueError("A Quantidade do Produto deve ser maior que zero.")
        self.__quantidade = int(nova_quantidade)

    def calcular_subtotal(self) -> float:
        return self.__preco * self.__quantidade

class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def adicionar_produto(self, produto: Produto):
        for p in self.__produtos:
            if p.nome.lower() == produto.nome.strip().lower():
                p.quantidade += produto.quantidade
                print(f"Produto '{p.nome}' atualizado no carrinho. Nova quantidade: {p.quantidade}")
                return
        self.__produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao carrinho.")

    def remover_produto(self, produto: Produto):
        for p in self.__produtos:
            if p.nome.lower() == produto.nome.strip().lower():
                self.__produtos.remove(p)
                print(f"Produto '{p.nome}' removido do carrinho.")
                return True
        print(f"Error: Produto '{produto.nome}' não encontrado no carrinho.")
        return False

