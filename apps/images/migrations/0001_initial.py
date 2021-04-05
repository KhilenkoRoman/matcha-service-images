# Generated by Django 3.1.6 on 2021-03-29 17:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('thumbnail', models.ImageField(null=True, upload_to='thumbnails/')),
            ],
        ),
    ]
