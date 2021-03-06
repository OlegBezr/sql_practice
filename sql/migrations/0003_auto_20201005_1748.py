# Generated by Django 3.1.2 on 2020-10-05 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0002_auto_20201005_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_id', to='sql.person')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_id', to='sql.person')),
            ],
        ),
        migrations.DeleteModel(
            name='Parents',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
