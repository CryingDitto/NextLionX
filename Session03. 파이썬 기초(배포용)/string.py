answer = "3/21은 NEXT 세션하는 날!"

string1 = "2022-03-21은 "
string2 = "next"
string3 = "        세션하는 날!      "


string1split=string1.split("-")
string = string1split[1][1]+"/"+string1split[2]+string2.upper()+" "+string3.strip()
# Answer
string=string1.replace("2022-0","").replace("-","/")+ string2.upper()+" "+ string3.strip()

if answer == string:
    print("정답입니다!")
else:
    print("틀렸습니다.")
    print(f"정답 : {answer}")
    print(f"입력값 : {string}")