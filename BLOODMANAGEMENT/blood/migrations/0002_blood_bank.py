from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_bank_name', models.CharField(max_length=120)),
                ('A_plus', models.IntegerField()),
                ('A_minus', models.IntegerField()),
                ('AB_plus', models.IntegerField()),
                ('AB_minus', models.IntegerField()),
                ('B_plus', models.IntegerField()),
                ('B_minus', models.IntegerField()),
                ('O_plus', models.IntegerField()),
                ('O_minus', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=10)),
            ],
        ),
    ]
