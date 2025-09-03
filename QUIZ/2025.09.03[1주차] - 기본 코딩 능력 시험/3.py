#202311388 김민상

def big(a, b):
    num1 = a+b
    num2 = a<<b
    num3 = a*b
    if(num1 > num2) :
        if(num1 > num3) :
            return num1
        else :
            return num3
    else :
        if(num2 > num3) :
            return num2
        else :
            return num3
        
num1 = int(input("1"))
num2 = int(input("2"))
print(big(num1, num2))
