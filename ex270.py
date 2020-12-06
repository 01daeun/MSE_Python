class Stock:
    def __init__(self, name, code, per, pbr, dividend): # __init__는 class를 정의하면서 동시에 초기화를 한다.
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성) # 리스트 형태의 종목에 삼성의 data를 마지막 부분에 추가한다.
종목.append(현대차) # 리스트 형태의 종목에 현대차의 data를 마지막 부분에 추가한다.
종목.append(LG전자) # 리스트 형태의 종목에 LG전자의 data를 마지막 부분에 추가한다.

for i in 종목: # 총 3개의 종목이 생성되었는데 삼성이 추가된 종목부터 실행시킨다.
    print(i.code, i.per)
# i.code는 위의 class에서 (code)에 위치한 값, i.per은 위의 class에서 (per)에 위치한 값을 출력한다.
# 출력해야되는 값은 리스트 함수(stock된)인 종목에 위치한 값이다.