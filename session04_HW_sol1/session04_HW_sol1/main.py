import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoon.csv',mode='w',newline='')
writer = csv.writer(file)
writer.writerow(["title","writer","ratings"])

webtoon_url = f"https://comic.naver.com/webtoon/weekdayList?week=sun"
webtoon_html = requests.get(webtoon_url)
webtoon_soup = BeautifulSoup(webtoon_html.text,"html.parser")

webtoon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")

print(extract_info(webtoon_list))

final_result = []
final_result += extract_info(webtoon_list)

for result in final_result:
    row=[]
    row.append(result["title"])
    row.append(result["author"])
    row.append(result["rating"])
    writer.writerow(row)

print(final_result)



