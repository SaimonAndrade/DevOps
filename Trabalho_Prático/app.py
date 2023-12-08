import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

app = Flask(__name__)
load_dotenv()

# Simulando um banco de dados simples com uma lista
tarefas = [
    {"id": 1, "titulo": "Ler um livro", "concluida": False},
    {"id": 2, "titulo": "Estudar programação", "concluida": False}
]

# Rota para listar todas as tarefas
@app.route('/', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

# Rota para criar uma nova tarefa
@app.route('/', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# Rota para atualizar uma tarefa
@app.route('/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == tarefa_id), None)
    if not tarefa:
        return jsonify({'mensagem': 'Tarefa não encontrada'}), 404
    dados = request.get_json()
    tarefa.update(dados)
    return jsonify(tarefa)

# Rota para deletar uma tarefa
@app.route('/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'}), 200

if __name__ == '__main__':
    app.run(host= '0.0.0.0' , port= os.getenv("PORT", "3000"))
