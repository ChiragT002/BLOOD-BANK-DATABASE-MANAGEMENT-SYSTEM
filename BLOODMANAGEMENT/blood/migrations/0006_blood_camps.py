from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0005_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Camps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_camp_name', models.CharField(max_length=120)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('adress_key', models.TextField(default='India')),
            ],
        ),
    ]
