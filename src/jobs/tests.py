from django.test import TestCase

from jobs.models import Job


class JobTestCase(TestCase):
    """
    Тестирование функций работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="path",
            description="description",
            content="content" * 100,
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для работы.

        :return:
        """

        job = Job.objects.get(image="path")

        content = "content" * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
