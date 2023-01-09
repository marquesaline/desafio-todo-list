from flask import Flask, jsonify
from src.task_controller import TaskController


app = Flask(__name__)

@app.route('/tasks/', methods=['GET'])
def get_tasks():
    try: 
        tasks = TaskController.get_all_tasks()
        print(tasks)
        return jsonify({
            'status_code': 200,
            'tasks': tasks
        }), 200
        
    except Exception as error:
        return jsonify({
            'error': str(error),
            'message': 'Erro ao buscar as tarefas',
            'status_code': 500
        }), 500


