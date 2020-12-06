per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
# 첫 실행에서 실행값이 try에서 '10.31'을 출력하고, 예외가 발생하지 않았으므로 'clean data'를 출력하고, finally의 값을 출력해준다.
# 두번째 실행에서 실행값이 try에서 출력값이 없으므로 예외가 발생하게 된다. 그래서 0을 출력하게 되고, finally의 값을 출력해준다.
# 마지막 실행에서 실행값이 try에서 '8.00'을 출력하고, 예외가 발생하지 않았으므로 'clean data'를 출력하고, finally의 값을 출력해준다.