# import travel.thailand
# # import travel.thailand.ThailandPackage # .(마지막) - 모듈이나 패키지만 가능 / 클래스나 함수는 X
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
print(inspect.getfile(thailand))