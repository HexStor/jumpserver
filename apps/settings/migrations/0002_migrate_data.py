# -*- coding: utf-8 -*-
#
from django.db import migrations, connection


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0001_initial"),
    ]
    sql = "INSERT INTO setting(name, value, category, encrypted, enabled, comment) " \
          "SELECT name, value, category, encrypted, enabled, comment from settings"
    settings_table_exist = 'settings' in connection.introspection.table_names()

    operations = []
    if settings_table_exist:
        operations.append(migrations.RunSQL(sql))