

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

SONG_PER_MONTH = 20
START_YEAR = 2017
START_MONTH = 9
END_YEAR = 2017
END_MONTH = 10

def update_month(year,month):
    if month<12:
        return [year,month+1]
    return [year+1,1]
def get_song_info(id):
    return ["","",""]

def parse_month(year,month):
    year = str(year)
    month = str(month)
    song_info_url = "http://www.genie.co.kr/detail/songInfo?xgnm=87463708"
    targetUrl = "http://www.genie.co.kr/chart/top100?ditc=M&ymd=20171001&hh=13&rtm=N&pg=1"
    targetRequest = Request(targetUrl)
    response = urlopen(targetRequest)
    responseText = response.read().decode('utf-8','ignore')
    soup = BeautifulSoup(responseText,'html.parser')
    #:nth-of-type(2)
    songs = [0]*SONG_PER_MONTH
    artists = [0]*SONG_PER_MONTH
    lyrics = [0]*SONG_PER_MONTH
    all_songs = soup.select("#sAllSongID")
    song_ids = all_songs[0]['value'].strip(';')

    for i in range(SONG_PER_MONTH):
        songs[i],artists[i],lyrics[i] = get_song_info(song_ids[i])

    return [[],[]]

    song_elems = soup.select('#body-content > div.song-main-infos > div.info-zone > h2')
    lyrics_elems = soup.select('#pLyrics')
    artist_elems = soup.select('#body-content > div.song-main-infos > div.info-zone > ul > li:nth-of-type(1) > span.value > a')
    #:nth-of-type(4)
    #BoardType1 > table > tbody > tr:nth-child(2) > td:nth-child(4)
    print(song_elems[0].text.strip())
    print(lyrics_elems[0].text)
    print(artist_elems[0].text)
    #for x in song_elems[:SONG_PER_MONTH]:
    #    songs.append(x.text)
    #print(songs)

    #for x in artist_elems[:SONG_PER_MONTH]:
    #    artists.append(x.text)
    #print(artists)
    return [songs,artists]

cur_year = START_YEAR
cur_month = START_MONTH

while(cur_year != END_YEAR or cur_month != END_MONTH):
    print(parse_month(cur_year, cur_month))
    cur_year,cur_month = update_month(cur_year,cur_month)

