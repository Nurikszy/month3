# Generated by Django 4.0.1 on 2022-01-24 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_post_date_book_update_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=35)),
                ('projects', models.IntegerField()),
                ('nameEX', models.TextField()),
                ('expert', models.CharField(choices=[('EXEMINATION OF EDUCATIONAL PROJECTS', 'EXEMINATION OF EDUCATIONAL PROJECTS'), ('experemential work', 'experemential work'), ('adout education development programs', 'adout education development programs'), ('legal documents', 'legal documents')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='BookComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_comment', to='book.book')),
            ],
        ),
    ]
