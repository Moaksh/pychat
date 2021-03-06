# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-01 13:37
from __future__ import unicode_literals

from django.db import migrations
import json

def forwards(apps, schema_editor):
    ch_m = apps.all_models['chat']
    Message = ch_m['message']

    with open('old_smileys_info.json') as old_file:
        data_old = json.load(old_file)

    with open('chat/static/smileys/info.json') as new_file:
        data_new = json.load(new_file)

    def find_old_entry(alt):
        for k in data_old:
            for smile in data_old[k]:
                if data_old[k][smile]['text_alt'] == alt:
                    return smile
        raise Exception("Not {} found")

    output = {}

    for k in data_new:
        for smile in data_new[k]:
            entry = find_old_entry(smile['alt'])
            output[json.dumps(entry)] = smile['code']
    messages = Message.objects.all()
    updated_count = 0
    updated_smileys = 0
    for mess in messages:
        output_content = ""
        for char in mess.content:
            get = output.get(json.dumps(char))
            if get is not None:
                updated_smileys+=1
                output_content += get
            else:
                output_content += char
        if mess.content != output_content:
            mess.content = output_content
            mess.save(update_fields=["content"])
            updated_count += 1
    print("Updated " + str(updated_count) + " , total smielys: " + str(updated_smileys))


class Migration(migrations.Migration):

    dependencies = [('chat', '0005_add_symbol_20170707_1213'), ]

    operations = [
        migrations.RunPython(forwards, hints={'target_db': 'default'}),
    ]
