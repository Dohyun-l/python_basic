print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(n) n칸을 사용하며 왼쪽정렬, rjust(n) n칸을 사용하며 오른쪽정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # zfill(n) n칸 사용하며 빈칸은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")