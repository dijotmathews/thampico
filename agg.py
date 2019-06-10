import json;
from pprint import pprint

from google.cloud import translate
# coding: utf-8 -*-
owners = []

villages = ['badagekkaru_35.json',
            'baikampadi_53.json',
            'bajpe_65.json',
            'bala_63.json',
            'chelyaru_48.json',
            'delantabettu_45.json',
            'hosabettu_51.json',
            'idya_50.json',
            'kalavaru_64.json',
            'katipalla.json',
            'kavuru_59.json',
            'kenjaru_66.json',
            'kulayi_52.json',
            'kunjattabailu_61.json',
            'kuttetturu_44.json',
            'madhya_47.json',
            'malavuru_67.json',
            'marakada_50.json',
            'mudushedde_75.json',
            'padushedde_76.json',
            'panamburu_54.json',
            'panjimogaru_58.json',
            'permude_43.json',
            'suratkal_49.json',
            'surinje_46.json',
            'tanneerubavi_55.json',
            'tenkekkaru_42.json',
            'tokuru_62.json']

for village in villages:
    with open(village, encoding='utf-8') as json_file:
        data = json.load(json_file)
        #for r in data['d']['Details'].items():
        #    pprint(r)
        recs = json.loads(data['d'])

        for r in recs['Details']:
            print('\x01'+r['owner']+'\x01')


    