if True :
    if False: # True가 아니기 때문에 else로 넘어간다.
        print("1")
        print("2")
    else: # if가 False였으므로 else는 True가 되기 때문에 3을 출력한다.
        print("3")
else : # if에서 값을 출력했기 때문에 여기에 있는 else는 값을 출력하지 않는다.
    print("4")
print("5") # if문과는 무관하게 5를 출력한다.