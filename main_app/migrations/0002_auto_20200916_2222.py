# Generated by Django 3.1 on 2020-09-16 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='role',
            field=models.CharField(choices=[('V', 'Villager'), ('W', 'Werewolf'), ('T', 'Tanner'), ('S', 'Seer'), ('V', 'Villager'), ('R', 'Robber'), ('M', 'Troublemaker'), ('D', 'Drunk')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='game',
            name='card',
        ),
        migrations.AddField(
            model_name='game',
            name='card',
            field=models.ManyToManyField(to='main_app.Card'),
        ),
        migrations.AlterField(
            model_name='game',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='room',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='stage',
            field=models.CharField(choices=[('1', 'SETUP'), ('2', 'See Cards'), ('3', 'Villager'), ('4', 'Night Werewolf'), ('5', 'Night Seer'), ('6', 'Night Robber'), ('7', 'Troublemaker'), ('8', 'Night Drunk'), ('99', 'Complete')], default=0, max_length=2),
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameConditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Alive'), ('E', 'Executed'), ('M', 'Murdered'), ('C', 'Consumed')], default=0, max_length=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
