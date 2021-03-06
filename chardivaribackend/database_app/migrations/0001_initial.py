# Generated by Django 2.1 on 2018-09-10 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('password', models.CharField(max_length=264)),
                ('phone', models.PositiveIntegerField()),
                ('create_Date', models.DateField(verbose_name='Create Date')),
                ('modeified_Date', models.DateField(editable=False, verbose_name='Modified Date')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(choices=[('A', 'Apartment'), ('H', 'House')], max_length=1)),
                ('listing_type', models.CharField(choices=[('R', 'Rent'), ('S', 'Sell')], max_length=1)),
                ('square', models.FloatField(verbose_name='Square meter')),
                ('bedroom', models.SmallIntegerField(verbose_name='Bedroom No.')),
                ('bath', models.SmallIntegerField(verbose_name='Bath No.')),
                ('postal', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('parking', models.BooleanField(verbose_name='Has Parking')),
                ('furnished', models.BooleanField(verbose_name='Is Furnished')),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('create_Date', models.DateField(editable=False, verbose_name='Create Date')),
                ('modeified_Date', models.DateField(editable=False, verbose_name='Modified Date')),
                ('availability', models.DateField(verbose_name='Availability date')),
                ('price', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.City')),
                ('list_owener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.A_User', verbose_name='Post Owner')),
            ],
            options={
                'ordering': ['-create_Date'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.Province'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.Province'),
        ),
    ]
