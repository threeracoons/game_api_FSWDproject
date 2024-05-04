from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('videogame', '0001_initial'),  
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',  
            name='release_date',
            field=models.DateField(),  
        ),
    ]
