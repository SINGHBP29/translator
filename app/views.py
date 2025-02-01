# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import redirect, render
from googletrans import Translator
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.forms import FAQForm

from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all()
    
    def list(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')
        faqs = self.get_queryset()
        data = [{
            'question': faq.get_translated_question(lang),
            'answer': faq.answer
        } for faq in faqs]
        return Response(data)

def faq_view(request):
    faqs = FAQ.objects.all()  # Fetch all FAQ data
    return render(request, 'faq_list.html', {'faqs': faqs})

# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from googletrans import Translator
# from .models import FAQ

# @api_view(['POST'])
def submit_question(request):
    question_text = request.data.get('question')
    selected_lang = request.data.get('language', 'en')

    if not question_text:
        return Response({"error": "Question is required"}, status=400)

    # Translate Question
    translator = Translator()
    translated_text = translator.translate(question_text, dest=selected_lang).text

    # Save to DB
    faq = FAQ.objects.create(question=question_text)
    setattr(faq, f'question_{selected_lang}', translated_text)
    faq.save()

#     return Response({"message": "Question submitted successfully!", "translated_text": translated_text})
def submit_faq(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'submit_faq.html', {'form': form})

# API to retrieve FAQs in selected language
@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    faq_data = []

    for faq in faqs:
        translated_answer = getattr(faq, f'answer_{lang}', faq.answer)
        faq_data.append({"question": faq.question, "answer": translated_answer})

    return Response(faq_data)