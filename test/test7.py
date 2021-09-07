# \n : 줄바꿈
print("백문이 불여일견 \n백문이 불여일타")

# \" \' : 문장 내에서 따옴표
# # 저는 "나도코딩"입니다
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\ 문장내에서 \

# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine") # Pine 이 제일 앞으로 가서 자릿수 만큼 입력됨

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


domain = "http://naver.com"
# redomain = domain.replace("http://", "").replace(".com","") # . 이후 다른게 나올 수 있음 
redomain = domain.replace("http://", "")
redomain = redomain[:redomain.index(".")]
print(redomain[:3] + str(len(redomain)) + str(redomain.count("e")) + "!")