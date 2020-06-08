# Generated by Django 2.2.13 on 2020-06-08 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gruppo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Gruppo',
                'verbose_name_plural': 'Gruppi',
            },
        ),
        migrations.CreateModel(
            name='Indagine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titoloIndagine', models.CharField(max_length=20)),
                ('erogatore', models.CharField(max_length=20)),
                ('imgUrl', models.FileField(upload_to='')),
                ('tematica', models.TextField()),
                ('creato_da', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gruppi', models.ManyToManyField(related_name='gruppi_interessati', to='BICAPweb.Gruppo')),
            ],
            options={
                'verbose_name': 'Indagine',
                'verbose_name_plural': 'Indagini',
            },
        ),
        migrations.CreateModel(
            name='Informazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFile', models.CharField(max_length=20)),
                ('fileUrl', models.FileField(upload_to='')),
                ('thumbnailUrl', models.FileField(upload_to='')),
                ('tipoFile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('gruppi', models.ManyToManyField(related_name='gruppi', to='BICAPweb.Gruppo')),
            ],
            options={
                'verbose_name': 'Utente',
                'verbose_name_plural': 'Utenti',
            },
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=20)),
                ('qualtricsUrl', models.CharField(max_length=250)),
                ('compilato', models.BooleanField()),
                ('indagine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionari', to='BICAPweb.Indagine')),
            ],
            options={
                'verbose_name': 'Questionario',
                'verbose_name_plural': 'Questionari',
            },
        ),
        migrations.CreateModel(
            name='Distribuzione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminata', models.BooleanField()),
                ('indagine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utenti', to='BICAPweb.Indagine')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indagini', to='BICAPweb.Utente')),
            ],
            options={
                'verbose_name': 'Distribuzione',
                'verbose_name_plural': 'Distribuzioni',
            },
        ),
        migrations.CreateModel(
            name='UtenteConGruppo',
            fields=[
            ],
            options={
                'verbose_name': 'Utente',
                'verbose_name_plural': 'Utenti',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('BICAPweb.utente',),
        ),
        migrations.CreateModel(
            name='InformazioneQuestionario',
            fields=[
                ('informazione_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BICAPweb.Informazione')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informazioni', to='BICAPweb.Questionario')),
            ],
            options={
                'verbose_name': 'Informazione Questionario',
                'verbose_name_plural': 'Informazioni Questionari',
            },
            bases=('BICAPweb.informazione',),
        ),
        migrations.CreateModel(
            name='InformazioneIndagine',
            fields=[
                ('informazione_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BICAPweb.Informazione')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informazioni', to='BICAPweb.Indagine')),
            ],
            options={
                'verbose_name': 'Informazione Indagine',
                'verbose_name_plural': 'Informazioni Indagini',
            },
            bases=('BICAPweb.informazione',),
        ),
    ]
