class Produto:
    def __init__(self, id_produto: int, nome: str, preco: float):
        self.id_produto = id_produto
        self._nome = nome   
        self.preco = preco

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self._nome = novo_nome.strip()

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self._preco = novo_preco

    def __repr__(self):
        return f"Produto(id_produto={self.id_produto}, nome='{self._nome}', preco={self._preco:.2f})"
