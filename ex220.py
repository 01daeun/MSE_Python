def print_max(a, b, c) :
    max_val = 0 # 초기값 = 0
    if a > max_val : # a > 0 일 경우 실행, 아닐 경우 건너 뜀
        max_val = a # 초기값 = a
    if b > max_val : # b > a 일 경우 실행, 아닐 경우 건너 뜀
        max_val = b # 초기값 = b
    if c > max_val : # c > b 일 경우 실행, 아닐 경우 건너 뜀
        max_val = c # 초기값 = c 
    print(max_val) # 위에서 만족하는 값을 출력한다.
    
print_max(1, 2, 3)