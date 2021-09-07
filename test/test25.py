# score_file = open("score.txt", "w", encoding="utf-8") # w(write) : 쓰기 
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8") # a(append) : 계속 쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r(read) : 읽기
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8") # r(read) : 읽기
# print(score_file.readline(), end="") # 줄별로 일기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf-8") # 줄 개수를 모를 때 while을 통해서 뽑아오기
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()