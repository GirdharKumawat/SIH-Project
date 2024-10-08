# Generated by Django 5.1.1 on 2024-09-19 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('specialization_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=50)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('publications_count', models.PositiveIntegerField()),
                ('previous_interview_experience_years', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('BSc', 'Bachelor of Science'), ('MSc', 'Master of Science'), ('PhD', 'Doctor of Philosophy')], max_length=10)),
                ('field', models.CharField(max_length=255)),
                ('institute', models.CharField(max_length=255)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='Core.expert')),
            ],
        ),
        migrations.CreateModel(
            name='DomainExpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain_expertise', to='Core.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=255)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='industries', to='Core.expert')),
            ],
        ),
        migrations.CreateModel(
            name='IndustryProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=255)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='industry_projects', to='Core.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='Core.expert')),
            ],
        ),
    ]
