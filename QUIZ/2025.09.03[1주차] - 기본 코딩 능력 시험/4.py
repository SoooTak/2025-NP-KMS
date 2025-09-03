#202311388 김민상
def formatt(num) :
    print(f" 10진수: {num}")
    print(f" 2진수: {format(num,'b')}")
    print(f" 8진수: {format(num,'o')}")
    print(f"16진수: {format(num,'x')}")
    
n = int(input("정수 1개 입력 : "))
formatt(n)
#format : 문자열 구성 및 출력시 사용
