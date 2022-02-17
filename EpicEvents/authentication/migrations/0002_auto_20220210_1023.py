# Generated by Django 4.0.1 on 2022-02-08 10:31
from django.core.management.sql import emit_post_migrate_signal

from django.db import migrations


def create_groups(apps, schema_migration):
    # Code nécessaire pour être sûr que les permissions sont créées
    emit_post_migrate_signal(verbosity=1, interactive=False, db='default')

    # Récupération de modèles
    UserTeam = apps.get_model('authentication', 'UserTeam')
    EventStatus = apps.get_model('CRMapp', 'EventStatus')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Création des statuts d'événement
    EventStatus.objects.create(status='En traitement')
    EventStatus.objects.create(status='Fini')

    # Création d'un utilisateur pour chaque futur groupe
    admin = UserTeam.objects.create_superuser(username='Yonohi', password='djangosuper', email='loic.planat2@gmail.com')
    user_sale = UserTeam.objects.create_user(username='testsale', password='djangosuper', team='Sale')
    user_support = UserTeam.objects.create_user(username='testsupport', password='djangosuper', team='Support')
    user_management = UserTeam.objects.create_user(username='testmanagement', password='djangosuper', team='Management')

    # Liste des permissions possibles
    view_client = Permission.objects.get(codename='view_client')
    add_client = Permission.objects.get(codename='add_client')
    change_client = Permission.objects.get(codename='change_client')
    delete_client = Permission.objects.get(codename='delete_client')

    view_contract = Permission.objects.get(codename='view_contract')
    add_contract = Permission.objects.get(codename='add_contract')
    change_contract = Permission.objects.get(codename='change_contract')
    delete_contract = Permission.objects.get(codename='delete_contract')

    view_event = Permission.objects.get(codename='view_event')
    add_event = Permission.objects.get(codename='add_event')
    change_event = Permission.objects.get(codename='change_event')
    delete_event = Permission.objects.get(codename='delete_event')

    safe_permissions = [
        view_client,
        view_contract,
        view_event
    ]

    # Création des groupes
    sale = Group(name='Vente')
    support = Group(name='Support')
    management = Group(name='Gestion')
    sale.save()
    support.save()
    management.save()

    # Ajout des permissions de base
    sale.permissions.set(safe_permissions)
    support.permissions.set(safe_permissions)
    management.permissions.set(safe_permissions)

    # Permissions spécifiques à l'équipe Vente
    sale.permissions.add(add_client,
                         change_client,
                         add_contract,
                         change_contract,
                         add_event,
                         change_event)

    # Permissions spécifiques à l'équipe Support
    support.permissions.add(change_event)

    # Permissions spécifiques à l'équipe Gestion
    management.permissions.add(add_client,
                               change_client,
                               delete_client,
                               add_contract,
                               change_contract,
                               delete_contract,
                               add_event,
                               change_event,
                               delete_event)

    for user in UserTeam.objects.all():
        if user.team == 'Sale':
            sale.user_set.add(user)
        elif user.team == 'Management':
            management.user_set.add(user)
        elif user.team == 'Support':
            support.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('CRMapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
