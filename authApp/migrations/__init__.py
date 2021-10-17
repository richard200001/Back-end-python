from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('fechaNacimiento', models.DateField()),
                ('celular', models.IntegerField(default=0, verbose_name='Celular')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('rol', models.CharField(max_length=13, verbose_name='Rol')),
                ('estado', models.BooleanField(default=True)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=8, verbose_name='producto y/o servicio')),
                ('existencia', models.IntegerField(default=0, verbose_name='Existencia')),
                ('lastChangeDate', models.DateTimeField(auto_now_add=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('idInv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to='authApp.inventario')),
                ('idUsu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consulta', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]