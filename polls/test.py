import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_question_publish_date(self):
        """
        publish_date is realtime?
        """
        future_question = Question("maybe fast")
        self.assertEqual(future_question.publish_date.day, timezone.now().day)
