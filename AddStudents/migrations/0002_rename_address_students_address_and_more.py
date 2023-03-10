# Generated by Django 4.1.5 on 2023-02-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AddStudents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='mobile',
            new_name='Mobile',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='rollno',
            new_name='Rollno',
        ),
        migrations.RemoveField(
            model_name='students',
            name='course',
        ),
        migrations.RemoveField(
            model_name='students',
            name='doj',
        ),
        migrations.AddField(
            model_name='students',
            name='Course',
            field=models.CharField(choices=[('python', 'Python'), ('java', 'Java'), ('c++', 'C++'), ('web design', 'Web Design'), ('dot net', 'Dot Net'), ('testing', 'Testing'), ('data science', 'Data Science'), ('data analytics', 'Data Analytics')], default='', max_length=20),
        ),
    ]
