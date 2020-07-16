# Importando as bibliotecas para ser utilizadas
from json import dump
from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

# Aplicando o Flask a uma variavel para ser utilizado
app = Flask(__name__)
# Configurando o MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Loja'
mongo = PyMongo(app)


# Pagina inicial
@app.route('/')
def pagInicial():
    return render_template('index.html')


# Cadastro de novo usuarios
@app.route('/usuarios', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('usuarios.html')
    else:
        nome = request.form['nome']
        endereco = request.form['endereco']
        email = request.form['email']
        telefone = request.form['telefone']
        password = request.form['passaword']
        mongo.db.Usuarios.insert({'Nome': nome, 'Endereço': endereco, 'Email': email, 'Telefone': telefone,
                                 'Password': password})
        return redirect(url_for('produtos'))


# Entrar na loja
@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'GET':
        return render_template('entrar.html')
    else:
        return redirect(url_for('produtos'))


# Catalogo de produtos
@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'GET':
        lis = mongo.db.Produtos.find()
        return render_template('produtos.html', p=lis)


# pagina de Compra
@app.route('/compra/<id>')
def compras(id):
        lis = mongo.db.Produtos.find({'_id': ObjectId(id)}) # Quando eu coloco o find_one
        # aparece varios objetos
        return render_template('compra.html', p=lis)


# Pagina do admistrador
@app.route('/adm')
def admim():
    return render_template('adm.html')


# Cadastro de um novo produto
@app.route('/bancoProdutos', methods=['GET', 'POST'])
def editarProduto():
    if request.method == 'GET':
        return render_template('bancoProdutos.html')
    else:
        nome = request.form['nome']
        cod = request.form['cod']
        tipo = request.form['tipo']
        tamanho = request.form['tamanho']
        preco = request.form['preco']
        quant = request.form['quant']
        mongo.db.Produtos.insert({'Nome': nome, 'Cod': cod, 'Tipo': tipo, 'Tamanho': tamanho, 'Preço': preco,
                                 'Quant': quant})
        return render_template('bancoProdutos.html')


# Editar produtos
@app.route('/editar')
def edi():
    lista = mongo.db.Produtos.find()
    return render_template('listapro.html', p=lista)


# Excluir produtos
@app.route('/excluir/<id>')
def excluirProduto(id):
    mongo.db.Produtos.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('edi'))


# Listar Usuarios
@app.route('/listaUser')
def userEdit():
    lista = mongo.db.Usuarios.find()
    return render_template('listUser.html', l=lista)


# Excluir Usuarios
@app.route('/excluiruser/<id>')
def excluirUsuer(id):
    mongo.db.Usuarios.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('userEdit'))


if __name__ == '__main__':
    app.run(debug=True)