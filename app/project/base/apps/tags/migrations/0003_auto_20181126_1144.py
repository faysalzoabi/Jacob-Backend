# Generated by Django 2.0.3 on 2018-11-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20181126_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlighted_text',
            name='pdf_documents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highlighted_text', to='tags.Pdf_documents', verbose_name='pdf_documents'),
        ),
    ]
