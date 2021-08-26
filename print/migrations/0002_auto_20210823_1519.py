# Generated by Django 3.2.4 on 2021-08-23 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='print.machinecategory'),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FilePathField()),
                ('uploaded', models.DateTimeField()),
                ('previous', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='print.fablabuser')),
            ],
        ),
    ]