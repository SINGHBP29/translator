"""BharatFD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from BharatFD import settings
from django.conf.urls.static import static

from app.views import faq_list, submit_faq, FAQListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', submit_faq, name='submit_faq'),
    path('api/faqs/', faq_list, name='faq_list'),
    path('api/', include('app.urls')),
    path('', FAQListView.as_view(), name='home'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)