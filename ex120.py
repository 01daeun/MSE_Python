fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
# fruit의 value : 딸기, 토마토, 사과
# user의 값에 fruit의 value가 해당하면 if의 값을 해당하지 않을 경우엔 else의 값을 출력한다.