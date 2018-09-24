# Generated by Django 2.1.1 on 2018-09-24 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('page_title', models.CharField(help_text='Limit it to 60-70 characters', max_length=100)),
                ('page_description', models.CharField(help_text='Limit it to 160-180 characters', max_length=200)),
                ('page_keywords', models.CharField(help_text='Limit it to 10 words', max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('page_image', models.CharField(help_text='HD image preferable', max_length=300)),
                ('page_qualifier', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pub_date', models.DateField(auto_now=True)),
                ('thumbnail', models.CharField(blank=True, help_text='Thumbnail to represent the page', max_length=300, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('eligibility', models.TextField()),
                ('preparation', models.TextField()),
                ('cost', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('page_title', models.CharField(help_text='Limit it to 60-70 characters', max_length=100)),
                ('page_description', models.CharField(help_text='Limit it to 160-180 characters', max_length=200)),
                ('page_keywords', models.CharField(help_text='Limit it to 10 words', max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('page_image', models.CharField(help_text='HD image preferable', max_length=300)),
                ('page_qualifier', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pub_date', models.DateField(auto_now=True)),
                ('thumbnail', models.CharField(blank=True, help_text='Thumbnail to represent the page', max_length=300, null=True)),
                ('internal', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('joined_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_title', models.CharField(help_text='Limit it to 60-70 characters', max_length=100)),
                ('page_description', models.CharField(help_text='Limit it to 160-180 characters', max_length=200)),
                ('page_keywords', models.CharField(help_text='Limit it to 10 words', max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('page_image', models.CharField(help_text='HD image preferable', max_length=300)),
                ('page_qualifier', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pub_date', models.DateField(auto_now=True)),
                ('thumbnail', models.CharField(blank=True, help_text='Thumbnail to represent the page', max_length=300, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('eligibility', models.TextField()),
                ('preparation', models.TextField()),
                ('cost', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('page_title', models.CharField(help_text='Limit it to 60-70 characters', max_length=100)),
                ('page_description', models.CharField(help_text='Limit it to 160-180 characters', max_length=200)),
                ('page_keywords', models.CharField(help_text='Limit it to 10 words', max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('page_image', models.CharField(help_text='HD image preferable', max_length=300)),
                ('page_qualifier', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('pub_date', models.DateField(auto_now=True)),
                ('thumbnail', models.CharField(blank=True, help_text='Thumbnail to represent the page', max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_desktop', models.CharField(help_text='Image to show on desktops', max_length=300)),
                ('url_laptop', models.CharField(blank=True, help_text='Image to show on desktops', max_length=300)),
                ('url_tablets', models.CharField(blank=True, help_text='Image to show on desktops', max_length=300)),
                ('url_mobile', models.CharField(blank=True, help_text='Image to show on desktops', max_length=300)),
                ('image_title', models.CharField(help_text='To be displayed on top of the image', max_length=100)),
                ('image_alt', models.CharField(help_text='To be displayed if image not found and for SEO purposes', max_length=100)),
                ('pub_date', models.DateField(auto_now=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='explorers.Album')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='explorers.ImageSet'),
        ),
        migrations.AddField(
            model_name='event',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='explorers.Contact'),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('email', 'phone')},
        ),
        migrations.AddField(
            model_name='adventure',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='explorers.ImageSet'),
        ),
        migrations.AddField(
            model_name='adventure',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='explorers.Contact'),
        ),
    ]
