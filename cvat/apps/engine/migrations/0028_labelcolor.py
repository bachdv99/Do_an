# Generated by Django 2.2.13 on 2020-08-11 11:26
from django.db import migrations, models
from cvat.apps.dataset_manager.formats.utils import get_label_color

def alter_label_colors(apps, schema_editor):
    Label = apps.get_model('engine', 'Label')
    Task = apps.get_model('engine', 'Task')

    for task in Task.objects.all():
        labels = Label.objects.filter(task_id=task.id).order_by('id')
        label_names = list()
        for label in labels:
            label.color = get_label_color(label.name, label_names)
            label_names.append(label.name)
            label.save()

class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0027_auto_20200719_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='color',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.RunPython(
            code=alter_label_colors,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
