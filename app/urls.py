from django.urls import path
from .views import faq_view, submit_question, FAQListView
# from .views import submit_faq, faq_list
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('api/app/', FAQListView.as_view(), name='faq-list'),
    path('app/', faq_view, name='faq-view'),
    path('api/submit-question/', submit_question, name='submit-question')
]