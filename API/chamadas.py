import requests
import json


# req = requests.get("http://localhost:5000/alunos")
# js = json.loads(req.content)
# print(js)


# nome="Rodrigo"
# req = requests.get(f"http://localhost:5000/pesquisa/{nome}")
# js = json.loads(req.content)
# print(js)

# id=5
# req = requests.get(f"http://localhost:5000/aluno/{id}")
# js = json.loads(req.content)
# print(js)


body = {"nome": "Rogerio", "idade": "50"}
req = requests.post("http://localhost:5000/insere", data=body)
js = json.loads(req.content)
print(js)


# body = {"id": "20", "nome": "Roberto", "idade": "55"}
# req = requests.put("http://localhost:5000/atualizar", data=body)
# print(req.status_code)


# id = {"id": "20"}
# req = requests.delete("http://localhost:5000/deletar", params=id)
# print(req.status_code)
