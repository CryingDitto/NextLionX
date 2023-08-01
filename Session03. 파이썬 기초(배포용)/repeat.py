#1. for문을 활용해서 1부터 10까지의 숫자 중 3의 배수는 제외하고 출력해주세요(힌트:continue)

for i in range (1,11):
    if i%3==0:
        continue
    
    print(i)



#2. while 문을 사용하여 아래와 같이 별을 표시하는 프로그램을 작성해주세요
# *
# **
# ***
# ****
# *****
line=1
while line <6:
    print(line*"*")
    line+=1




#3. 입력받은 줄 수 만큼 별을 오른쪽 정렬로 표시하는 프로그램을 작성해주세요
# 예:
#     *
#    **
#   ***
#  ****

line = int(input("몇 줄?: "))
i=1
while i < line+1:
    print(" "*(line-i)+"*"*i)
    i+=1
    
for i in range(1,line+1):
    print(" "*(line-i) + '*'* i)

for i in range(1,line+1):
    star='*' * i
    print(star.rjust(line))
    


import sys
n=int(sys.stdin.readline()) # 훨씬 연산 속도가 빠르다고 함

for i in range(1,n+1):
    print(' '*(n-i) + '*' * i)