# Generated by Django 2.1.1 on 2018-09-28 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180928_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='id_moeda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Moeda'),
        ),
    ]
