# Generated by Django 5.0.6 on 2024-05-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaygraApp', '0002_categoria_produto_carrinho_endereco_listadesejos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=100)),
                ('mensagem', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]