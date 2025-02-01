from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FAQ

# admin.site.register(FAQ)
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'question_bn')
    search_fields = ('question',)
    fields = ('question','answer', 'answer_hi', 'answer_bn') # CKEditor enabled
    
