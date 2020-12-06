low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i]) # append()는 리스트 형태의 데이터에 ()안의 값을 추가하는 것이다.
    # volatility에 high_prices의 첫번째 값과 low_prices의 두번째 값을 뺀 값을 추가한다.
    # 위의 내용을 low_prices의 길이만큼 실행한다.
    
print(volatility)