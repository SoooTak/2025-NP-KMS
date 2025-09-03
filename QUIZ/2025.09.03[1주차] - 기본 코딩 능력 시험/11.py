#202311388 김민상
def func() :
    people = []

    while(True) :
        name = input("이름 : ")
        if name == "0" :
            break
        age = input("나이 : ")
        if age == "0" :
            break
        number = input("전화번호 : ")

        people.append([name, age, number])

    return people

def printf(people) :
    for i in range(len(people)) :
        print(f"{i+1} : {people[i]}")
        
printf(func())