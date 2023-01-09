from flask import Flask, jsonify, request
from src.task_controller import TaskController


app = Flask(__name__)


@app.route('/tasks', methods=['POST'])
def create_task():
    try: 
        task = request.get_json('task')

        result = TaskController.create_task(task)
        print(result)

        return jsonify({
            'status_code': 200,
            'message': 'Tarefa criada com sucesso',
            'task': result
        }), 200
    
    except Exception as error:
        return jsonify({
            'status_code': 500,
            'message': 'Erro ao cadastrar a tarefa',
            'error': str(error)
        }), 500


@app.route('/tasks', methods=['GET'])
def get_tasks():
    try: 
        tasks = TaskController.get_all_tasks()
        return jsonify({
            'status_code': 200,
            'tasks': tasks
        }), 200
        
    except Exception as error:
        return jsonify({
            'status_code': 500,
            'message': 'Erro ao buscar as tarefas',
            'error': str(error)
        }), 500


