from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
        'id':0,
        'nome': 'Rafael',
     'habilidades': ['Pynthon', 'Flask']
     },
    {
        'id':1,
        'nome': 'Galleani',
      'habilidades':['Python', 'Django']}
]
# Consulta, exclusão e alteração de dados
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem ='Desenvolvedor de ID{} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem ='Erro desconhecido. Procure o Admistrador da API'
            response = {'status':'erro','mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Staus':'Sucesso', 'mensagem':'Registro Excluído'})
# Inserção de dados e consulta da lista completa
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

atividades = [
    {
        'id':0,
        'nome': 'Rafael',
        'tarefa': 'tarefa 1',
        'status':'concluída'
     },
    {
        'id':1,
        'nome': 'Galleani',
        'tarefa':'tarefa 2',
        'status':"pendente"
    }
]
# Consulta, exclusão e alteração de dados
@app.route('/ativ/<int:id>/', methods=['GET','PUT','DELETE'])
def atividades(id):
    if request.method == 'GET':
        try:
            response = atividades[id]
        except IndexError:
            mensagem ='Atividade de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem ='Erro desconhecido. Procure o Admistrador da API'
            response = {'status':'erro','mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        atividades[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        atividades.pop(id)
        return jsonify({'Staus':'Sucesso', 'mensagem':'Registro Excluído'})
# Inserção de dados e consulta da lista completa
@app.route('/ativ/', methods=['POST','GET'])
def lista_atividades():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(atividades)
        dados['id'] = posicao
        atividades.append(dados)
        return jsonify(atividades[posicao])
    elif request.method == 'GET':
        return jsonify(atividades)

if __name__== '__main__':
    app.run(debug = True)

if __name__== '__main__':
    app.run(debug = True)