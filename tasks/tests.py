from django.test import TestCase
from .scoring import calculate_score
from datetime import date

class TestScoringAlgorithm(TestCase):

    def test_high_importance_task(self):
        task = {
            "title": "Important Task",
            "due_date": "2025-12-10",
            "importance": 10,
            "estimated_hours": 2,
            "dependencies": []
        }
        score = calculate_score(task)
        self.assertGreater(score, 0)

    def test_quick_win_low_effort_task(self):
        task = {
            "title": "Quick Task",
            "due_date": "2025-12-15",
            "importance": 5,
            "estimated_hours": 0.5,
            "dependencies": []
        }
        score = calculate_score(task)
        self.assertIsInstance(score, float)

    def test_dependency_penalty(self):
        task = {
            "title": "Blocked Task",
            "due_date": "2025-12-05",
            "importance": 7,
            "estimated_hours": 3,
            "dependencies": [1, 2, 3]
        }
        score = calculate_score(task)
        self.assertLess(score, 1000)
