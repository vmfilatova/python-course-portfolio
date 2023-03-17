from datetime import datetime

from django.utils import timezone
from django.test import TestCase

from blog.models import Blog


class BlogTestCase(TestCase):
    """
    Тестирование функций блога.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Blog.objects.create(
            title="Blog №1 title",
            content="Blog №1 content. " * 5,
            image="images/horseshoe_94961.png",
            publication_date=datetime(2023, 3, 16, tzinfo=timezone.utc),
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для блога.

        :return:
        """

        blog = Blog.objects.get(title="Blog №1 title")

        content = "Blog №1 content. " * 5
        self.assertEqual(blog.summary(), content[:100] + "...")
        self.assertEqual(blog.publication_date_format(), "Mar 16 2023")
        self.assertEqual(str(blog), f'Объект "Сообщение блога" (id={blog.pk})')
