# Generated by Django 3.1.4 on 2020-12-11 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myquora', '0003_answer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='myquora.question', verbose_name='سوال'),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='myquora.category', verbose_name='دسته\u200cبندی'),
        ),
    ]
