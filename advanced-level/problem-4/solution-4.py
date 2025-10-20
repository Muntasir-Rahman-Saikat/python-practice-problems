from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of tasks
tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Build a REST API"}
]

# GET: Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST: Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify({"message": "Task added successfully!"}), 201

# DELETE: Remove a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({"message": f"Task {task_id} deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
