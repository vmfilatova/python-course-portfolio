from datetime import datetime

from django.utils import timezone
from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работы.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            description="Job №1 description",
            full_description="Job №1 full_description. " * 5,
            image="images/horseshoe_94961.png",
         )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для работы.

        :return:
        """

        job = Job.objects.get(description="Job №1 description")

        full_description = "Job №1 full_description. " * 5
        self.assertEqual(job.summary(), full_description[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
