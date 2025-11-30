from django.test import TestCase
from .scoring import calculate_score
from datetime import date, timedelta

class ScoringTest(TestCase):
    def test_overdue_boost(self):
        t = {'due_date': (date.today() - timedelta(days=5)).isoformat(), 'importance': 5, 'estimated_hours': 2, 'dependencies': []}
        s = calculate_score(t)
        self.assertTrue(s > 0)

    def test_quick_win(self):
        t1 = {'due_date': (date.today() + timedelta(days=10)).isoformat(), 'importance': 5, 'estimated_hours': 0.5, 'dependencies': []}
        t2 = {'due_date': (date.today() + timedelta(days=10)).isoformat(), 'importance': 5, 'estimated_hours': 5, 'dependencies': []}
        self.assertTrue(calculate_score(t1) > calculate_score(t2))
