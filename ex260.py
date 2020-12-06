class OMG :
    def print() : # 함수값 존재 안함
        print("Oh my god")


mystock = OMG()
mystock.print() # OMG.print(mystock)가 된다.
# 처음에는 ()에 아무것도 존재하지 않지만 마지막에는 ()안에 값이 생겼기 때문에 오류가 발생한다.