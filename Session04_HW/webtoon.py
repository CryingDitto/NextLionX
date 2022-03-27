
def extract_webtoon(toon_list, day):

    # title_list = []
    # artist_list = []
    # rating_list = []

    # Replace an abbreivation to a full name
    if day=='mon':
        weekday = 'Monday'
    elif day =='tue':
        weekday = 'Tuesday'
    elif day == 'wed':
        weekday = 'Wednesday'
    elif day =='thu':
        weekday = 'Thursday'
    elif day == 'fri':
        weekday = 'Friday'
    elif day == 'sat':
        weekday = 'Saturday'
    elif day == 'sun':
        weekday = 'Sunday'
    else:
        weekday = 'Wrong'

    webtoons = []
    for cartoon in toon_list:
        title = cartoon.find("dt").find("a").text
        artists = cartoon.find("dd", {"class": "desc"}).find("a").string.split("/")
        ratings = cartoon.find("div", {"class": "rating_type"}).find("strong").text
        # title_list.append(title)
        # artist_list.append(artists)
        # rating_list.append(rating)

        toon_info = {
            'weekday': weekday,
            'title': title,
            'artists': artists,
            'ratings': ratings
        }
        webtoons.append(toon_info)
    return webtoons
