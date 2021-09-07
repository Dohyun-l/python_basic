from random import *

i = 1
person = 0

while i <= 50:
    time = randint(5, 51) # test2.py 참고 이러면 51들어갈 수 도 있음
    check = 0

    if time >= 5 and time <= 15:
        check = 1
        person += 1

    if check == 0:
        print("[   ] {}번째 손님 (소요시간 : {}분)".format(i, time))
    else:
        print("[ 0 ] {}번째 손님 (소요시간 : {}분)".format(i, time))
    i += 1

print("총 탑승 승객 : {} 분".format(person))

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[ 0 ] {}번째 손님 (소요시간 : {}분)".format(i, time))
        cnt += 1
    else:
        print("[   ] {}번째 손님 (소요시간 : {}분)".format(i, time))
print("총 탑승 승객 : {} 분".format(person))

