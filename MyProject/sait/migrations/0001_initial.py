# Generated by Django 4.2.5 on 2023-10-28 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('auction', models.BooleanField(help_text='Отметьте,если торг уместен', verbose_name='торг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлённая дата')),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisments/', verbose_name='изображение')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'db_table': 'advertisement',
            },
        ),
    ]
