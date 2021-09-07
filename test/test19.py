# def profile(name, age, main_lang):
#     print("이름 : {}\t나이 : {}\t 주 사용 언어: {}"\
#         .format(name, age, main_lang)) # \ <- 역 슬러쉬을 사용하면 줄바꿔서 계속 코딩 가능

# profile("유재석", 20, "파이썬")
# profile("김태호", 20, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t 주 사용 언어: {}"\
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")