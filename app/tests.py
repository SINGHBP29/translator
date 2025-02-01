from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.
##  model checking
from django.test import TestCase
from app.models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )

    def test_faq_creation(self):
        """Ensure FAQ instance is created correctly."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a Python web framework.")

    def test_translation_fields(self):
        """Check if translations are generated."""
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)

    def test_get_translated_question(self):
        """Ensure the model returns the correct translated question."""
        self.assertEqual(self.faq.get_translated_question('hi'), self.faq.question_hi)
        self.assertEqual(self.faq.get_translated_question('bn'), self.faq.question_bn)
        

## test FAQ API
from rest_framework.test import APITestCase
from django.urls import reverse
# from faqs.models import FAQ

class FAQAPITestCase(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )
        self.url = reverse('faq-list')  # Ensure URL name is correct

    def test_fetch_faqs(self):
        """Check if FAQs are fetched properly."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('question', response.json()[0])

    def test_fetch_faqs_with_translation(self):
        """Ensure API supports multilingual responses."""
        response_hi = self.client.get(f"{self.url}?lang=hi")
        self.assertEqual(response_hi.status_code, 200)
        self.assertEqual(response_hi.json()[0]['question'], self.faq.question_hi)

    def test_empty_faqs(self):
        """Test API response when no FAQs exist."""
        FAQ.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

## test cache
from django.core.cache import cache

class FAQCacheTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )

    def test_cache_translation(self):
        """Check if FAQ translations are cached."""
        cache_key = f'faq_{self.faq.id}_lang_hi'
        self.faq.get_translated_question('hi')  # Trigger caching
        cached_value = cache.get(cache_key)
        self.assertEqual(cached_value, self.faq.question_hi)
