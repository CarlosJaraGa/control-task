# Generated by Django 3.0.4 on 2022-09-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Cargo_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=100, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True)),
                ('correo_electronico', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=255, null=True)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'Empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Estado_tarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('inicio', models.DateTimeField(blank=True, null=True)),
                ('termino', models.DateTimeField(blank=True, null=True)),
                ('repetible', models.BooleanField(null=True)),
                ('activo', models.IntegerField()),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadInterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Unidad_interna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_column='NombreUsuario', max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='FechaCreacion')),
                ('last_login', models.DateTimeField(auto_now_add=True, db_column='LastLogin')),
                ('is_staff', models.BooleanField(db_column='is_staff', default=False)),
                ('is_active', models.BooleanField(db_column='Estado', default=True)),
                ('is_profesional', models.BooleanField(db_column='is_profesional', default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
