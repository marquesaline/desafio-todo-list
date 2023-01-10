<h1 align="center">
  Desafio Lacrei - Lista de Tarefas
</h1>

## 1. Tecnologias utilizadas
- Python
- Flask

## 2.  Instalação da aplicação

Depois de clonar o repositório na sua máquina, é só seguir esses passos:

* Create venv
    ```
    $ python -m venv venv
    ```
* Ativando o ambiente virtual
   
    Para ativar o ambiente virtual no Linux:
    ```
    $ source venv/bin/activate
    ```
    Para ativar o ambiente virtual no Windows:
    ```
    $ .\venv\Scripts\activate
    ```
  Após o comando inserido, deve aparecer o nome do ambiente virtual

* Install requirements
    ```
    pip install -r requirements.txt
    ```
* Run
    ```
    python main.py
    ```
  A aplicação vai está disponível em http://localhost:5000

## 3.  Como usar a API?

É possível fazer as requisições através das seguintes rotas:

```
GET http://localhost:5000/tasks #retorna todas as tarefas cadastradas

POST http://localhost:5000/tasks #cdastra uma nova tarefa
    Content-Type: application/json" 
    '{"title":"título da tarefa", "description": "descrição da tarefa"}'
```