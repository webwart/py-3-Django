# Generated by Django 3.2.9 on 2021-11-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20211120_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='ytube_playlist_plid',
            field=models.CharField(max_length=33, null=True, verbose_name='yoTu playlist ID'),
        ),
        migrations.AddField(
            model_name='video',
            name='ytube_playlist_url',
            field=models.CharField(max_length=128, null=True, verbose_name='yoTu playlist URL'),
        ),
        migrations.AddField(
            model_name='video',
            name='ytube_url',
            field=models.CharField(max_length=128, null=True, verbose_name='yoTu Video URL'),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=64, verbose_name='ceo'),
        ),
        migrations.AlterField(
            model_name='video',
            name='category_id',
            field=models.IntegerField(choices=[(1, 'HTML/CSS'), (2, 'JavaScript'), (3, 'Python'), (4, 'Django'), (5, 'Salsa')]),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='youtube_vid',
            field=models.CharField(default='8BDH3ceqKOM', max_length=11, verbose_name='yoTu Video ID'),
        ),
    ]
