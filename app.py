from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    # Get form data
    title = request.form['title']
    description = request.form['description']
    category = request.form['category']
    date= request.form['date']
    time=request.form['time']

    # Create task
    task = {
        'title': title,
        'description': description,
        'category': category,
        'date': date,
        'time': time,
        'completed': False
    }

    # Load, append, save
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Form submitted:", title, description, category,date, time)


    return redirect(url_for('index'))


def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
    print("Saved tasks:", tasks)
import os
print("Saving to:", os.path.abspath(DATA_FILE))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'tasks.json')





@app.route('/complete/<int:task_id>')
def complete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/summary')
def summary():
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    pending = total - completed
    return render_template('summary.html', total=total, completed=completed, pending=pending)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    tasks=load_tasks()
    if 0<= task_id<len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route("/edit/<int:task_id>",methods=['GET','POST'])
def edit(task_id):
    tasks= load_tasks()
    if request.method=='POST':
        tasks[task_id]['title']=request.form['title']
        tasks[task_id]['category']=request.form['category']
        tasks[task_id]['description']=request.form['description']
        tasks[task_id]['date']=request.form['date']
        tasks[task_id]['time']=request.form['time']

        save_tasks(tasks)
        return redirect(url_for('index'))
    
    if 0 <=task_id< len(tasks):
        return render_template('edit.html',task=tasks[task_id],task_id=task_id)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
