# from django.db import models
# from ckeditor.fields import RichTextField
# from django.core.cache import cache
# from googletrans import Translator, LANGUAGES

# class FAQ(models.Model):
#     question = models.TextField()
#     answer = RichTextField()
#     question_hi = models.TextField(blank=True, null=True)
#     question_bn = models.TextField(blank=True, null=True)
#     answer_hi = RichTextField(blank=True, null=True)  # Hindi
#     answer_bn = RichTextField(blank=True, null=True)  # Bengali

#     def save(self, *args, **kwargs):
#         translator = Translator()

#         # Translate question to Hindi if not already available
#         if not self.question_hi:
#             try:
#                 translated_hi = translator.translate(self.question, dest='hi').text
#                 if translated_hi:
#                     self.question_hi = translated_hi
#             except Exception as e:  # Catching errors if translation fails
#                 print(f"Error translating question to Hindi: {e}")
        
#         # Translate question to Bengali if not already available
#         if not self.question_bn:
#             try:
#                 translated_bn = translator.translate(self.question, dest='bn').text
#                 if translated_bn:
#                     self.question_bn = translated_bn
#             except Exception as e:  # Catching errors if translation fails
#                 print(f"Error translating question to Bengali: {e}")

#         super().save(*args, **kwargs)  # Call the parent save method to persist the model

#     def __str__(self):
#         return self.question

#     def get_translated_question(self, lang='en'):
#         # Implement caching logic
#         cache_key = f'faq_{self.id}_lang_{lang}'
#         cached_question = cache.get(cache_key)
#         if cached_question:
#             return cached_question

#         translation_map = {
#             'hi': self.question_hi,
#             'bn': self.question_bn,
#         }

#         # Safely fetch the translated text, default to English if translation is not available
#         translated_text = translation_map.get(lang, self.question)
#         if translated_text is None:  # Ensure None is not returned
#             translated_text = self.question
        
#         # Cache the translated question for future requests
#         cache.set(cache_key, translated_text, timeout=3600)
#         return translated_text
from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache

try:
    from googletrans import Translator
except ImportError:
    from deep_translator import GoogleTranslator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    # Multi-language fields
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    answer_hi = RichTextField(blank=True, null=True)  
    answer_bn = RichTextField(blank=True, null=True)  
    
    def translate_text(self, text, target_lang):
        """Translates text using Google Translate API with fallback."""
        if not text:
            return None

        try:
            translator = Translator()
            return translator.translate(text, dest=target_lang).text
        except Exception as e1:
            print(f"googletrans failed: {e1}")

        try:
            return GoogleTranslator(source='auto', target=target_lang).translate(text)
        except Exception as e2:
            print(f"deep_translator failed: {e2}")

        return text  # Fallback to original text if all translations fail

    def save(self, *args, **kwargs):
        """Automatically translate content before saving."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')

        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

    def get_translated_question(self, lang='en'):
        """Returns the translated question based on the requested language."""
        cache_key = f'faq_{self.id}_lang_{lang}'
        cached_question = cache.get(cache_key)
        if cached_question:
            return cached_question

        translation_map = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        translated_text = translation_map.get(lang, self.question)
        cache.set(cache_key, translated_text, timeout=3600)
        return translated_text
