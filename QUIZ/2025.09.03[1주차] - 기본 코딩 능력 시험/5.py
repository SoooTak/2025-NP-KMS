#202311388 김민상
def plus(n, m) :
    num = n
    p = 2
    print(f"1회차 : {num}")
    for i in range(n, m) :
        num += 1
        print(f"{p}회차 : {num}")
        p+=1

n = int(input("n : "))
m = int(input("m : "))
plus(n, m)