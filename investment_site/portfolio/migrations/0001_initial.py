# Generated by Django 4.2.10 on 2024-02-11 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('symbol', models.CharField(max_length=255, unique=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='DailyStockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_prices', to='portfolio.company')),
            ],
            options={
                'db_table': 'daily_stock_prices',
            },
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='dailystockprice',
            index=models.Index(fields=['date'], name='date_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='dailystockprice',
            unique_together={('company', 'date')},
        ),
    ]
