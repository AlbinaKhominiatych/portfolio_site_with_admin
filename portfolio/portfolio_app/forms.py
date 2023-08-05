from django import forms
from django.contrib import admin
from .models import Name, Profession, Description, Experience, Photo

"""class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['photo']"""

admin.site.register(Name)
admin.site.register(Profession)
admin.site.register(Description)
admin.site.register(Experience)
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'thumbnail']