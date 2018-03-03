#!__*__coding:utf-8__*__
import collections
import pytagcloud

# 인코딩 ANSI로 바꿔서 저장해야 돌아감.

# 한글로 하려면 Noto Sans CJK 글꼴 설치
#install pytagcloud, pygame, simplejson

# 텍스트파일 내용
# 2018년 1월 29일 오후 4:12, 회원님 : ㅇㅇㅇ
#   년도  월  일  오전/후 시간 말한사람: 말한내용
# 이부분은 제외하자. -> remove_list

# 띄어쓰기로 구분
x=[]
f = open("파일위치\\파일명.txt", "r") #파일위치 파일명 입력
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
user=["회원님", "사용자1", "사용자2"] #카카오톡 대화명

remove_list= day+month+year+time+etc+user # (user를 추가하지 않으면 말한 횟수를 볼 수 있음)

new=[] #remove를 하고 남은 것을 받을 list

for word in x:
    if word not in remove_list:
        new.append(word)


b = collections.Counter(new)
top_100 = b.most_common(50)
print(top_100)



d=top_100
tags = pytagcloud.make_tags(d)
pytagcloud.create_tag_image(tags, '저장할파일이름명.png',  fontname='Noto Sans CJK')
#저장할 파일 이름명에 입력


# "ㅋㅋㅋㅋㅋㅋㅋㅋ" 등을 처리해야할지..