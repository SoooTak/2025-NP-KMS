#202311388 김민상
def plus(num) :
    list = []
    temp = 0
    for i in range(len(str(num))) :
        list.append(num % 10)
        num //= 10
    for i in range(len(list)) :
        temp += list[i]
    return temp

num = int(input("숫자 : "))
print(plus(num))