import requests
from bs4 import BeautifulSoup
from egg import extract_info
import csv

from webtoon import extract_webtoon

file = open('webtoon.csv', mode='w', newline='')
# 'w' 쓰기 모드, newline='' 띄어쓰기 없이 데이터 입력
writer = csv.writer(file)
writer.writerow(["weekday","title", "artists", "ratings"])  # 가장 상위 header 달아준 것

webtoon_summary = []
for day in ['mon','tue','wed','thu','fri','sat','sun']:
    toon_url = f"https://comic.naver.com/webtoon/weekdayList?week={day}"
    toon_html = requests.get(toon_url)
    toon_soup = BeautifulSoup(toon_html.text, "html.parser")

    # print(toon_soup)
    toon_list_box = toon_soup.find("ul",{"class":"img_list"})
    toon_list = toon_list_box.find_all("dl")


    webtoon_summary += extract_webtoon(toon_list, day)
    
print(webtoon_summary)

for info in webtoon_summary:
    row = []
    row.append(info['weekday'])
    row.append(info['title'])
    row.append(info['artists'])
    row.append(info['ratings'])
    writer.writerow(row)


# title = toon_list.find_all("dt").find("a").text

    
# print(toon_list[0].find("div",{"class":"rating_type"}).find("strong").text)
# print(title_list)
# print(artist_list)
# print(rating_list)
