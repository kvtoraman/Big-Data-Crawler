

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

SONG_PER_MONTH = 40
START_YEAR = 2015
START_MONTH = 12
END_YEAR = 2017
END_MONTH = 11
COUNT = 0
def update_month(year,month):
    if month<12:
        return [year,month+1]
    return [year+1,1]

def get_song_info(id):
    song_info_url = "http://www.genie.co.kr/detail/songInfo?xgnm=" + str(id)
    targetRequest = Request(song_info_url)
    response = urlopen(targetRequest)
    responseText = response.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(responseText, 'html.parser')

    song_elems = soup.select('#body-content > div.song-main-infos > div.info-zone > h2')
    lyrics_elems = soup.select('#pLyrics')
    artist_elems = soup.select('#body-content > div.song-main-infos > div.info-zone > ul > li:nth-of-type(1) > span.value > a')
    #:nth-of-type(4)
    song_name = song_elems[0].text.strip()
    lyrics = lyrics_elems[0].text.strip()
    artist = artist_elems[0].text.strip()

    #print(song_name,artist,lyrics)
    return [song_name,artist,lyrics]
def get_fname(year,month):
    year = int(year)
    month = int(month)
    return str((year - 2015)*12 + month - 10)

def parse_month(year,month):
    global COUNT
    year = str(year)
    month = str(month)
    song_info_url = "http://www.genie.co.kr/detail/songInfo?xgnm=87463708"
    targetUrl = "http://www.genie.co.kr/chart/top100?ditc=M&ymd=20171001&hh=13&rtm=N&pg=1"
    targetRequest = Request(targetUrl)
    response = urlopen(targetRequest)
    responseText = response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(responseText,'html.parser')
    #:nth-of-type(2)
    song_names = [""]*SONG_PER_MONTH
    artists = [""]*SONG_PER_MONTH
    lyrics = [""]*SONG_PER_MONTH
    all_songs = soup.select("#sAllSongID")
    song_ids = all_songs[0]['value'].strip().split(';')

    for i in range(SONG_PER_MONTH):
        #print(song_ids[i])
        song_names[i],artists[i],lyrics[i] = get_song_info(song_ids[i])
        #(song_names[i])

    with open("billboard_data/bb" + str(COUNT) + "_lyrics.txt", 'w',encoding = 'utf-8') as file:
        for i in range(SONG_PER_MONTH):
            #print(song_names[i])
            lyrics[i] = lyrics[i].replace('\r\n', '\n')
            file.write(lyrics[i].replace('\n',' ') + "\n")

    with open("billboard_data/bb" + str(COUNT) + "_songs.txt", 'w',encoding = 'utf-8') as file:
        for i in range(SONG_PER_MONTH):
            file.write(song_names[i]+ ":" + artists[i] + "\n")

    COUNT += 1
    return [song_names,artists,lyrics]

cur_year = START_YEAR
cur_month = START_MONTH

while(cur_year != END_YEAR or cur_month != END_MONTH):
    print(cur_year,cur_month)
    parse_month(cur_year, cur_month)
    cur_year,cur_month = update_month(cur_year,cur_month)

