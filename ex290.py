class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모): # 제일 마지막 줄에 '나 = 자식()'이 있으므로 이 class 실행
    def __init__(self):
        print("자식생성") 
        super().__init__() # 위의 class의 모든 instance를 제한 없이 사용하게 해준다.
        # 먼저 '자식생성'을 출력하고 처음 class를 실행한다.

나 = 자식()