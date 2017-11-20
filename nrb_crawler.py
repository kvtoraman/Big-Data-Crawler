from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib import parse

Num = 23


def NRBcrwal(name,fname):
    targetUrl = "https://m.search.naver.com/search.naver?where=m&query="+parse.quote(name)
    targetRequest = Request(targetUrl)
    response = urlopen(targetRequest)
    responseText = response.read()

    soup = BeautifulSoup(responseText,"lxml")
    targetList = soup.select('#_cs_music_track > div.group_music._tab_panel > div.lyrics_area._panel._hp_style._hp_class > div.lyrics_txt')
    #print(targetList)
    if targetList == []:
        print('Error line: ' + name)
    for i,elem in enumerate(targetList):
        fname.write(elem.text)
        fname.write('\n')


for i in range(Num):
    str2 = 'noraebang_data/noraebang' + str(i) + '_songs.txt'
    fr = open(str2,'r',encoding='UTF8')
    strw = 'noraebang_data/nrb_lyrics' + str(i) + '.txt'
    fw = open(strw,'w',encoding='UTF8')
    line = fr.read().split('\n')
    
    
    for lst in line:
        NRBcrwal(lst+'+가사', fw)

#NRBcrwal('윤종신+좋니')