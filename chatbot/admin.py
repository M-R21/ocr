from django.contrib import admin


from django.contrib import admin
from .models import FAQ, ClientQuestion

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')

@admin.register(ClientQuestion)
class ClientQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'client', 'admin_assigned', 'created_at', 'answered_at')
    search_fields = ('question',)
    list_filter = ('answered_at', 'admin_assigned')

