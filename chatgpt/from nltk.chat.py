from nltk.chat.util import Chat, reflections

ciftler = [

        ["Benim adım (.*)", ["Merhaba %1, nasılsın?"]] ,

        ['yaşın kaç',['yaşım yok ama 2023 yılında üretildim']],
        ['(.*)(memleket|nerelisin|hangi şehir)',['Türkiye/İZMİR']],

        ['bugün hava nasıl?',['bugün hava güzel görünüyor']],

        ['(hey|hello|nasılsın|naber|ne var ne yok|)', ['selam, naber?', 'hey nasılsın?', 'nasıl gidiyor?', 'keyfin yerinde mi?']] ,
]

yansimalar={
    'merhaba' : 'merhaba, nasılsın',
    'gittim'  : 'gittin',

}


chat = Chat(ciftler, reflections)
chat.converse(quit='bitti')
#print(chat._substitute("merhaba"))