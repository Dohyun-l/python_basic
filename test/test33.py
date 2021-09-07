try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError: # 잘못된 값이 들어왔을때! ex) 수식에 문자
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 0으로 나눌 때
    print(err)
# except: # 모든 에러
#     print("알 수 없는 에러가 발생하였습니다.")
except Exception as err: # 모든 에러
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)