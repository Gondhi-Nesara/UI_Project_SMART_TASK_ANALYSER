from datetime import date, datetime

# Configurable weights (easy to tweak)
WEIGHTS = {
    'urgency': 0.4,
    'importance': 0.35,
    'effort': 0.15,
    'dependencies': 0.1
}

def _days_until(due_date):
    if isinstance(due_date, str):
        try:
            due = datetime.strptime(due_date, "%Y-%m-%d").date()
        except:
            return 30
    else:
        due = due_date
    return (due - date.today()).days

def calculate_score(task):
    # return task.importance * 10 - task.hours * 2
    """
    Input: task can be either a Task model instance OR a dict with fields:
           {'due_date': ..., 'importance': int, 'estimated_hours': float, 'dependencies': list}
    Output: numeric score (higher = higher priority)
    """
    # Normalize properties
    if hasattr(task, 'due_date'):
        days = _days_until(task.due_date)
        importance = getattr(task, 'importance', 5)
        hours = getattr(task, 'estimated_hours', 1)
        dependencies = getattr(task, 'dependencies', []) or []
    else:
        # dict-like
        days = _days_until(task.get('due_date'))
        importance = task.get('importance', 5)
        hours = task.get('estimated_hours', 1)
        dependencies = task.get('dependencies', []) or []

    # Urgency score: inverse of days (smaller days => larger score)
    urgency = 1 / (abs(days) + 1)
    # boost for past-due
    if days < 0:
        urgency *= 1.6

    # Importance normalized 0..1
    importance_score = importance / 10.0

    # Effort / quick-win: smaller hours => higher quick-win
    effort_score = 1.0 / (hours + 0.1)

    # Dependencies: more tasks blocked by this one -> more important (we'll treat dependencies length as blocking_count if provided)
    # If dependencies list describes tasks this one depends on, treat as penalty instead.
    # Convention used in this solution: if dependencies > 0 -> this task is blocked by others -> penalize.
    dep_penalty = 0
    if isinstance(dependencies, (list, tuple)) and len(dependencies) > 0:
        # penalize because this task can't be completed until dependencies are resolved
        dep_penalty = len(dependencies)  # number of dependencies

    # Compose final score using weights
    score = (
        WEIGHTS['urgency'] * urgency +
        WEIGHTS['importance'] * importance_score +
        WEIGHTS['effort'] * effort_score -
        WEIGHTS['dependencies'] * (dep_penalty / (dep_penalty + 1))
    )

    # Return scaled score for readability
    return round(score * 100, 3)

