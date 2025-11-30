from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Task
from .scoring import calculate_score

def _days_until(due_date):
    today = datetime.utcnow().date()
    return (due_date - today).days

@api_view(['POST'])
def analyze_tasks(request):   
    data = request.data
    if not isinstance(data, list):
        return Response({"error": "Request body must be a JSON list of tasks"}, status=status.HTTP_400_BAD_REQUEST)

    Task.objects.all().delete()

    result = []
    for i, t in enumerate(data):
        title = t.get("title", f"Task {i+1}")
        due = t.get("due_date")
        importance = int(t.get("importance", 5))
        hours = float(t.get("estimated_hours", 1.0))
        deps = t.get("dependencies", [])

        due_date = None
        try:
            due_date = datetime.strptime(due, "%Y-%m-%d").date()
        except:
            due_date = datetime.utcnow().date()

        saved = Task.objects.create(
            title=title,
            due_date=due_date,
            importance=importance,
            estimated_hours=hours,
            dependencies=deps
        )

        score = calculate_score(saved)

        explanation = f"Due: {saved.due_date} | Importance: {saved.importance} | Effort: {saved.estimated_hours}h | Dependencies: {len(deps)} | Score: {score}"

        result.append({
            "id": saved.id,
            "title": saved.title,
            "due_date": saved.due_date.isoformat(),
            "importance": saved.importance,
            "estimated_hours": saved.estimated_hours,
            "score": score,
            "explanation": explanation
        })

    result.sort(key=lambda x: x["score"], reverse=True)
    return Response(result)


@api_view(['GET'])
def suggest_tasks(request):
    tasks = Task.objects.all()
    scored = []
    for t in tasks:
        score = calculate_score(t)
        scored.append({
            "id": t.id,
            "title": t.title,
            "due_date": t.due_date.isoformat(),
            "importance": t.importance,
            "estimated_hours": t.estimated_hours,
            "score": score,
            "explanation": f"Due {t.due_date.isoformat()}, importance {t.importance}, effort {t.estimated_hours}h, score {score}"
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    top3 = scored[:3]
    suggestions = [s["explanation"] for s in top3]

    return Response({"top": top3, "suggestions": suggestions})

