from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_blood_bank_adress_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factt', models.TextField()),
            ],
        ),
    ]
