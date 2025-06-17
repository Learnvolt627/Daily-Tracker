# Daily Tracker

A simple Flask-based task management web app that allows you to:

* ✅ Add, edit, complete, and delete daily tasks
* 🗓️ Assign a date and time to each task
* 🗂️ Categorize tasks
* 📊 View a summary of completed and pending tasks

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/Daily-Tracker.git
cd Daily-Tracker
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser and go to: `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
Daily-Tracker/
│
├── app.py                 # Main Flask app
├── tasks.json             # Data file for storing tasks
├── requirements.txt       # List of required Python packages
└── templates/
    ├── index.html         # Home page
    ├── edit.html          # Edit task page
    └── summary.html       # Task summary page
```

---

## ✍️ Features

* Add new tasks with title, description, category, date, and time.
* Edit existing tasks.
* Mark tasks as completed.
* Delete tasks.
* View a summary of total, completed, and pending tasks.

---

## 🛠️ Tech Stack

* **Backend**: Flask (Python)
* **Frontend**: HTML, Bootstrap 5
* **Storage**: JSON file

---

## 📌 To Do / Future Features

* Add user authentication (login/signup)
* Move from JSON to SQL (SQLite or MySQL)
* Add filters for viewing tasks by category or date
* Deploy to Render/Heroku

---

## 📄 License

This project is open-source and free to use.

