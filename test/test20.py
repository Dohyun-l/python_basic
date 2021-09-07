def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t 주 사용 언어: {}"\
        .format(name, age, main_lang))

profile(name="유재석", main_lang="파이썬", age=20)
profile(age=17, main_lang="자바", name="김태호")