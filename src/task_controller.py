from src.task_schema import TaskSchema
from src.database import Database

class TaskController:


    def get_all_tasks():

        try:

            db = Database.connect_db()
            cursor = db.cursor()
            
            cursor.execute(f'SELECT * FROM tasks')

            tasks = cursor.fetchall()

            print(tasks)

            result = []

            for task in tasks:
                result.append(task)

            return result

        except Exception as error:
            return error
    
