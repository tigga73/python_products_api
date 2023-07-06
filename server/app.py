from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_restx import fields
from flask_restx import Resource, reqparse
from models.produto_model import ProdutoModel
import uuid

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app, version='1.0', title='API produtos',
          description='Operações referentes a Produto')


ns = api.namespace('Produtos', description='Operações de produtos')

produto_modelo = api.model('Produtos', {
    'id': fields.Integer(readOnly=True, description='Identificador do produto'),
    'nome': fields.String(required=True, description='Nome do produto'),
    'marca': fields.Integer(required=True, description='Marca do produto'),
    'preco': fields.Float(required=True, description='Preço do produto')
})


@ns.route('/')
class Produtos(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True,
                            help="O campo 'nome' não pode ser deixado em branco")
    argumentos.add_argument('marca', type=str, required=True,
                            help="O campo 'marca' não pode ser deixado em branco")
    argumentos.add_argument('preco', type=float, required=True,
                            help="O campo 'preco' não pode ser deixado em branco")

    @ns.doc('lista_produtos')
    def get(self):
        produtos = ProdutoModel.query.all()
        return [produto.json_parse() for produto in produtos]

    @ns.doc('cria_produto')
    @ns.expect(produto_modelo)
    def post(self):
        dados = Produtos.argumentos.parse_args()

        produto_id = str(uuid.uuid4())
        produto = ProdutoModel(produto_id, **dados)

        try:
            produto.save_produto()
        except:
            return {'message': 'Ocorreu um erro ao tentar salvar um novo produto'}, 500

        return produto.json_parse(), 201


@ns.route('/<string:id>')
@ns.response(404, 'Produto não encontrado')
@ns.param('id', 'Identificador do Produto')
class Produto(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('marca')
    argumentos.add_argument('preco')

    @ns.doc('obtem_produto')
    def get(self, id):
        produto = ProdutoModel.encontrar_produto(id)
        if produto:
            return produto.json_parse(), 200

        return {'message': 'Produto não encontrado'}, 404

    @ns.doc('atualiza_produto')
    @ns.expect(produto_modelo)
    def put(self, id):
        dados = Produto.argumentos.parse_args()

        produto_encontrado = ProdutoModel.encontrar_produto(id)

        if produto_encontrado:
            produto_encontrado.atualizar_produto(**dados)
            try:
                produto_encontrado.save_produto()
            except:
                return {'message': 'Ocorreu um erro ao tentar atualizar o produto'}, 500

            return produto_encontrado.json_parse(), 201

        return {'message': 'Produto não encontrado'}, 404

    @ns.doc('deleta_produto')
    def delete(self, id):
        produto = ProdutoModel.encontrar_produto(id)
        if produto:
            try:
                produto.deletar_produto()
            except:
                return {'message': 'Ocorreu um erro ao tentar deletar o produto'}, 500
            return {'message': 'Produto deletado'}, 202
        return {'message': 'Produto não encontrado'}, 404


@app.before_request
def cria_banco():
    banco.create_all()


api.add_resource(Produtos, '/produtos')
api.add_resource(Produto, '/produtos/<string:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
