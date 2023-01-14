from datetime import datetime
from flask import Flask, render_template, request, redirect
tasks = []

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = {"id": len(tasks) + 1, "content": task_content, "date_created": datetime.utcnow()}
        tasks.append(new_task)
        return redirect('/')
    else:
        return render_template("index.html", tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            del tasks[i]
            break
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    for task in tasks:
        if task["id"] == id:
            if request.method == 'POST':
                task["content"] = request.form['content']
                return redirect('/')
            else:
                return render_template("update.html", task=task)

if __name__ == "__main__":
    app.run(debug=True)