# Generated by Django 3.2.8 on 2021-11-04 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendees', models.IntegerField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Contracts',
            new_name='Contract',
        ),
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.client'),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.eventstatus'),
        ),
        migrations.AddField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
