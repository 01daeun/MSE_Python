import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 위의 두 줄은 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.(문제에 있는 것)

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
# float는 소수점이 있는 숫자로 변환하는 작업을 해준다.
# 변동폭은 max_price(최근 24시간 내 최고 거래금액)에서 min_price(최근 24시간 내 최소 거래금액)을 빼준 값이다.
# 시가는 최근 24시간 내 시작 거래금액을 의미한다.
# 최고가는 최근 24시간 내 마지막 거래금액을 의미한다.

if (시가+변동폭) > 최고가: # (시가+변동폭)이 최고가 보다 클 경우는 if를 실행하고, 아닐 경우는 else를 실행한다.
    print("상승장")
else:
    print("하락장")