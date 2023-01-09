import json

from src.task_schema import TaskSchema
from src.database import Database

class TaskController:

    def create_task(task: TaskSchema):
        try:
            db = Database.connect_db()
            cursor = db.cursor()

            sql_query = 'INSERT INTO tasks (title, description) VALUES(?, ?)'

            title = task['title']
            description = task['description']

            cursor.execute(sql_query, [title, description])
            db.commit()
            
            # retorna a tarefa criada
            result = TaskController.get_task_by_id(cursor.lastrowid)
           
            db.close()

            return result
        except Exception as error:
            return error

    def get_all_tasks():
        try:
            db = Database.connect_db()
            cursor = db.cursor()
            
            cursor.execute(f'SELECT * FROM tasks')
            tasks = []

            for task in cursor.fetchall():
                tasks.append({
                    'id':task[0],
                    'title':task[1],
                    'description':task[2]
                })

            db.close()

            return tasks
        except Exception as error:
            return error

    def get_task_by_id(id: int):
        try:
            db = Database.connect_db()
            cursor = db.cursor()
            
            cursor.execute(f'SELECT * FROM tasks WHERE id={int(id)}')
            db.commit()
            task = cursor.fetchone()
          
            db.close()

            return task
        except Exception as error:
            return error


    
