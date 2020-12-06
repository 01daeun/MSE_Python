리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트: # 변수 = '리스트' 안의 값
    split = 변수.split(".") #split()은 ()안의 값을 기준으로 문자열을 분리하여 리스트를 리턴한다.
    if (split[1] == "h") or (split[1] == "c"): # split한 뒤의 값이 h나 c일 경우 if문을 실행한다.
        print(변수)