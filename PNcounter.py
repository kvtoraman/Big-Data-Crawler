from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib import parse
import csv


TOTAL = 23


num_month = dict()

def count_neg(num):

	str1 = str(num)
	f = open('billboard_data/bb'+str1+'_lyrics.txt','r',encoding='UTF8')
	words = f.read().split()

	Neg = {'못', '말지', '안돼', '아닌', '아니', '비겁', '없', '에러', '괴로', '괴롭', '쓴', '헤어'}
	Pos = {'행복','기뻐', '아름', 'good', '예쁘', '예뻐', '반하' , '사랑', '고마', '좋', '잘', 'love', '설레', '기쁨'}
	neg, pos = 0, 0
	
	for word in words:
		for neg_word in Neg:
			if neg_word in word:
				neg += 1
		for pos_word in Pos:
			if pos_word in word:
				pos += 1

	return pos, neg

f = open('PNdata.csv' ,'w' , encoding = 'utf-8', newline='')
wr = csv.writer(f)

for i in range(TOTAL):
	pos, neg = count_neg(i)
	print(i, pos, neg)
	wr.writerow([i, pos, neg])

f.close()
