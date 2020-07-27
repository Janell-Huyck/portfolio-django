from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "synopsis",
        "language",
        "description",
        "site_url",
        "repository",
    )
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Project, ProjectAdmin)
