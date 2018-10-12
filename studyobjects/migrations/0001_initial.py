# Generated by Django 2.0.2 on 2018-10-12 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='instructing_courses', to='user.TeamMembership')),
                ('students', models.ManyToManyField(related_name='courses', to='user.TeamMembership')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('is_master', models.BooleanField(default=False)),
                ('termination_type', models.CharField(choices=[('BR', 'BREAK'), ('NOR', 'NORMAL')], max_length=5, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyobjects.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('TODO', 'TODO'), ('INP', 'IN_PROGRESS'), ('CP', 'COMPLETED')], default='TODO', max_length=5)),
                ('description', models.TextField(blank=True, null=True)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyobjects.Assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.TeamMembership')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyobjects.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='UserEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utc_update', models.DateTimeField(auto_now=True)),
                ('utc_created', models.DateTimeField(auto_now_add=True)),
                ('assessment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='studyobjects.Assessment')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='studyobjects.Tag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.TeamMembership')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='session',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyobjects.Task'),
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.TeamMembership'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studyobjects.Course'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.TeamMembership'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='tags',
            field=models.ManyToManyField(to='studyobjects.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'assessment')},
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('course', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together={('course', 'name')},
        ),
    ]
