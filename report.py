import sys
import json

import csv

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

#villages = [
#            'tokuru_62.json',
#            'delantabettu_45.json',
#            'kuttetturu_44.json',
#            'tenkekkaru_42.json',
#            'bajpe_65.json',
#            'kalavaru_64.json',
#            'permude_43.json'
#            ]

names_lookup = {}

with open('translated_owner_names.txt') as translated_owner_names:
    recs = translated_owner_names.read()
    for name_pairs in recs.split('\x01'):
        names = name_pairs.split('\x02')
        if(len(names) == 2):
            names_lookup[names[0]] = names[1]


with open ('suratkal.csv', 'w') as report:
    pen = csv.writer(report, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    pen.writerow(['Owner(EN)', 'Owner(KN)','VILLAGE','SURVEY No', 'SURNOC', 'HISSA No', 'LAND CODE', 'MAIN OWNER No'])
    for village in villages:
        with open(village, encoding='utf8') as json_file:
            data = json.load(json_file)
            #for r in data['d']['Details'].items():
            #    pprint(r)
            recs = json.loads(data['d'])

            for r in recs['Details']:
                owner_kn = r.get('owner' ).replace('\n', '')
                owner_en = names_lookup.get(owner_kn, r['owner']);    
                pen.writerow([owner_en, owner_kn,village.replace('.json',''),r.get('survey_no'), r.get('surnoc'), r.get('hissa_no'), r.get('land_code'), r.get('main_owner_no')])
    else:
        pass
