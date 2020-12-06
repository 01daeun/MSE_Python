def 함수0(num) : # 밑에 있는 값을 받은 뒤 실행된다.
    return num * 2 # 14*2의 값이 c의 값이 된다.

def 함수1(num) : # 밑에 있는 값을 받은 뒤 실행된다.
    return 함수0(num + 2) # 함수0(12 + 2)가 되서 def 함수0(num):으로 되돌아간다.

def 함수2(num) : # 제일 밑에 있는 c = 함수2(2)로 인해 num 값이 2가 되서 실행된다.
    num = num + 10 # 2 + 10 = num이 된다.
    return 함수1(num) # 함수1(12)가 되서 def 함수1(num):으로 되돌아간다.

c = 함수2(2)
print(c)