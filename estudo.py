from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Loja'
usar = PyMongo(app)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/adm')
def adm():
    return render_template('adm.html')


@app.route('/bancoProdutos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'GET':
        return render_template('bancoProdutos.html')
    else:
        nome = request.form['nome']
        cod = request.form['cod']
        tipo = request.form['tipo']
        tamanho = request.form['tamanho']
        preco = request.form['preco']
        quant = request.form['quant']
        usar.db.Produtos.insert({'Nome': nome, 'Cod': cod, 'Tipo': tipo, 'Tamanho': tamanho, 'Preço': preco,
                                 'Quant': quant})
        return render_template('bancoProdutos.html')


@app.route('/editar', methods=['GET', 'POST'])
def edi():
    if request.method == 'GET':
        n = usar.db.Produtos.count()
        lista = usar.db.Produtos.find().limit(n + 1)
        return render_template('listapro.html', p=lista)
    else:
        codex = request.form['cod']
        usar.db.Produtos.remove({'Cod': codex})
        n = usar.db.Produtos.count()
        ls = usar.db.Produtos.find().limit(n + 1)
        return render_template('listapro.html', p=ls)


@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'GET':
        return render_template('entrar.html')
    else:
        return redirect('/produto')


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
        usar.db.Usuarios.insert({'Nome': nome, 'Endereco': endereco, 'Email': email, 'Telefone': telefone,
                                 'Password': password})
        return redirect('/produto')


@app.route('/listaUser', methods=['GET', 'POST'])
def list():
    if request.method == 'GET':
        n = usar.db.Usuarios.count()
        lis = usar.db.Usuarios.find().limit(n + 1)
        return render_template('listUser.html', l=lis)
    else:
        excluir = request.form['nome']
        usar.db.Usuarios.remove({'Nome': excluir})
        n = usar.db.Usuarios.count()
        lis = usar.db.Usuarios.find().limit(n + 1)
        return render_template('listUser.html', l=lis)


@app.route('/produto', methods=['GET', 'POST'])
def pro():
    if request.method == 'GET':
        numb = usar.db.Produtos.count()
        pro = usar.db.Produtos.find().limit(numb+1)
        return render_template('produtos.html', p=pro)
    else:
        com = request.form['produto']
        pro = usar.db.Produtos.find({'Nome': com})
        return render_template('compra.html', p=pro)


<<<<<<< HEAD
app.run(debug=True)
=======
app.run(debug=True)

>>>>>>> aabdc8e4e7816a312e02a2d3f71aaef1d2e549b3
