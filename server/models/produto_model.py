from sql_alchemy import banco


class ProdutoModel(banco.Model):
    __tablename__ = 'produtos'

    id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    marca = banco.Column(banco.String(80))
    preco = banco.Column(banco.Float(precision=2))

    def __init__(self, id, nome, marca, preco):
        self.id = id
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def json_parse(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'marca': self.marca,
            'preco': self.preco
        }

    @classmethod
    def encontrar_produto(cls, id):
        hotel = cls.query.filter_by(id=id).first()
        if hotel:
            return hotel
        return None

    def save_produto(self):
        banco.session.add(self)
        banco.session.commit()

    def atualizar_produto(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def deletar_produto(self):
        banco.session.delete(self)
        banco.session.commit()
