from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib import parse

Num = 23
resolved_songs = {}
resolved = {}
unresolved = {}

def fill_resolved_songs():
    f = open("billboard_song_names.txt","r",encoding="utf-8").readlines()
    for line in f:
        line = line.split('(')[0].strip()
        resolved_songs[line] = 1

    return

def NRBcrwal(song_name,name,fname):
    targetUrl = "https://m.search.naver.com/search.naver?where=m&query="+parse.quote(name)
    targetRequest = Request(targetUrl)
    response = urlopen(targetRequest)
    responseText = response.read()
    global resolved_songs,resolved, unresolved

    soup = BeautifulSoup(responseText,"lxml")
    targetList = soup.select('#_cs_music_track > div.group_music._tab_panel > div.lyrics_area._panel._hp_style._hp_class > div.lyrics_txt')

    song_name = song_name.split('(')[0].strip()
    #print(song_name)
    if song_name in resolved_songs:
        resolved[song_name] = 1
    else:
        unresolved[song_name] = 1


    if targetList == []:
        return
    for i,elem in enumerate(targetList):
        fname.write(elem.text)
        fname.write('\n')

fill_resolved_songs()
print(resolved_songs)
for i in range(Num):
    str2 = 'noraebang_data/noraebang' + str(i) + '_songs.txt'
    fr = open(str2,'r',encoding='UTF8')
    strw = 'noraebang_data/nrb_lyrics' + str(i) + '.txt'
    fw = open(strw,'w',encoding='UTF8')
    line = fr.read().split('\n')
    fee = open('noraebang_data/Error_Song'+str(i)+'.txt','w',encoding='UTF8')
    
    

#     for lst in line:
#         NRBcrwal(lst.split(':')[0],lst+'+가사', fw)
#     print('res:', len(resolved), "unres", len(unresolved))
#
# with open("nb_UNresolved_songs.txt", 'w', encoding='utf-8') as file:
#     for key in unresolved:
#         print(key)
#         file.write(key + "\n")
#
# with open("nb_resolved_songs.txt", 'w', encoding='utf-8') as file:
#     for key in resolved:
#         print(key)
#         file.write(key + "\n")

    for j in range(len(line)):
        NRBcrwal(line[j], fw, j, fee)


                #NRBcrwal('윤종신+좋니')