from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import string

SONG_PER_MONTH = 40
START_YEAR = 2015
START_MONTH = 12
END_YEAR = 2017
END_MONTH = 11


def update_month(year,month):
    if month<12:
        return [year,month+1]
    return [year+1,1]

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
problem_mp = {}
def find_song(name):
    lyrics = ""
    global valid_chars
    banned_chars = '<>:"/|?*\\'
    for c in banned_chars:
        name = name.replace(c,'')

    if name != "" and   name[0] == " ":
        name = name[1:]
    try:
        f = open("all_lyrics_noraebang/" + name + '.txt',"r",encoding='utf-8')
        lyrics = f.read()
        lyrics = lyrics.replace("\r\n", "\n")
        lyrics = lyrics.replace("\n", " ")
        #print(lyrics[:10])
    except:
        lyrics = ""
        print("PROBLEM " + name)
        problem_mp[name] = 1

    return lyrics

def parse_month(year,month):
    global COUNT
    year = str(year)
    month = str(month)
    targetUrl = "https://www.tjmedia.co.kr/tjsong/song_monthPopular.asp?strType=1&SYY="+year+"&SMM="+month+"&SDD=01&EYY="+year+"&EMM="+month+"&EDD=28"
    print(targetUrl)
    targetRequest = Request(targetUrl)
    response = urlopen(targetRequest)
    responseText = response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(responseText,'html.parser')
    #:nth-of-type(2)
    songs = []
    artists = []
    targetTable = soup.select('#BoardType1 > table > tbody > tr')
    song_elems = soup.select('#BoardType1 > table > tbody > tr > td.left')
    artist_elems = soup.select('#BoardType1 > table > tbody > tr > td:nth-of-type(4)')
    #BoardType1 > table > tbody > tr:nth-child(2) > td:nth-child(4)
    for x in song_elems[:SONG_PER_MONTH]:
        songs.append(x.text.split('(')[0].strip())
    #print(songs)

    for x in artist_elems[:SONG_PER_MONTH]:
        artists.append(x.text)
    #print(artists)
    # with open("noraebang_data/noraebang" + str(COUNT) + "_songs.txt", 'w',encoding = 'utf-8') as file:
    #      for i in range(SONG_PER_MONTH):
    #          file.write(songs[i]+ ":" + artists[i] + "\n")

    with open("noraebang_data/missing" + str(COUNT) + "_songs.txt", 'w', encoding='utf-8') as file:
        for i in range(SONG_PER_MONTH):
            lyrics = find_song(songs[i])
            if lyrics != "":
                file.write(find_song(songs[i]) + "\n")



    COUNT += 1
    return [songs,artists]

COUNT = 0
cur_year = START_YEAR
cur_month = START_MONTH

while(cur_year != END_YEAR or cur_month != END_MONTH):
    print(cur_year, cur_month)
    parse_month(cur_year, cur_month)
    cur_year,cur_month = update_month(cur_year,cur_month)


with open("problem_mp.txt", 'w', encoding='utf-8') as file:
    for p in problem_mp:
        file.write(p + "\n")
