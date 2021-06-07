# Generated by Django 3.1.2 on 2021-06-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('DOB', models.DateField(null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(1, 'I will earn 0 coins; and the other person will earn 0 coins'), (2, 'I will earn 0 coins; and the other person will earn 2 coins'), (3, 'I will earn 2 coins; and the other person will earn 0 coins'), (4, 'I will earn 1 coin; and the other person will earn 1 coin')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('R', 'Red'), ('B', 'Blue')], max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, default='')),
            ],
        ),
    ]