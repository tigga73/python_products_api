from flask_restful import Resource, reqparse
from models.produto_model import ProdutoModel
import uuid

produtos = [
    {
        'id': '1',
        'nome': 'Placa de Vídeo RTX 3060 Ti 1-Click',
        'marca': 'NVIDIA',
        'preco': 2499.99
    },
    {
        'id': '2',
        'nome': 'Placa de Vídeo RX 6600 CLD 8G',
        'marca': 'AMD',
        'preco': 1389.99
    }
]


class Produtos(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('marca')
    argumentos.add_argument('preco')

    def get(self):
        return {'produtos': [produto.json_parse() for produto in ProdutoModel.query.all()]}

    def post(self):
        dados = Produtos.argumentos.parse_args()

        produto_id = str(uuid.uuid4())
        produto = ProdutoModel(produto_id, **dados)

        produto.save_produto()

        return produto.json_parse(), 201


class Produto(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('marca')
    argumentos.add_argument('preco')

    def get(self, id):
        produto = ProdutoModel.encontrar_produto(id)
        if produto:
            return produto.json_parse(), 200

        return {'message': 'Produto não encontrado'}, 404

    def put(self, id):
        dados = Produto.argumentos.parse_args()

        produto_encontrado = ProdutoModel.encontrar_produto(id)

        if produto_encontrado:
            produto_encontrado.atualizar_produto(**dados)
            produto_encontrado.save_produto()
            return produto_encontrado.json_parse(), 201

        return {'message': 'Produto não encontrado'}, 404

    def delete(self, id):
        produto = ProdutoModel.encontrar_produto(id)
        if produto:
            produto.deletar_produto
            return {'message': 'Produto deletado'}, 202
        return {'message': 'Produto não encontrado'}, 404
