# Generated by Django 4.2.4 on 2023-10-02 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_sub_categories_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.sub_categories",
            ),
        ),
    ]
