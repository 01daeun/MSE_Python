def message1(): # message1()의 값은 A를 출력한다.
    print("A")

def message2(): # message2()의 값은 B를 출력한다.
    print("B")

def message3():
    for i in range (3) : # 총 3번 반복한다.
        message2() # message2()의 값인 B를 출력한다.
        print("C") # message2()의 값인 B에 한 줄 띄고 C를 출력한다.
    message1() # for문이 다 끝난 값에 한 줄 띄고 message1()의 값인 A를 출력한다.
    #위의 내용이 message3()의 값이 된다.

message3()