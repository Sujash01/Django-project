from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    client = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    technologies_used = models.TextField(blank=True)
    team_members = models.ManyToManyField('TeamMember', blank=True)
    case_study_pdf = models.FileField(upload_to='case_studies/', null=True, blank=True)
    featured_image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

class Testimonial(models.Model):
    project = models.ForeignKey(Project, related_name='testimonials', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.author} for {self.project.title}"

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=255, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    project_overview = models.TextField()
    project_goals = models.TextField(blank=True)
    target_audience = models.TextField(blank=True)
    desired_features = models.TextField(blank=True)
    budget = models.CharField(max_length=100, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    additional_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.submitted_at})"

class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    resource_type = models.CharField(max_length=50, choices=[
        ('article', 'Article'),
        ('guide', 'Guide'),
        ('template', 'Template'),
        ('tool', 'Tool'),
        ('best_practice', 'Best Practice'),
        ('other', 'Other'),
    ], default='article')
    url = models.URLField(blank=True)
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ActiveProject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    client = models.ForeignKey('auth.User', related_name='active_projects', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    expected_end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=[
        ('planning', 'Planning'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
    ], default='planning')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProjectUpdate(models.Model):
    project = models.ForeignKey(ActiveProject, related_name='updates', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    deliverables = models.ManyToManyField('Deliverable', blank=True)

    def __str__(self):
        return f"Update for {self.project.name} at {self.timestamp}"

class Deliverable(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='project_deliverables/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    expertise = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    portfolio_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='team_profiles/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)