from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

SONG_PER_MONTH = 20
START_YEAR = 2017
START_MONTH = 5
END_YEAR = 2017
END_MONTH = 10

def update_month(year,month):
    if month<12:
        return [year,month+1]
    return [year+1,1]

def parse_month(year,month):
    year = str(year)
    month = str(month)
    targetUrl = "https://www.tjmedia.co.kr/tjsong/song_monthPopular.asp?strType=1&SYY="+year+"&SMM="+month+"&SDD=01&EYY="+year+"&EMM="+month+"&EDD=28"
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
        songs.append(x.text)
    #print(songs)

    for x in artist_elems[:SONG_PER_MONTH]:
        artists.append(x.text)
    #print(artists)
    return [songs,artists]

cur_year = START_YEAR
cur_month = START_MONTH

while(cur_year != END_YEAR or cur_month != END_MONTH):
    print(parse_month(cur_year, cur_month))
    cur_year,cur_month = update_month(cur_year,cur_month)

#code for melon
#with open("MelonTop50.txt", 'w',encoding = 'utf-8') as file:
 #   for i in range(len(titles)):
  #      print("%2d %s - %s\n" % (i + 1, titles[i].text.strip(), artists[i].text.strip()))
   #     file.write("%2d %s - %s\n" %( i+1, titles[i].text.strip(), artists[i].text.strip()))
