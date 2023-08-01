import time
from unittest import case
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup
import re
import json

# --크롬창을 숨기고 실행-- driver에 options를 추가해주면된다
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# --원하는 크기의 창으로 열기
options.add_argument('window-size=1080,960')

url = 'https://map.naver.com/v5/search'
# driver = webdriver.Chrome('./chromedriver')  # 드라이버 경로  
driver = webdriver.Chrome('./chromedriver', options=options)

# css 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait

# frame 변경 메소드
def switch_frame(frame):
    driver.switch_to.default_content()  # frame 초기화
    driver.switch_to.frame(frame)  # frame 변경
    res
    soup


# 페이지 다운
def page_down(num):
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)


# key_word = '안암 한식'
# done "안암 한식", "안암 중식", "안암 양식", "안암 일식", "안암 인도", "안암 베트남", 
# "서울대입구 한식", "서울대입구 중식", "서울대입구 양식", "서울대입구 일식", "서울대입구 인도", "서울대입구 베트남",
#'안암 맥주', '안암 와인', '안암 막걸리', '안암 칵테일', '안암 술집',
# '서울대입구 맥주', '서울대입구 와인', '서울대입구 막걸리', '서울대입구 칵테일', '서울대입구 술집'

# "AnamKor", "AnamChi", "AnamWest", "AnamJap", "AnamInd", "AnamViet",
# "SeolipKor", "SeoliplChi", "SeolipWest", "SeolipJap", "SeolipInd", "SeolipViet",
# "AnamBeer", "AnamWine", "AnamMak", "AnamCocktail", "AnamDrink",
# "SeolipBeer", "SeolipWine", "SeolipMak", "SeolipCocktail", "SeolipDrink"
areaNames = ["서울대입구"]  # "안암", "서울대입구"
saveAreaNames = ["Seolip"]  # "Anam", "Seolip"
# "영화", "보드게임","노래방","당구","방탈출","네컷사진"
playCategory = ["방탈출"]
keywords = []# keywords = ["안암 ", "서울대입구 카페"]
savenames = []#["AnamCafe", "SeolipCafe"]
for area in areaNames:
    for play in playCategory:
        keyword = area+' '+play
        keywords.append(keyword)

for saveArea in saveAreaNames:
    for play in playCategory:
        savename = saveArea+play
        savenames.append(savename)

print(keyword in keywords)
print(saveArea in savenames)

savecount = 31
savecountOrigin = savecount
for keyword in keywords:

    driver.get(url)
    # css를 찾을때 까지 10초 대기
    time_wait(10, 'div.input_box > input.input_search')

    # 검색창 찾기
    search = driver.find_element(
        By.CSS_SELECTOR, 'div.input_box > input.input_search')

    # search.send_keys(key_word)  # 검색어 입력
    search.send_keys(keyword)
    search.send_keys(Keys.ENTER)  # 엔터버튼 누르기


    res = driver.page_source  # 페이지 소스 가져오기
    soup = BeautifulSoup(res, 'html.parser')  # html 파싱하여  가져온다

    sleep(1)


    # frame 변경
    switch_frame('searchIframe')
    page_down(40)
    sleep(5)

    # 매장 리스트
    store_list = driver.find_elements(By.CSS_SELECTOR, '._1EKsQ')
    # 페이지 리스트
    next_btn = driver.find_elements(By.CSS_SELECTOR, '._2ky45 > a') 

    # dictionary 생성
    # store_dict = { keyword+' 매장정보': []}
    store_dict = {keyword: {}}
    # 각 가게 하나의 dictionary
    store_detail_dict = {}
    
    # 시작시간
    start = time.time()
    print(f'[{keyword} 크롤링 시작]')

    # page selector 키워드에 따라 달라지므로 구분해줌
    pageSelector = '.OXiLu'
    if ("한식" not in keyword) and ("일식" not in keyword) and ("서울대입구 중식" not in keyword
    ) and ("막걸리" not in keyword) and ("칵테일" not in keyword) and ("서울대입구 와인" not in keyword
    ) and ("술집" not in keyword) and ("카페" not in keyword):
        pageSelector ='._3Apve' #음식점 개수가 많지 않으면 이렇게 처리되는 듯함..
        store_list = driver.find_elements(By.CSS_SELECTOR, '._22p-O')  # 매장 리스트 selector도 달라짐
    if ("서울대입구 보드게임" in keyword) or ("서울대입구 방탈출" in keyword):
        pageSelector = '._1AjbI'
        store_list = driver.find_elements(By.CSS_SELECTOR, '._3KSjd')  # 매장 리스트 selector도 달라짐

    count = 0
    countEnd = len(next_btn)-2 # 검색하고 싶은 페이지 개수 #페이지 개수 전체 하고 싶으면 버튼 개수 -2 (이전, 다음 버튼 뺀 것)
    
    # 크롤링 (페이지 리스트 만큼)
    for btn in range(len(next_btn))[1:]:  # next_btn[0] = 이전 페이지 버튼 무시 -> [1]부터 시작
        print(f'현재 페이지 {btn}')

        
        if count==countEnd:
            # 3페이지 정도만 검색...
            break;
        count += 1
        # '.OXiLu' # '._3Apve' # 페이지에는 현재 페이지의 가게 전체가 들어감  
        
        store_list
        for data in range(len(store_list)):  # 매장 리스트 만큼
            page = driver.find_elements(By.CSS_SELECTOR, pageSelector)
            # print(f'page 개수: {len(page)}')
            print(f'{data+1}번 가게')
            if data >= len(page):  # wrong index
                print('Reset data index')
                data = 0
                break

            curBox = store_list[data] #._1EKsQ 가진 리스트에서 하나 뽑아옴
            try:
                isAd = len(curBox.find_elements(By.CSS_SELECTOR, '._1x55T > span'))  # 광고 표시 있으면 1, 없으면 0
            except: 
                # 광고 아예 없을 경우 에러나므로 예외 처리
                isAd = 0
            
            if isAd:
                print(f'skip ad: {isAd}')
                continue
            
            
            page[data].click()  # 가게 리스트에서 가게 이름을 눌러서 팝업창 띄움
            sleep(2)
            try:
                # 상세 페이지로 이동
                switch_frame('entryIframe')
                time_wait(5, '._3XamX')
                # 스크롤을 맨밑으로 1초간격으로 내린다.
                for down in range(3):
                    sleep(1)
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")

                
                # -----주소(위치)-----
                try:
                    store_addr_list = driver.find_elements(By.CSS_SELECTOR, '._1aj6-')
                    for i in store_addr_list:
                        store_addr = i.find_element(
                            By.CSS_SELECTOR, '._1h3B_').text
                    if "안암역" in store_addr:
                        pass
                    elif "고려대역" in store_addr:
                        pass
                    elif "서울대입구역" in store_addr:
                        pass
                    # elif "개운사" in store_addr:
                    #     pass
                    # elif "인촌" in store_addr:
                    #     pass
                    # elif "관악로" in store_addr:
                    #     pass
                    # elif "남부순환로" in store_addr:
                    #     pass
                    else:
                        # 위의 주소에 해당되지 않는 경우
                        switch_frame('searchIframe')  # search frame으로 돌아감
                        print('switch_frame')
                        continue                        
                except:
                    pass
                

                # -----매장명 가져오기-----
                store_name = driver.find_element(By.CSS_SELECTOR, '._3XamX').text

                # -----카페 프랜차이즈 여부-----
                store_franchise = 0
                if '카페' in keyword:
                    try:
                        
                        if ('스타벅스' in store_name) or ('투썸' in store_name) or ('할리스' in store_name) or ('이디야' in store_name
                        ) or ('공차' in store_name) or ('탐앤탐' in store_name) or ('커피빈' in store_name) or ('매머드' in store_name
                        ) or ('아마스빈' in store_name) or ('빽다방' in store_name) or ('팔공' in store_name) or ('쥬씨' in store_name
                        ) or ('컴포즈' in store_name) or ('와플앨리' in store_name) or ('와플대학' in store_name) or ('메가' in store_name
                        ) or ('파리바게뜨' in store_name) or ('배스킨' in store_name) or ('뚜레쥬르' in store_name):
                            print('프랜차이즈 카페')
                            store_franchise = 1
                    except:
                        pass
                
                print(store_name)
                print(store_addr)

                # 현재 매장 페이지 url 가져오기
                store_url = driver.current_url
                print(store_url)

                # -----전화번호 가져오기-----
                try:
                    store_tel = driver.find_element(By.CSS_SELECTOR, '._3ZA0S').text
                except:
                    pass

                print(store_tel)

                # -----음식 종류-----
                try:
                    food_type = driver.find_element(
                        By.CSS_SELECTOR, '._3ocDE').text
                except:
                    pass
                if keyword == '영화':
                    if ("영화제작" in food_type):
                        print(f'{store_name} ...영화관 아님. switch_frame')
                        switch_frame('searchIframe')
                        continue
                    elif ("영화" not in food_type) or ("DVD" not in food_type):
                        print(f'{store_name} ...영화관 아님. switch_frame')
                        switch_frame('searchIframe')
                        continue
                print(food_type)

                # if '카페' in keyword:
                #     if '스터디' in food_type:
                #         switch_frame('searchIframe') # 스터디카페 제외
                #         continue

                # # -----영업시간-----
                # try:
                #     store_time_list = driver.find_elements(By.CSS_SELECTOR, 
                #         '._2vK84')  # 아니 태그가 그세 바뀌네ㅡ,.ㅡ
                #     for i in store_time_list:
                #         store_time = i.find_element(By.CSS_SELECTOR,
                #                                     '._3uEtO > time').text
                # except:
                #     pass
                # print(store_time)

                # -----메뉴-----
                try:
                    menu_list = driver.find_elements(By.CSS_SELECTOR, '._1XxR5')
                    menu_name = []  # 메뉴이름
                    menu_price = []  # 메뉴가격

                    for i in menu_list:
                        name = i.find_element(By.CSS_SELECTOR, '._1q3GD').text
                        menu_name.append(name)

                        price = i.find_element(By.CSS_SELECTOR,
                                            '._3IAAc').text  # 텍스트를 넣을 변수 생성
                        # 할인 전 가격 제거  # 재정의
                        price = re.sub('원\d{2},\d{3}', '', price)
                        menu_price.append(price)  # 추가

                except:
                    pass

                # -----메뉴2 (다른 태그의 메뉴)-----
                try:
                    menu_list_two = driver.find_elements(By.CSS_SELECTOR, '._20R25')
                    menu_name_two = []
                    menu_price_two = []

                    for i in menu_list_two:
                        name_two = i.find_element(By.CSS_SELECTOR, '._2E0Gk').text
                        name_two = re.sub('\n사진|\n대표', '', name_two)

                        price_two = i.find_element(By.CSS_SELECTOR, '._3GJcI').text

                        menu_name_two.append(name_two)
                        menu_price_two.append(price_two)

                except:
                    print('menu 문제 있음')
                    menus = []
                    prices = []

                    # -----평점-----
                    try:
                        store_rating_list = driver.find_element(By.CSS_SELECTOR,
                                                                '._1A8_M').text
                        store_rating = re.sub('별점', '', store_rating_list).replace(
                            '\n', '')  # 별점이라는 단어 제거
                    except:
                        store_rating = []
                        # 키워드리뷰 없으면 다음 음식점으로
                        print('별점 없음')

                        # ---- dict에 데이터 집어넣기----
                        dict_temp = {
                            'name': store_name,
                            'tel': store_tel,
                            'star': store_rating,
                            'addr': store_addr,
                            'foodtype': food_type,
                            # 'time': store_time,
                            'menu': menus,
                            'price': prices,
                            # 'kwd': kwd_title,
                            # 'kwd_count': kwd_count,
                            'thumb': store_thumb,
                            'url': store_url,
                            'franchise': store_franchise
                        }

                        store_dict[keyword+' 매장정보'].append(dict_temp)

                        print(f'{store_name} ...완료')
                        switch_frame('searchIframe')
                        continue
                    # 메뉴는 없지만 별점은 있을 때
                    # ---- dict에 데이터 집어넣기----
                    dict_temp = {
                        'name': store_name,
                        'tel': store_tel,
                        'star': store_rating,
                        'addr': store_addr,
                        'foodtype': food_type,
                        # 'time': store_time,
                        'menu': menus,
                        'price': prices,
                        # 'kwd': kwd_title,
                        # 'kwd_count': kwd_count,
                        'thumb': store_thumb,
                        'url': store_url,
                        'franchise': store_franchise
                    }

                    # store_dict[keyword+' 매장정보'].append(dict_temp)
                    # dictionary일 때
                    store_detail_dict[store_name] = dict_temp

                    print(f'{store_name} ...완료')
                    switch_frame('searchIframe')
                    continue

                # 메뉴 리스트 합체
                menus = menu_name + menu_name_two
                prices = menu_price + menu_price_two

                print(menus)
                print(prices)
                # # -----키워드 리뷰 가져오기-----
                # try:
                #     keyword_list = driver.find_element(By.CSS_SELECTOR,
                #                                        '._28hFN')  # 키워드가 담긴 리스트 클릭
                #     keyword_list.click()

                # except:  # 키워드리뷰 없으면 다음 음식점으로
                #     print('키워드리뷰 없음 >>> 다음으로',)
                #     switch_frame('searchIframe')
                #     continue

                # try:
                #     keyword_review_list = driver.find_elements(By.CSS_SELECTOR, 
                #         '._3FaRE')  # 리뷰 리스트
                #     kwd_title = []
                #     kwd_count = []
                #     sleep(2)

                #     for i in keyword_review_list:
                #         keyword_title = i.find_element(By.CSS_SELECTOR,
                #                                        '._1lntw').text  # 키워드리뷰
                #         keyword_count = i.find_element(By.CSS_SELECTOR,
                #                                        '.Nqp-s').text   # 리뷰를 선택한 수

                #         # db에 넣을 때 편의를 위해 요청하였음
                #         title_re = re.sub('"', '', keyword_title) \
                #             .replace('양이 많아요', '1').replace('음식이 맛있어요', '2').replace('재료가 신선해요', '3') \
                #             .replace('가성비가 좋아요', '4').replace('특별한 메뉴가 있어요', '5').replace('화장실이 깨끗해요', '6') \
                #             .replace('주차하기 편해요', '7').replace('친절해요', '8').replace('특별한 날 가기 좋아요', '9').replace(
                #             '매장이 청결해요',
                #             '10') \
                #             .replace('인테리어가 멋져요', '11').replace('단체모임 하기 좋아요', '12').replace('뷰가 좋아요', '13').replace(
                #             '매장이 넓어요',
                #             '14') \
                #             .replace('혼밥하기 좋아요', '15')

                #         # 1~15만 리스트에추가 (이외에 다른 키워드들은 추가하지않음)
                #         title_num = list(map(str, range(1, 16)))
                #         count_keyword = re.sub(
                #             '이 키워드를 선택한 인원\n', '', keyword_count)
                #         if title_re in title_num:
                #             kwd_title.append(title_re)
                #             kwd_count.append(count_keyword)
                #         else:
                #             pass
                # except:
                #     pass
                # kwd_count = list(map(int, kwd_count))  # int 형변환

                # print(kwd_title)
                # print(kwd_count)

                # -----썸네일 사진 주소-----
                try:
                    thumb_list = driver.find_element(By.CSS_SELECTOR, '.cb7hz') \
                        .value_of_css_property('background-image')  # css 속성명을 찾는다
                    store_thumb = re.sub(
                        'url|"|\)|\(', '', thumb_list)  # url , (" ") 제거
                except:
                    pass
                print(store_thumb)

                # -----평점-----
                try:
                    store_rating_list = driver.find_element(By.CSS_SELECTOR,
                                                            '._1A8_M').text
                    store_rating = re.sub('별점', '', store_rating_list).replace(
                        '\n', '')  # 별점이라는 단어 제거
                except:
                    store_rating = []
                    # 키워드리뷰 없으면 다음 음식점으로
                    print('별점 없음')

                    # ---- dict에 데이터 집어넣기----
                    dict_temp = {
                        'name': store_name,
                        'tel': store_tel,
                        'star': store_rating,
                        'addr': store_addr,
                        'foodtype': food_type,
                        # 'time': store_time,
                        'menu': menus,
                        'price': prices,
                        # 'kwd': kwd_title,
                        # 'kwd_count': kwd_count,
                        'thumb': store_thumb,
                        'url': store_url,
                        'franchise': store_franchise
                    }

                    # store_dict[keyword+' 매장정보'].append(dict_temp)
                    # dictionary일 때
                    store_detail_dict[store_name] = dict_temp

                    print(f'{store_name} ...완료')
                    switch_frame('searchIframe')
                    continue
                print(store_rating)

                # ---- dict에 데이터 집어넣기----
                dict_temp = {
                    'name': store_name,
                    'tel': store_tel,
                    'star': store_rating,
                    'addr': store_addr,
                    'foodtype': food_type,
                    # 'time': store_time,
                    'menu': menus,
                    'price': prices,
                    # 'kwd': kwd_title,
                    # 'kwd_count': kwd_count,
                    'thumb': store_thumb,
                    'url': store_url,
                    'franchise': store_franchise
                }

                # store_dict[keyword].append(store_detail_temp)

                # dictionary일 때 
                store_detail_dict[store_name] = dict_temp
                

                print(f'{store_name} ...완료')
                switch_frame('searchIframe')
                sleep(1)

            except:
                print('ERROR!' * 3)
                # 지금까지 한 내용이라도 저장
                with open('./data/store_data_'+keyword+'_errorOccured.json', 'w', encoding='utf-8') as f:
                    json.dump(store_dict, f, indent=4, ensure_ascii=False)

        # 다음 페이지 버튼
        # if data==len(page)-1:
        if page[-1]:  # 마지막 매장일 경우 다음버튼 클릭
            
            next_btn[-1].click()
            sleep(2)
        else:
            print('페이지 인식 못함')
            break

    print('['+ keyword + ' 데이터 수집 완료]\n소요 시간 :', time.time() - start)
    store_dict[keyword] = store_detail_dict
    
    # json 파일로 저장
    with open('./data/store_dict_'+str(savecount)+savenames[savecount-savecountOrigin]+'.json', 'w', encoding = 'utf-8') as f:
        json.dump(store_dict, f, indent=4, ensure_ascii=False)
    savecount += 1

    # 검색창 건드리기 위해
    driver.get(url)
    # switch_frame('searchIframe')

driver.quit()  # 작업이 끝나면 창을닫는다.
