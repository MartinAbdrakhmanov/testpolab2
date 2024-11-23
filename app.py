from flask import Flask, request, jsonify
from models import add_task, get_tasks, update_task, delete_task, mark_task_as_completed
from database import init_db

app = Flask(__name__)

# Инициализация базы данных
init_db()

@app.route('/')
def home():
    """Корневая страница."""
    return "<h1>Welcome to the Todo List API!</h1>"

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = get_tasks()
    return jsonify([dict(task) for task in tasks])

@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data['title']
    description = data.get('description', '')
    add_task(title, description)
    return jsonify({'message': 'Task created successfully!'}), 201

@app.route('/task/<int:id>', methods=['PUT'])
def update_task_route(id):
    data = request.get_json()
    title = data['title']
    description = data.get('description', '')
    completed = data.get('completed', 0)
    update_task(id, title, description, completed)
    return jsonify({'message': 'Task updated successfully!'})

@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task_route(id):
    delete_task(id)
    return jsonify({'message': 'Task deleted successfully!'})

@app.route('/task/<int:id>/complete', methods=['PUT'])
def complete_task(id):
    mark_task_as_completed(id)
    return jsonify({'message': 'Task marked as completed!'})

if __name__ == '__main__':
    app.run(debug=True)
