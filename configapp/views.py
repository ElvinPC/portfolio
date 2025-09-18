from typing import Any

from django.http import request
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from configapp import models
from configapp.forms import ContactForm, UserLoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect

from configapp.models import PortfolioTagModel


class PortfolioView(FormMixin, ListView):
    template_name = 'index.html'
    model = models.PortfolioModel
    context_object_name = 'posts'
    form_class = ContactForm

    def get_success_url(self):
        return reverse_lazy('pages:home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tech_skills'] = models.TechnicalSkillsModel.objects.all()
        context['pro_skills'] = models.ProfessionalSkillsModel.objects.all()
        context['tags'] = models.PortfolioTagModel.objects.all()
        context['clients'] = models.ClientModel.objects.all()
        context['educations'] = models.EducationModel.objects.all()
        context['works'] = models.WorkExperienceModel.objects.all()
        context['languages'] = models.WorkLanguageModel.objects.all()
        portfolio = models.PortfolioModel.objects.first()  # birinchi portfoliodan CV olish
        context['cv_file'] = portfolio.cv.url if portfolio and portfolio.cv else None

        return context


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('pages:home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('pages:home')
def logout_view(request):
    logout(request)
    return redirect('/')

# from django.http import HttpResponse
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from io import BytesIO
#
# from .models import PortfolioModel, TechnicalSkillsModel, ProfessionalSkillsModel, EducationModel, WorkExperienceModel
#
# def download_resume(request):
#     """
#     Baza ma'lumotlaridan PDF rezume yaratish
#     """
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=(595, 842))  # A4
#
#     styles = getSampleStyleSheet()
#     story = []
#
#     # Sarlavha
#     story.append(Paragraph("Rezume", styles["Title"]))
#     story.append(Spacer(1, 12))
#
#     # Portfolio
#     story.append(Paragraph("Portfolio", styles["Heading2"]))
#     for p in PortfolioModel.objects.all():
#         story.append(Paragraph(f"<b>{p.title}</b> ({p.language})", styles["Normal"]))
#         story.append(Paragraph(p.description, styles["Normal"]))
#         story.append(Spacer(1, 6))
#
#     story.append(Spacer(1, 12))
#
#     # Technical Skills
#     story.append(Paragraph("Texnik ko'nikmalar", styles["Heading2"]))
#     data = [["Til", "Foiz"]]
#     for skill in TechnicalSkillsModel.objects.all():
#         data.append([skill.lang, f"{skill.value}%"])
#     table = Table(data, colWidths=[200, 100])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
#         ('ALIGN', (1, 1), (-1, -1), 'CENTER')
#     ]))
#     story.append(table)
#     story.append(Spacer(1, 12))
#
#     # Professional Skills
#     story.append(Paragraph("Professional ko'nikmalar", styles["Heading2"]))
#     data = [["Ko'nikma", "Foiz"]]
#     for skill in ProfessionalSkillsModel.objects.all():
#         data.append([skill.title, f"{skill.value}%"])
#     table = Table(data, colWidths=[200, 100])
#     table.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
#         ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
#         ('ALIGN', (1, 1), (-1, -1), 'CENTER')
#     ]))
#     story.append(table)
#     story.append(Spacer(1, 12))
#
#     # Education
#     story.append(Paragraph("Ta'lim", styles["Heading2"]))
#     for edu in EducationModel.objects.all():
#         story.append(Paragraph(f"<b>{edu.name}</b> ({edu.year})", styles["Normal"]))
#         story.append(Spacer(1, 6))
#
#     # Work Experience
#     story.append(Paragraph("Ish tajribasi", styles["Heading2"]))
#     for work in WorkExperienceModel.objects.all():
#         story.append(Paragraph(f"<b>{work.name}</b> ({work.year})", styles["Normal"]))
#         story.append(Spacer(1, 6))
#
#     doc.build(story)
#     buffer.seek(0)
#
#     response = HttpResponse(buffer, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="rezume.pdf"'
#     return response
# configapp/views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import ResumeModel

def download_resume(request):
    # Admin panelda kiritilgan eng oxirgi rezumeni olib kelamiz:
    resume = ResumeModel.objects.last()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"<b>{resume.full_name}</b>", styles['Title']))
    elements.append(Paragraph(resume.position, styles['Heading2']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Tavsif:</b> {resume.description}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Ko‘nikmalar:</b> {resume.skills}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Ish tajribasi:</b> {resume.experience}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Ta’lim:</b> {resume.education}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"📧 {resume.email}  📞 {resume.phone}", styles['Normal']))
    if resume.github:
        elements.append(Paragraph(f"GitHub: {resume.github}", styles['Normal']))
    if resume.linkedin:
        elements.append(Paragraph(f"LinkedIn: {resume.linkedin}", styles['Normal']))

    doc.build(elements)
    return response
