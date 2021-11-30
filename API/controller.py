from peewee import AutoField, CharField, DecimalField, Model, MySQLDatabase
from playhouse.shortcuts import *

db = MySQLDatabase('maisumcode', user='root',
                   password='', host='localhost', port=3306)


class Alunos(Model):
    id = AutoField()
    nome = CharField(max_length=45, unique=True)
    idade = DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        database = db
        db_table = "alunos"


def listar():
    db.connect()
    alunos = list(Alunos.select().dicts())
    db.close()
    return alunos


def select(nome):
    db.connect()
    alunos = list(Alunos.select().where(Alunos.nome ** f"%{nome}%").dicts())
    db.close()
    return alunos


def getById(id):
    db.connect()
    aluno = Alunos.get_by_id(id)
    db.close()
    return model_to_dict(aluno)


def inserir(aluno):
    db.connect()
    aluno.save()
    db.close()
    return model_to_dict(aluno)


def update(aluno):
    db.connect()
    # aluno.save()
    query = (Alunos.update({Alunos.nome: aluno.nome, Alunos.idade: aluno.idade}).where(
        Alunos.id == aluno.id))
    query.execute()
    db.close()
    return "200"


def delete(id):
    db.connect()
    query = Alunos.delete().where(Alunos.id == id)
    query.execute()
    db.close()
    return "200"
