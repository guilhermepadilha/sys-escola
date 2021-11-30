from flask import Flask, request
from flask.json import jsonify
from controller import getById, listar, select, Alunos, inserir, update, delete
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/alunos')
def alunos():
    return jsonify(listar())


@app.route('/pesquisa/<nome>')
def pesquisa(nome):
    return jsonify(select(nome))


@app.route('/aluno/<id>')
def aluno(id):
    return jsonify(getById(id))


@app.route('/insere', methods=['POST'])
def insere():
    json_data = request.get_json(force=True)
    nome = json_data["nome"]
    idade = json_data["idade"]

    aluno = Alunos(nome=nome, idade=idade)
    return inserir(aluno)


@app.route('/deletar', methods=['DELETE'])
def deletar():
    id = request.args.get("id")
    return delete(id)


@app.route('/atualizar', methods=['PUT'])
def atualizar():
    id = request.form.get("id")
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    aluno = Alunos(id=id, nome=nome, idade=idade)
    return update(aluno)

Alunos.create_table()
app.run()
