# import theater_module

# theater_module.price(3) # 3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때 가격

# import theater_module as mv

# mv.price(3) # 3명이서 영화보러 갔을 때 가격
# mv.price_morning(4) # 4명이서 조조 할인 영화보러 갔을 때 가격
# mv.price_soldier(5) # 5명의 군인이 영화보러 갔을 때 가격

# from theater_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning

# price(3)
# price_morning(4)
# price_soldier(5) # 사용 안됨

from theater_module import price_soldier as price
price(3) # 앨리어스 사용
