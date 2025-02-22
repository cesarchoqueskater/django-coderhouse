# Generated by Django 5.1.6 on 2025-02-22 11:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('tags', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
