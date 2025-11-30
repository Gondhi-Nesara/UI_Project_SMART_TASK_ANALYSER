![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Gondhi-Nesara/UI_Project_SMART_TASK_ANALYSER)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

# SMART TASKS ANALYZER

Smart Task Analyzer is a lightweight prioritization engine that helps users organize tasks intelligently and focus on what matters most.
Built for **Singularium Internship Task Planning**, designed to **analyze, score, and prioritize tasks intelligently** using a weighted algorithm.

---

## What It Does

- Accepts a list of tasks in **JSON format**.

- Analyzes them based on **importance, deadline, and effort**.

- Generates a **priority score** for each task.

- Displays results in clean **UI cards** showing:

  - **Title**

  - **Due date**

  - **Estimated hours**

  - **Importance level**

  - **Calculated score**

  - **Why it got that score** (explanation)

- Displays results as **animated professional task cards**

- Provides **Top 3 prioritized suggestions** instantly

This project currently runs **locally** on your system using Django — others can test it by running it on their machine, or it can be deployed later to a public server.

---

## Project Structure

Smart_Task_Analyzer
 ┣ backend
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ asgi.py
 ┣ tasks
 ┃ ┣ models.py
 ┃ ┣ views.py
 ┃ ┣ urls.py
 ┃ ┣ serializers.py
 ┃ ┣ scoring.py
 ┃ ┗ tests.py
 ┣ frontend
 ┃ ┣ index.html
 ┃ ┣ styles.css
 ┃ ┗ script.js
 ┣ static
 ┣ db.sqlite3
 ┣ manage.py
 ┣ requirements.txt
 ┗ README.md

---

## Tech stack

**Frontend:** HTML, CSS, JavaScript

**Backend API** handled using Django REST Framework

**Database:** SQLite

**Task scoring logic:** Custom algorithm

---

## How Task Prioritization Works

Each task is scored using a weighted formula:

| Factor | Meaning |
|--------|---------|
| due_date | Closer due dates → higher priority |
| importance | Higher value (1–10) → more important |
| estimated_hours | Smaller hours → faster/efficient task |
| dependencies | Tasks needing others first → lower score |

The backend algorithm processes those and sorts the cards so that highest priority (highest score) comes first.

---

## Why JSON Format?

We use JSON because:

- It allows users to **input multiple tasks at once**
- It is **structured, machine-readable, and easy to scale**
- It can be directly processed by the backend algorithm
- It supports dynamic fields like:
  - dependencies (list)
  - hours, importance, dates, etc.

---

## 🔽 Installation & Run Guide

### 1️⃣ Clone the project

git clone <https://github.com/Gondhi-Nesara/UI_Project_SMART_TASK_ANALYSER>

### 2️⃣ Create and activate virtual environment

python -m venv venv

venv\Scripts\activate

### 3️⃣ Install requirements

pip install -r requirements.txt

### 4️⃣ Apply database migrations

python manage.py makemigrations

python manage.py migrate

### 5️⃣ Collect static files

python manage.py collectstatic

### 6️⃣ Run the server

python manage.py runserver

### 7️⃣ Open in browser

http://127.0.0.1:8000

---

![App UI preview](docs/UI_Preview.png)


## Assessment ready?

Yes! This project meets the task submission requirement by:
✔ Accepting JSON input
✔ Scoring and prioritizing
✔ Returning top 3 suggestions
✔ Displaying them in UI cards
✔ Running without MATLAB/Python dependency in frontend

---

## Example JSON task format:

```json
[
  {
    "title": "Complete UI Integration",
    "due_date": "2025-12-05",
    "importance": 9,
    "estimated_hours": 4.5,
    "dependencies": []
  },
  { 
    "title": "Build API", 
    "due_date": "2025-12-02", 
    "importance": 10, 
    "estimated_hours": 3, 
    "dependencies": [] 
  },
  { 
    "title": "Test API", 
    "due_date": "2025-12-04", 
    "importance": 6, 
    "estimated_hours": 2.5, 
    "dependencies": [] 
  },
  { 
    "title": "Frontend Connect", 
    "due_date": "2025-12-06", 
    "importance": 8, 
    "estimated_hours": 4, 
    "dependencies": [] 
  },
  { 
    "title": "Optimize Score Algo", 
    "due_date": "2025-12-03", 
    "importance": 9, 
    "estimated_hours": 5, 
    "dependencies": [] 
  },
  { 
    "title": "Final Deployment Prep", 
    "due_date": "2025-12-08", 
    "importance": 7, 
    "estimated_hours": 6.5, 
    "dependencies": []
  }
]
```
---

## Privacy Note

This app does NOT store any user identity

Local database only stores task details you input

Nothing is shared with others unless the project is deployed publicly

Even Top 3 suggestions are computed only from your local inputs

---

## Future Scope

Add JWT or session-based user auth

Store tasks per user

Deploy to internet servers (Render / AWS / PythonAnywhere)

Improve UI with React or dashboard upgrades

---
<!-- 
## Built By

Gondhi Nesara

Electronics and Communication Engineering

JSS Academy of Technical Education, Bengaluru

For Singularium Internship Assessment 2025

--- -->

## Need Help?

Feel free to open an issue or connect for improvements or deployment support!

---

Built for Singularium Internship Assessment 2025.