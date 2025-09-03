#202311388 김민상
def hol(num1, num2) :
    temp = 0
    list1 = []
    for i in range(num1, num2) :
        if(i % 2 == 1) :
            temp += i
            list1.append(i)
    print(f"{num1}, {num2} 사이의 홀수 : {list1}")
    print(f"그 사이 홀수들의 합 : {temp}")
    
num1 = int(input("정수1 : "))
num2 = int(input("정수2 : "))
hol(num1, num2)