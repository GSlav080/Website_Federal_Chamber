# Generated by Django 4.1.3 on 2022-11-27 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_form_nikname_alter_form_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='razdel',
            field=models.CharField(default=1, max_length=150, verbose_name='Раздел'),
            preserve_default=False,
        ),
    ]
