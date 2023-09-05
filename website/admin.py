from django.contrib import admin
from .models import Education, Experience, Certificate


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass
