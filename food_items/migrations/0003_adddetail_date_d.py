# Generated by Django 4.1 on 2022-11-07 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0002_adddate_rename_fooditem_adddetail_add_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddetail',
            name='date_d',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food_items.adddate'),
        ),
    ]
