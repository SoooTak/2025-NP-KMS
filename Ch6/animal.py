from abc import ABC, abstractmethod

class Animal(ABC):
    animal_count = 0                        # 클래스 변수로 동물 객체 수를 지정

    def __init__(self):
        Animal.animal_count += 1

    @abstractmethod
    def sound(self):
        pass

    @staticmethod
    def get_animal_count():
        return Animal.animal_count          # 현재 동물 객체 수 반환

class Dog(Animal):
    def __init__(self, name):               # 생성자에서 이름을 초기화 
        super().__init__()                  # 부모 클래스의 생성자 호출
        self.__name = name

    def sound(self):
        return f"{self.__name}이 멍멍하고 울어요"

class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.__name = name
    
    def sound(self):    # 추상 메소드 구현
        return f"{self.__name}이 야옹하고 울어요"


if __name__ == "__main__" :
    mydog : Dog = Dog("춘식이")
    mycat : Cat = Cat("야옹이")
    print(mydog.sound())
    print(mycat.sound())
    print("현재 동물 수 : ", Animal.get_animal_count())
    
 #anymal = Animal = Animal()  # 추상 클래스는 객체 생성 불가
 
    anymal : Animal = Dog("바둑이")
    print(anymal.sound())
    print("현재 동물 수 : ", Animal.get_animal_count())
    
    anymalList = [Dog("토리"), Cat("나비"), Dog("멍멍이"), Cat("고양이")]
    for animal in anymalList :
        print(animal.sound())