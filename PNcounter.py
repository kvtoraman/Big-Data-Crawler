from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib import parse
import csv


TOTAL = 23
Neg = {'못', '말지', '안돼', '아닌', '아니', '비겁', '없', '에러', '괴로', '괴롭', '쓴', '헤어', '싫','아픈', '아프', '아퍼', '아닌', '슬프', '슬퍼', '슬픈', '안돼', '마지막'}
Pos = {'love', 'good', '사랑', '좋','행복','기뻐', '아름', 'good', '예쁘','예쁜', '예뻐', '반하' , '사랑', '고마', '좋', '잘', 'love', '설레', '설렘', '기쁨', 'beautiful', '두근','기쁜','기쁠'}

num_month = dict()

def count_neg(num, mode):

	str1 = str(num)
	if mode == 'bb':
		f = open('billboard_data/bb'+str1+'_lyrics.txt','r',encoding='UTF8')
	else:
		f = open('noraebang_data/nrb_lyrics'+str1+'.txt','r',encoding='UTF8')
	words = f.read().split()

	neg, pos = 0, 0
	
	for word in words:
		for neg_word in Neg:
			if neg_word in word:
				neg += 1
		for pos_word in Pos:
			if pos_word in word:
				pos += 1
	if mode == 'nrb':
		return pos, neg, len(words)
	return pos, neg

f = open('PNdata.csv' ,'w' , encoding = 'utf-8', newline='')
wr = csv.writer(f)

for i in range(TOTAL):
	bb_pos, bb_neg = count_neg(i,'bb')
	nrb_pos, nrb_neg, song_num = count_neg(i,'nrb')
	print(i, bb_pos, bb_neg, nrb_pos, nrb_neg)
	wr.writerow([i, bb_pos, bb_neg, nrb_pos, nrb_neg, song_num])

f.close()
