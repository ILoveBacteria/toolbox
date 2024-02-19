from django.contrib import admin

from website.models import Certificate, Company, Education, Experience


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
