class SalvarProd:  # Classe para salvar as informações dos produtos
    def __init__(self, nome, quant, fra, cod):
        self.cod = cod
        self.nome = nome
        self.quant = quant
        self.fra = fra


class SalvarFabri:  # Classe para salvar as informações dos fabricantes
    def __init__(self, cod, nome):
        self.cod = cod
        self.nome = nome
