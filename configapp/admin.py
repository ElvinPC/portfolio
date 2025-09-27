from django.contrib import admin
from .models import (PortfolioModel, PortfolioTagModel,TechnicalSkillsModel, ProfessionalSkillsModel,ContactModel, ClientModel, EducationModel,WorkLanguageModel, WorkExperienceModel)

admin.site.register([PortfolioModel, PortfolioTagModel,TechnicalSkillsModel, ProfessionalSkillsModel, ClientModel,ContactModel, EducationModel,WorkLanguageModel, WorkExperienceModel])

# configapp/admin.py
from django.contrib import admin
from .models import ResumeModel

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "email", "phone")

from django.contrib import admin
from configapp.models import ContactModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')