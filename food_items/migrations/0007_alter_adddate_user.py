# Generated by Django 4.1 on 2022-11-21 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_items', '0006_adddate_user_alter_adddetail_date_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddate',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
