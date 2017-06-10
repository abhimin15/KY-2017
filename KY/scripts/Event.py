CategoryList = [ ['NATRAJ (DANCE)',
                  ['BLISS', 'CUT-A-RUG','ECSTASY'],],
                ['ABHINAY (THEATRE)',
                 ['STAGE PLAY COMPETITION', 'MONO ACT COMPETITION','STREET PLAY COMPETITION']],
                ['BANDISH (INDIAN MUSIC)',
                 ['SUR','YUGAL','SANLAYAN','KRITI','ADVAITA']],
                ['TOOLIKA (FINE ARTS)',
                 ['RAPID FIRE','SOAP CARVING','SPOIL THE TEES!','PAPER COSTUME DESIGNING','CLAY MODELLING']],
                ['MIRAGE (FASHION SHOW)',
                 ['FASHION SHOW','MISS KY',]],
                ['ENQUIZTA (QUIZ)',
                 ['India Quiz','90s-Themed Quiz','SpEnt Quiz','Biz Tech Quiz']],
                ['CROSSWINDZ (WESTERN MUSIC)',
                 ['CROSSWINDZ']],
                ['SAMWAAD (LITERARY EVENTS)',
                 ['SCRIPTURESQUE', 'BATTLEFRONT', 'SHIPWRECK COVE', 'The Legend of Sir Speak-A-Lot',"A Jester's Court","What's The Word?",'VAAD VIVAAD', 'ALFAAZ', 'HINDI CREATIVE WRITING' ]],
                ['INFORMAL EVENTS',
                 ['KARAOKE NIGHT', 'FREE JAM','BEAT BOXING', 'JAM (Just A Minute)', 'CHARADES', 'POTPOURRI' ]],
]

file=open("Event.csv",'wb')
for i in CategoryList:
    file.write(str(i[0])+"\n")
    for j in i[1]:
        file.write(str(j)+"\n")
    # file.write("\n")
