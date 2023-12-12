import streamlit as st
import os
os.system('cls')
'### :gray[하성철 포트폴리오]'
col1, col2 = st.columns([1, 2])
with col1:
    st.image('하성철.jpg')
with col2:
    '#### :blue[간단한 자기소개]'
    '저의 나이는 현재 27살(1997년생)이며,'
    '2023학년도에 3학년으로 편입한 하성철입니다.'
    '저는 학교에 오기 전인 2019년 5월부터 2022년 11월까지 직장 생활을 하다가 건양대학교에 편입학하게 되었습니다.'

''
'-----------------------'
col = st.sidebar.columns(2)
with col[0]:
    '### :blue[SNS Aaddress]'
    st.link_button("instagram(📷)", "https://www.instagram.com/0320_ha_s/")
with col[1]:
    '### :blue[SNS Aaddress]'
    st.link_button("Facebook(ⓕ)", "https://www.facebook.com/profile.php?id=100005327141659")

''
''
'##### :blue[하성철의 간략한 일대기]'
' 저의 간략한 일대기에 대해 이야기 해보겠습니다.'
' 저는 2016년도에 목원대학교 행정학과에 입학하여 2017년 9월 입대전인 2학년 1학기 까지 마치고 입대를 하였습니다.'
' 2학년때에는 학생회활동도 하여 학교 생활에 누구보다 더 적극적으로 임하였습니다.'
''
' 그리고 저는 군대부터 다른 사람들과는 조금 다르게 다녀왔습니다. 국방부 연합사의장대에서 군 복무를 하였으며, 의무복무 기간인 21개월을  마치고 1년 연장하여 하사로 전역하였습니다.'
' 그 전역 후 목원대학교에서 남은 한 한기를 마치고 공무원시험준비를 하고자 휴학을 결정하였고, 앞이 깜깜한 수험생활에 지쳐 잠시 쉬고자 천주교법인에서 사무장으로 1년 6개월 근무하고 학업에 대한 갈망때문에 퇴사 후 편입으로 2023년부터 재난안전소방학과에 재학하고 있습니다.'
''
'##### :orange[장점]'
' 저의 장점은 젊은 나이임에도 불구하고 다양한 사회생활을 했다는 경험이 있다는 점입니다'
' 조직의 구성원과의 의사소통하는 방법, 문제가 생겼을 때 해결할 수 있는 방법 등 일하면서 생길 수 있는 다양한 변수들에 대해 대처능력이 좋다고 저는 자신합니다.'
' 그리고 어린나이에 시작한 사회생활로 인하여 그 누구보다도 멘탈이 단단하여 사람들 혹은 일에 휘둘리는 일이 없다는 점입니다.'
''
'##### :orange[취미 및 특기]'
' 저의 취미와 특기는 운동입니다. 싫어하는 운동없이 모든 운동을 좋아하고 다양한 운동을 즐겨하고 있습니다.'
' 또한 자기 관리가 철저한 편이라 운동을 매일 하고 있습니다.'
' 아래는 저의 신상정보들입니다. 항상 관심가져주시고 지켜봐주시고, 언제든 연락주세요. '
' 이상으로 저의 소개를 마치겠습니다. 감사합니다.'

''
'##### :orange[신상정보]'
'직업(💼) :건양대학교 재난안전소방학과 3학년에 재학중인 대학생입니다.'
'전화번호(📞) : 010-9241-6375'
'이메일(📧) : gktjdcjf97@naver.com'
'주소(🏠) : 대전광역시 서구 관저동로 90번길 47 느리울 1101동 901호'
'경력(🛠️) : 국방부 근무지원단 연합사의장대 하사 전역, 천주교법인 사무장(행정직) 1년 6개월 근무'
'자격증(📝) : 1종운전면허, MOS 엑셀, MOS 파워포인트, ITQ 한글, 파워포인트, 인터넷, 엑셀'


# import numpy as np
# # import pandas as pd

# os.system('cls')

# p = pd.Series
# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li, index=['a', 'b', 'c', 'd'])
# li
# n
# p

# import streamlit as st
# st.write('Hello, **World!** :sunglasses:🤩🤑')
# 'Hello, World! :sunglasses:🤩🤑'
# '# Hello, World! color :blue :sunglasses:🤩🤑'

# import streamlit as st

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()

# x = []
# y = []
# for i in range(-10, 11, 2):
#     x.append(i)
#     y.append(3*i*3 - 5*i**2 + 3*i - 7)

# col1, col2, col3 = st.columns(3)
# with col1 : 
#     cc = st.radio('선의 색을 선택하시오.', ['red', 'green', 'blue', 'orange'])
# with col2:
#     ma = st.radio('마커의 형태를 선택하시오.', ['o', '^', 's', 'p', 'h'])
# with col3:
#     ls = st.radio('선의 형태를 선택하시오.', ['-', '-.', ':', '--'])
# # plt.plot(x, y, '-go')
# plt.plot(x, y, color = cc, linestyle = ls, marker = ma)
# st.pyplot(fig)


# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(2*i**3 + 5*i**2 + 3*i + -7)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오.', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커의 스타일을 선택하시오.', ('s', '^', 'o'))
# plt.plot(x,y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)

# x = []
# for i in range(-100, 100):
#     x. append(i/10.0)

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('Insert a', step = 1)
# with col[1]:
#     b = st.number_input('Insert b', step = 1)
# with col[2]:
#     c = st.number_input('Insert c', step = 1)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)
# plt.plot(x,y)
# st.pyplot(fig)  

# import sys
# sys.exit()

# list1 = list([['한빛', '남자', '20', '180'], ['한결', '남자', '21', '177'], ['김한결', '충성', '51', '155'], ['한라', '여자', '20', '160']])
# n = np.array(list1)
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행', '2행', '3행', '4행'])
# df

# genre = st.radio("선택하시오", ["오름차순", "내림차순", "기타"], horizontal=True, index=2)

# number = st.number_input('Insert a number', value=20, step=1)
# st.write('The current number is ', number)
# df.iloc[3,2] = number  

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'],ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())


#     li[i] = li[i] + 3
# li 

# li = np. array([1, 2, 3, 4])
# li + 30

# li = np.array([7, 2, 5, 4])
# li
# li_sort = np.sort(li)[::-1]
# li_sort



# import turtle
# import turtle as t
# import random
# t = turtle.Turtle()
# t.shape('turtle')
# random.random()
# t.speed(0)
# t.pensize(3)
# t.penup()
# t.goto(-200, 0)
# t.pendown()

# def shape(n):
#     for i in range(n):
#         t.forward(1 + 5*i)
#         t.left(360/n)



# while True:
#     for i in range(30):
#         shape(7)
#         t.color(random.random(), random.random(), random.random())
#         t.goto(i*20, 0)
#     t.clear()
# turtle.done()






# t1.color('red')
# t1.penup()
# t1.goto(-100, 100)
# t1.pendown()
# t1.forward(100)
# t2 = turtle.Turtle()
# t2.shape('turtle')
# t2.width(5)
# t2.color('blue')
# t2.penup()
# t2.goto(-300, -100)
# t2.pendown()
# t2.forward(100)

# for i in range(30):
#     d1 = random.randint(1, 60)
#     t1. forward(d1)
#     d2 = random.randint(1, 60)
#     t2. forward(d2)




# a = np.arange(8)
# a

# a.shape = (4,2)
# a

# b = a.flatten()
# b

# b.resize((4,2))
# b

# os.system('cls')
# a = np.array([1, 10, -5, 2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(np.square(a))
# print(a**0.5)
# print(np.square(a))
# print(a**2)

# --------------------------------------
# -중간고사 2번 문제-
# n = 7
# arr = np.full((n, n), '나머지')
# arr

# for i in range(n):
#     for j in range(n):
#         # arr[i,j] = '나머지'
#         if i == j or i + j == n-1:
#             arr[i, j] = '대'
#         # if i + j == n-1:
#         #     arr[i, j] = '대'
# arr
# -------------------------------------
# -중간고사 3번 문제-
# n = 100
# for i in range(1, n+1):
#     if i%7 == 3:
#         i
# ------------------------------------
# #-----------------------------------------------------------
# # #<10월 10일>
# list1 = [[1,2,3,4], [3,5,7,9]]
# # a = np.array(list1)
# # a

# # b = np.ones((10,5))
# # b
# # c = np.zeros((10,5))
# # c
# # d = np.full((10,5),3)
# # d
# e = np.eye(5)
# e


# e
# def user_eye(n):
#     arr = np.zeros((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i ==n-j-1:
#                 arr[i,j]=1
#     return arr
# arr = user_eye(10)            
# arr


# list1= [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
# n = np.array(list1)
# n

# def arry():
#     array = [[10]*5 for _ in range(4)]
#     for k in arry:
#         k
#     return k

# def user_eye(n):
#     arr = np.full((n,n))
#     for i in range(n):
#         for j in range(n):
#             if i ==  j:
#                 arr[i, j] = 1
#             else:
#                 st.write("나머지")
#         return arr

# arr = user_eye(10)
# arr



# def user_eye(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 st.write("대각선", end = " ")
#             else:
#                 st.write("나머지", end = " ")
#         st.write()

# n = user_eye(10)
# n



# for h in range(1,n+1):
#     if h%7 == 3 :
#         h

# s= 0
# # for i in range(2,1000+1,2):
# #     s=s+i
# # s

#-----------------------------------------------------------
# #<9월 26일>
#  list_1 = [1,2,7,4,50,33]
#  s=sum(list_1)
#  mx = max(list_1)
#  mn = min(list_1)
#  s,mx, mn

# def sta(arr):
#     s = 0
#     mx = -1e10
#     mn = 1e10
#     for i in arr: 
#         s = s +i
#         if mx<i:
#             mx=i
#         mx
#         if mn>i:
#             mn=i
#         mn
#     arr
#     'sum = ', s, 'min = ', mn, 'max = ', mx
#     return s, mx, mn
# list_1 =[5,13,7,4,11]
# [s1,mx1, mn1] = sta(list_1)
# s1, mx1, mn1

# import numpy as np
# list_1 = [1,2,3,4]

# a= np.array(list_1)
# a+10
#-----------------------------------------------------------

# #리스트 생성하기
# list_1 = [1,2,3,4,5,1,3]
# list_2 =[]
# list_1
# list_2
# len(list_1)

# #리스트 변경하기
# list_1[3] = 9999
# list_1
# list_1.append(100)
# list_1
# list_1.remove(9999)
# list_1
# list_1.insert(0,777)
# list_1

# list_2 = list_1.copy()
# list_2

# import turtle 
# t = turtle.Turtle()
# n=60
# t.shape('turtle')
# t.speed(0)
# t.write("HA", move=False, align="center", font=("arial",50,"bold"))

# t.penup()
# t.sety(-100)
# t.pendown()


# # for i in range(5):
# #     t. forward(100)
# #     t.left(144)
# turtle.done()





#딕셔너리 생성하기
# dict_1={'name' : '홍길동', 
#         'birth' : '1990', 
#         'addr' : '대한민국'}
# dict_1
# dict_1['addr']

# dict_1['weight'] = 60.5
# dict_1['family'] = ['아빠','엄마','여동생']
# dict_1

# dict_1.update({'weight' : 67.8, 'hobby' : ['게임','독서']})
# dict_1

# dict_1['hobby'] = ['축구','등산']
# dict_1

# del dict_1['weight']
# del dict_1['birth']
# del dict_1['addr']
# dict_1 


# for key in dict_1.keys():
#     key
# for v in dict_1.values():
#     v 
# for k, v in dict_1.items():
#     k
#     v




# print('파이썬의 세계에 오신 것을 환영합니다.')

# st. write('파이썬의 세계에 오신것을 환영합니다.')

# st.image('im.jpg')
# st.title('스트림릿...')
# a=2+3+8

#관계연산자

# a=5
# if a==5:
#     'right!'
#     'a is 5'

# if a==3:
#     'right'
#     'a is 3'
# if a !=3:
#     'right'
#     'a is not 3'

# grade = 51
# if grade >=90:
#     "a"
# elif grade >=80:
#     "b"
# elif grade >=70:
#     "c"
# elif grade >=60:
#     "d"
# elif grade >=50:
#     "f"

#for 반복문으로 구구단 출력

# for a in range(2,10):
#     a,'단 입니다'
#     for i in range(1,10):
#         b = str(a) + 'X' + str(i) +'='+str(i*a)
#         b 

