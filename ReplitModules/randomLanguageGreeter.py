from random import randint

greetings = ["Hello", "こんにちは", "Hallo", "Привет", "Салом", "مرحبًا"]


for i in range(10):
    randomGreetingNum = randint(0, greetings.__len__() - 1)

    print(randomGreetingNum)

    print(greetings[randomGreetingNum])
