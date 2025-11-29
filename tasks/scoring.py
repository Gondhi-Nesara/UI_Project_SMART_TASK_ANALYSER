from datetime import datetime, date

def calculate_task_score(task):
    score = 0
    today = date.today()

    # Convert due date
    due_date = task["due_date"]
    if isinstance(due_date, str):
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

    days_until_due = (due_date - today).days

    # 1. Urgency factor
    if days_until_due < 0:
        score += 100  # Overdue
    elif days_until_due <= 3:
        score += 50   # Almost due

    # 2. Importance weight
    score += task.get("importance", 5) * 5

    # 3. Effort quick win bonus
    if task.get("estimated_hours", 1) < 2:
        score += 10

    # 4. Dependency penalty if present
    if task.get("dependencies"):
        score -= 20  # Slight decrease until dependencies are finished

    return score
