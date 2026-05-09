from django.db import models


class MainPage(models.Model):
    # Hero section
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()

    # Profile
    profile_image = models.URLField(blank=True, null=True)

    # CTA buttons
    resume_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    # About
    about_title = models.CharField(
        max_length=200,
        default="About Me"
    )
    about_description = models.TextField(blank=True)

    # Skills
    skills = models.TextField(
        blank=True,
        help_text="Python, Django, DRF, PostgreSQL..."
    )

    # Experience stats
    years_experience = models.PositiveIntegerField(default=0)
    total_projects = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)

    # Contact
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)

    # SEO
    page_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)

    # Control
    is_active = models.BooleanField(default=True)

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title