# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {}".format(waiting_no))

for waiting_no in range(5): # 0 ~ 4
    print("대기번호 : {}".format(waiting_no))

for waiting_no in range(1, 6): # 1 ~ 5
    print("대기번호 : {}".format(waiting_no))

for waiting_no in range(3, 9): # 3 ~ 8
    print("대기번호 : {}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{}, 커피가 준비 되었습니다.".format(customer))