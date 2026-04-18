from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "🚀 Flask To-Do API Running"

@app.route("/add", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/delete", methods=["POST"])
def delete_task():
    data = request.get_json()
    task = data.get("task")

    if task in tasks:
        tasks.remove(task)
        return jsonify({"message": "Task deleted"})
    
    return jsonify({"message": "Task not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
