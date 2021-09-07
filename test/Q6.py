def std_weight(height, gender):
    if gender == "남자":
        return round(pow(height,2) * 22 / 10000, 2)
    else:
        return round(pow(height,2) * 21 / 10000, 2)

height = 175
gender = "여자"
print("키 {}cm {}의 표준 체중은 {}kg입니다.".format(height, gender, std_weight(height, gender)))