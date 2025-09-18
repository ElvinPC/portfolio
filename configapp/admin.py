from django.contrib import admin
from .models import (PortfolioModel, PortfolioTagModel,TechnicalSkillsModel, ProfessionalSkillsModel,ContactModel, ClientModel, EducationModel,WorkLanguageModel, WorkExperienceModel)

admin.site.register([PortfolioModel, PortfolioTagModel,TechnicalSkillsModel, ProfessionalSkillsModel,ContactModel, ClientModel, EducationModel,WorkLanguageModel, WorkExperienceModel])

# configapp/admin.py
from django.contrib import admin
from .models import ResumeModel

@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "email", "phone")
