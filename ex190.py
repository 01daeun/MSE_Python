apart = [ [101, 102], [201, 202], [301, 302] ]
# apart는 3 by 2 array(3행 2열의 배열)
for row in apart: # row는 행을 의미
    for col in row: # col은 열을 의미
        print(col, "호")        
# 첫번째 for문은 행이 3개이므로 3번 실행하게 된다.
# 두번째 for문은 열이 2개이므로 2번 실행한 뒤 첫번째 for문으로 되돌아간다.

print("-" * 5) # 마지막에 -를 5번 실행한다.