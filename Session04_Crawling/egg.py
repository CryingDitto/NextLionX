# type codes below in the terminal
# pipenv shell
# pipenv install requests
# pipenv install bs4


# simple example 상품 하나 정보 불러오기
# title = egg_list[0].find("div",{"class":"basicList_title__3P9Q7"}).find("a").string
# price = egg_list[0].find("div",{"class":"basicList_price_area__1UXXR"}).find("span").text

# details=[]
# detail_lists = egg_list[0].find("div", {"class": "basicList_detail_box__3ta3h"}).find("a")
# for detail in detail_lists:
#     details.append(detail.text)
# result = {
#     'title': title,
#     'price': price,
#     'details': details
# }
def extract_info(egg_list):
    result = []
    
    # 페이지의 여러 상품 정보 불러오기
    for egg in egg_list:
        title = egg.find("div", {"class": "basicList_title__3P9Q7"}).find("a").string
        price = egg.find("div", {"class": "basicList_price_area__1UXXR"}).find("span", {"class": "price_num__2WUXn"}).text

        detail_lists = egg.find("div", {"class": "basicList_detail_box__3ta3h"}).find_all("a")

        details = []
        for detail in detail_lists:
            details.append(detail.text)
            
        egg_info={
            'title':title,
            'price':price,
            'details':details
        }
        
        result.append(egg_info)
        
        # print(result)
    return result

