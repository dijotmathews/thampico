import sys
from google.cloud import translate_v3beta1 as translate

client = translate.TranslationServiceClient()

#export GOOGLE_APPLICATION_CREDENTIALS='/home/dijo/dev/learn/Enforcement/enforcement-c0db214466b6.json' 

project_id = 'enforcement'
#text = u'62ನೇ ತೋಕೂರು ಗ್ರಾಮದ ಪಂಚಾಯತ್ ಅಭಿವೃದ್ದಿ ಅಧಿಕಾರಿ'
source_language_code = 'kn'
target_language_code = 'en'
location = 'global'

parent = client.location_path(project_id, location)
names = []
with open('own1.txt', encoding='utf8') as owner:
    names = owner.read().split('\x01')



for name in names:
    response = client.translate_text(
        parent=parent,
        contents=[name],
        mime_type='text/plain',
        source_language_code=source_language_code,
        target_language_code=target_language_code )

    for translation in enumerate(response.translations):
        t = str(translation[1]).replace('\n', '').split('"')
        print(name+'\x02'+t[1]+'\x01', end='')



#^A




#print(u'Text: {}'.format(text))
#print(u'Translation: {}'.format(translation['translatedText']))