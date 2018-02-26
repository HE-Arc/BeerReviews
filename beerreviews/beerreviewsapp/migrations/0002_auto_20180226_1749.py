# Generated by Django 2.0.2 on 2018-02-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerreviewsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='imgsrc',
            field=models.CharField(default='https://cdn4.iconfinder.com/data/icons/proglyphs-food/512/Beer-512.png', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together={('name',)},
        ),
        migrations.AlterUniqueTogether(
            name='maker',
            unique_together={('name',)},
        ),
        migrations.AlterUniqueTogether(
            name='style',
            unique_together={('name',)},
        ),
    ]
