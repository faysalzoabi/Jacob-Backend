# Generated by Django 2.0.3 on 2018-11-22 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('datapoint', models.CharField(max_length=200, verbose_name='datapoint')),
                ('field_type', models.CharField(max_length=200, verbose_name='field_type')),
                ('domain_value', models.CharField(max_length=200, verbose_name='domain_value')),
                ('description_gbr', models.TextField(verbose_name='description_gbr')),
                ('description_FR', models.TextField(verbose_name='description_fr')),
            ],
        ),
        migrations.CreateModel(
            name='Highlighted_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_text', models.CharField(max_length=1000, verbose_name='file_name')),
                ('document_tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlighted_text', to='tags.Document_tags', verbose_name='document_tags')),
            ],
        ),
        migrations.CreateModel(
            name='Pdf_documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.FileField(upload_to='reports')),
            ],
        ),
        migrations.AddField(
            model_name='highlighted_text',
            name='pdf_documents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='highlighted_text', to='tags.Pdf_documents', verbose_name='pdf_documents'),
        ),
        migrations.AddField(
            model_name='document_tags',
            name='pdf_documents',
            field=models.ManyToManyField(related_name='document_tags', to='tags.Pdf_documents', verbose_name='pdf_documents'),
        ),
    ]