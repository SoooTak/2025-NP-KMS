#202311388 김민상
def count(st, s) :
    list2 = []
    temp = 0
    for i in range(0, len(st)) :
        if(st[i] == s) :
            list2.append(i)
            temp += 1
    print(f"원본 문자열 : {st}, 찾는 문자 : {s},")
    print(f"위치 : {list2}, 개수 : {temp}")
    return list2, temp
    
st = input("문자열 : ")
s = input("문자 : ")

listtest, counttest = count(st, s)