# Generated by Django 4.0 on 2021-12-08 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modify_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='banner_images',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='banner_images',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modify_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='cms',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='cms',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modify_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modify_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by_user', to='User.user'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='modify_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modify_by_user', to='User.user'),
        ),
    ]