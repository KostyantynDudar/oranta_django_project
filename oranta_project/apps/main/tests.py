from django.test import TestCase
from django.urls import reverse

class MainPagesTests(TestCase):

    def test_home_page_status_code(self):
        """Главная страница возвращает код 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_page_status_code(self):
        """Страница контактов возвращает код 200"""
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_articles_page_status_code(self):
        """Страница статей возвращает код 200"""
        response = self.client.get(reverse('articles'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        """Проверяем контент главной страницы"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Оформить заявку')

    def test_contacts_page_content(self):
        """Проверяем контент страницы контактов"""
        response = self.client.get(reverse('contacts'))
        self.assertContains(response, 'Контакты')

    def test_articles_page_content(self):
        """Проверяем контент страницы статей"""
        response = self.client.get(reverse('articles'))
        self.assertContains(response, 'Статьи')
