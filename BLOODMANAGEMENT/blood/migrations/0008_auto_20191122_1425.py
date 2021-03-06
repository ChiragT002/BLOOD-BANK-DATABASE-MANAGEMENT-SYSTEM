from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0007_auto_20191122_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateblood',
            name='blood_group',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='donateblood',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='needblood',
            name='blood_group',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='needblood',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
