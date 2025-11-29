from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method == "POST":
        try:
            tasks = json.loads(request.body)

            for task in tasks:
                if isinstance(task.get("due_date"), str):
                    task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d").date()

                task["importance"] = task.get("importance", 5)
                task["estimated_hours"] = task.get("estimated_hours", 1)
                task["dependencies"] = task.get("dependencies", [])

                task["score"] = calculate_task_score(task)

            tasks.sort(key=lambda x: x["score"], reverse=True)

            for task in tasks:
                task["due_date"] = task["due_date"].strftime("%Y-%m-%d")

            return JsonResponse(tasks, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

def suggest_tasks(request):
    sample = [
        {"title": "Complete hardware design", "due_date": "2025-11-30", "importance": 9, "estimated_hours": 3, "dependencies": []},
        {"title": "Review API logic", "due_date": "2025-11-29", "importance": 7, "estimated_hours": 1, "dependencies": []},
        {"title": "Fix scoring module", "due_date": "2025-11-28", "importance": 8, "estimated_hours": 2, "dependencies": []},
    ]

    for task in sample:
        if isinstance(task["due_date"], str):
            task["due_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
        task["score"] = calculate_task_score(task)

    sample.sort(key=lambda x: x["score"], reverse=True)

    for task in sample:
        task["due_date"] = task["due_date"].strftime("%Y-%m-%d")

    return JsonResponse(sample[:3], safe=False)
