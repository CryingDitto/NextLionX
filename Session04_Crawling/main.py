import requests
from bs4 import BeautifulSoup
from egg import extract_info
import csv

file=open('egg.csv', mode='w', newline='')
# 'w' 쓰기 모드, newline='' 띄어쓰기 없이 데이터 입력
writer=csv.writer(file)
writer.writerow(["title","price","detail"]) #가장 상위 header 달아준 것

final_result = []
for page in range(1,11):
    # 우리가 정보를 얻고 싶어하는 URL
    EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex={page}&pagingSize=80&query=반숙란"
    # get 요청을 통해 해당 페이지 정보를 저장
    egg_html = requests.get(EGG_URL)
    # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
    egg_soup = BeautifulSoup(egg_html.text, "html.parser")

    # print(egg_soup)
    egg_list_box = egg_soup.find("ul", {"class": "list_basis"})
    egg_list = egg_list_box.find_all("li", {"class": "basicList_item__2XT81"})

    final_result += extract_info(egg_list)

#여러 상품 정보를 돌면서
#상품 하나 result로 받아와서 그 상품의 title, price, detail을 추가
for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['details'])
    writer.writerow(row)

print(final_result)








# # 우리가 정보를 얻고 싶어하는 URL
# EGG_URL = f"https://search.shopping.naver.com/search/all?pagingIndex=2&pagingSize=80&query=반숙란"
# # get 요청을 통해 해당 페이지 정보를 저장
# egg_html = requests.get(EGG_URL)
# # bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
# egg_soup = BeautifulSoup(egg_html.text, "html.parser")

# # print(egg_soup)
# egg_list_box = egg_soup.find("ul", {"class": "list_basics"})
# egg_list = egg_list_box.find_all("li", {"class": "backList_item__2XT81"})
