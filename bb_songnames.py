

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

SONG_PER_MONTH = 40
START_YEAR = 2015
START_MONTH = 12
END_YEAR = 2017
END_MONTH = 11
COUNT = 0
banned_artist = ["Ed Sheeran","Maroon 5","Adele","Lasse Lindh","The Chainsmokers","The Chainsmokers & Coldplay"]

name_mp = {}

def update_month(year,month):
    if month<12:
        return [year,month+1]
    return [year+1,1]

def get_song_info(id):
    global name_mp
    song_info_url = "http://www.genie.co.kr/detail/songInfo?xgnm=" + str(id)
    #print(song_info_url)
    targetRequest = Request(song_info_url)
    response = urlopen(targetRequest)
    responseText = response.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(responseText, 'html.parser')

    song_elems = soup.select('#body-content > div.song-main-infos > div.info-zone > h2')

    #:nth-of-type(4)
    song_name = song_elems[0].text.strip()

    if "19금" in song_name:
        return
    name_mp[song_name] = 1
    #print(song_name,artist,lyrics)
    return
def get_fname(year,month):
    year = int(year)
    month = int(month)
    return str((year - 2015)*12 + month - 10)

def parse_month(year,month):
    global COUNT
    year = str(year)
    month = str(month).zfill(2)
    print(year,month)

    song_info_url = "http://www.genie.co.kr/detail/songInfo?xgnm=87463708"
    targetUrl = "http://www.genie.co.kr/chart/top100?ditc=M&ymd=" + year + month + "01&hh=13&rtm=N&pg=1"
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
        get_song_info(song_ids[i])
        #(song_names[i])
    COUNT += 1
    return

cur_year = START_YEAR
cur_month = START_MONTH

while(cur_year != END_YEAR or cur_month != END_MONTH):
    parse_month(cur_year, cur_month)
    cur_year,cur_month = update_month(cur_year,cur_month)

with open("billboard_song_names.txt", 'w',encoding = 'utf-8') as file:
    for key in name_mp:
        print(key)
        file.write(key + "\n")