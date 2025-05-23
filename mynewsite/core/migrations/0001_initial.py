# Generated by Django 5.2 on 2025-05-04 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='project_deliverables/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('project_overview', models.TextField()),
                ('project_goals', models.TextField(blank=True)),
                ('target_audience', models.TextField(blank=True)),
                ('desired_features', models.TextField(blank=True)),
                ('budget', models.CharField(blank=True, max_length=100)),
                ('timeline', models.CharField(blank=True, max_length=100)),
                ('additional_notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('client', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('technologies_used', models.TextField(blank=True)),
                ('case_study_pdf', models.FileField(blank=True, null=True, upload_to='case_studies/')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('resource_type', models.CharField(choices=[('article', 'Article'), ('guide', 'Guide'), ('template', 'Template'), ('tool', 'Tool'), ('best_practice', 'Best Practice'), ('other', 'Other')], default='article', max_length=50)),
                ('url', models.URLField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('category', models.CharField(blank=True, max_length=100)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('published_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('expertise', models.TextField(blank=True)),
                ('skills', models.CharField(blank=True, max_length=255)),
                ('portfolio_url', models.URLField(blank=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='team_profiles/')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('expected_end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('in_progress', 'In Progress'), ('on_hold', 'On Hold'), ('completed', 'Completed')], default='planning', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_gallery/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('deliverables', models.ManyToManyField(blank=True, to='core.deliverable')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='core.activeproject')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='team_members',
            field=models.ManyToManyField(blank=True, to='core.teammember'),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='core.project')),
            ],
        ),
    ]
