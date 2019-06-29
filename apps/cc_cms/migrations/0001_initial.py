# Generated by Django 2.1.7 on 2019-04-20 15:12

import cc_cms.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('type', models.CharField(default='COL', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicText',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cc_cms.Content')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            bases=('cc_cms.content',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cc_cms.Content')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('intro', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(editable=False, max_length=250, unique=True)),
                ('thumbnail', models.ImageField(blank=True, max_length=250, null=True, upload_to=cc_cms.models.upload_path)),
            ],
            bases=('cc_cms.content',),
        ),
        migrations.AddField(
            model_name='columnssection',
            name='content',
            field=models.ManyToManyField(blank=True, related_name='sections', to='cc_cms.Content'),
        ),
    ]