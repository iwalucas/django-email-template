# Generated by Django 2.2.3 on 2019-07-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmailTemplate', '0002_auto_20190719_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='subject',
            field=models.CharField(default='CHANGE ME', max_length=255, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
