#!__*__coding:utf-8__*__
import collections
import pytagcloud
import os

# 인코딩 ANSI로 바꿔서 저장해야 돌아갔으나 밑에 (encoding="UTF-8")로 해결하였음

# 한글로 하려면 Noto Sans CJK 글꼴 설치
#install pytagcloud, pygame, simplejson

# 텍스트파일 내용
# 2018년 1월 29일 오후 4:12, 회원님 : ㅇㅇㅇ
#   년도  월  일  오전/후 시간 말한사람: 말한내용
# 이부분은 제외하자. -> remove_list

# 띄어쓰기로 구분


directory = input("카카오톡 대화 txt 파일이 있는 디렉토리를 입력하세요. 예) e:\pythondata")
filename = input("txt파일명을 입력하세요. 예) kakao.txt")
save_file_name = input("저장할 파일 이름명을 입력하세요. 예)kakao.png")
full_directory = os.path.join(directory, filename)
x=[]
f = open(full_directory, "r", encoding="UTF-8") #파일위치 파일명 입력
while True:
    a=f.readline()
    if a=="":
        break
    y=a.split(" ")
    x=x+y

# 일 제외 "d일"
d1 = range(32)
d2=list(d1)
day = [str(d3)+"일" for d3 in d2]

#월 제외 "M월"
m1=range(13)
m2=list(m1)
month=[str(m3) +"월" for m3 in m2]

# 시간 "h:mm," 형식
hour=range(13)
minute=range(60)
#time = [str(h)+":"+"%2s"+"," %min for h in hour for min in minute]
time=[]
for h in hour:
    for min in minute: # mm 형식으로 바꿈
        if min<=9:
            tt=str(h)+":"+"0"+str(min)+","
            time.append(tt)
        else:
            tt = str(h) + ":" + str(min) + ","
            time.append(tt)

y=range(2010, 2019) #카톡 출시일 2010년부터
y2=list(y)
year=[str(y3)+"년" for y3 in y2]
etc=["오전","오후",":","\n","<사진>\n"] #기타 제외할 것들
user=["회원님"]
while True:
    new_user = input("카카오톡 대화명를 입력하세요. 다 입력하셨으면 q를 입력하세요.")
    if new_user =="q":
    #    for i in user:
    #       print (i) #확인용 print
        break
    user.append(new_user)



#user=["회원님", "사용자1", "사용자2"] #카카오톡 대화명

remove_list= day+month+year+time+etc+user # (user를 추가하지 않으면 말한 횟수를 볼 수 있음)

new=[] #remove를 하고 남은 것을 받을 list

for word in x:
    if word not in remove_list:
        new.append(word)

#상위 50개만 합시다.
b = collections.Counter(new)
top_50 = b.most_common(50)
print(top_50)



d=top_50
tags = pytagcloud.make_tags(d)
pytagcloud.create_tag_image(tags, save_file_name,  fontname='Noto Sans CJK')
#저장할 파일 이름명에 입력


# "ㅋㅋㅋㅋㅋㅋㅋㅋ" 등을 처리해야할지..