# Generated by Django 5.0.6 on 2024-05-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('CPF_CNPJ', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
