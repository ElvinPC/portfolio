from django.db import models
from django.utils.translation import gettext_lazy as _


class PortfolioTagModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class PortfolioModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    language = models.CharField(max_length=128, verbose_name=_("language"))
    url = models.CharField(max_length=255, verbose_name=_("url"))
    image1 = models.ImageField(upload_to='portfolio', verbose_name=_("image1"))
    image2 = models.ImageField(upload_to='portfolio', verbose_name=_("image2"))

    tags = models.ManyToManyField(
        PortfolioTagModel,
        verbose_name=_("tag"),
        related_name="portfolios"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')


class TechnicalSkillsModel(models.Model):
    lang = models.CharField(max_length=64, verbose_name=_("language"))
    value = models.IntegerField(verbose_name=_("percentage %"))

    def __str__(self):
        return self.lang

    class Meta:
        verbose_name = _("TechnicalSkill")
        verbose_name_plural = _('TechnicalSkills')


class ProfessionalSkillsModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_("title"))
    value = models.IntegerField(verbose_name=_("percentage %"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("ProfessionalSkill")
        verbose_name_plural = _('ProfessionalSkills')


class ContactModel(models.Model):
    first_name = models.CharField(max_length=128, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=128, verbose_name=_("last_name"))
    email = models.CharField(max_length=128, verbose_name=_("email"))
    message = models.TextField(verbose_name=_("message"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


class ClientModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    job = models.CharField(max_length=128, verbose_name=_("job"))
    description = models.TextField(verbose_name=_("description"))
    image = models.ImageField(upload_to="client", verbose_name=_("image"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")


class EducationModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    year = models.CharField(max_length=128, verbose_name=_("year"))
    description = models.TextField(verbose_name=_("description"))
    url = models.CharField(max_length=255, verbose_name=_("url"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")


class WorkLanguageModel(models.Model):
    title = models.CharField(max_length=128, verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Work Language")
        verbose_name_plural = _("Work Languages")


class WorkExperienceModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("name"))
    year = models.CharField(max_length=128, verbose_name=_("year"))
    url = models.CharField(max_length=255, verbose_name=_("url"))

    languages = models.ManyToManyField(
        WorkLanguageModel,
        verbose_name=_("languages"),
        related_name="work_experiences"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experiences")


from django.db import models
from django.utils.translation import gettext_lazy as _

class ResumeModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("F.I.O"))
    position = models.CharField(max_length=255, verbose_name=_("Lavozim"))
    description = models.TextField(verbose_name=_("Qisqacha tavsif"))
    skills = models.TextField(verbose_name=_("Ko‘nikmalar (vergul bilan ajrating)"))
    experience = models.TextField(verbose_name=_("Ish tajribasi"))
    education = models.TextField(verbose_name=_("Ta’lim"))
    email = models.CharField(max_length=255, verbose_name=_("Email"))
    phone = models.CharField(max_length=50, verbose_name=_("Telefon"))
    github = models.URLField(blank=True, null=True, verbose_name=_("GitHub"))
    linkedin = models.URLField(blank=True, null=True, verbose_name=_("LinkedIn"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Rezume")
        verbose_name_plural = _("Rezume")
