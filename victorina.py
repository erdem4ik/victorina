l1ose = int(0)
score = int(0)
b = 0 #Пропуск о прохождении лвл 1 матем
c = 0 #Пропуск о прохождении лвл 2 матем
d = 0 #Пропуск о прохождении лвл 3 матем
g = 0 #Пропуск о прохождении лвл 1 геогр
e = 0 #Пропуск о прохождении лвл 2 геогр
h = 0 #Пропуск о прохождении лвл 3 геогр
global l1ose, score,a,b,c,d,g,e,h
def math():
    global l1ose, score, a, b
    print("Выбери сложность")
    print("Если вы выбирали сложность и прошли её выберите другую в ином случае вы выбываете.")
    print("0-Низкая сложность, 1-средняя сложность, 2- высокая сложность")
    a = int(input())
    if a == 0:
        if b != 1:
            print("Отлично давай начнем с низкой сложности!")
            print("Первый вопрос")
            print("Выберите правильный порядрок выполнения действий")
            print("0-(Скобки,умножение/деление,сложение/вычитание), 1-(сложение/вычитание, деление/умнодение, скобки),2-(деление/умножение, скобки, сложение/вычитание)")
            a = int(input())
            if a == 0:
                print("Молодец! Верно")
                score = score + 1
            else:
                print("Не верно в следующий раз повезет")
                print(score)
                l1ose = l1ose + 1
                exit()
            print("Второй вопрос")
            print("Можно ли делить на 0")
            print("0-да, 1-нет")
            b = int(input())
            if a == 1:
                print("Молодец, верно")
                score = score + 1
            else:
                print("Не в этот раз в другой раз повезет.")
                l1ose = l1ose + 1
                exit()
            print("Третий вопрос")
            print("Дайте верный ответ на пример 94+46-100/5*(60)")
            a = int(input())
            if a == -1060:
                print("Верно, молодец!")
                b = 1
            else:
                l1ose = l1ose + 1
                exit()
        else:
            print("Tы проходил этот уровень!")
            print("За попытку обмануть систму вы проиграли викторину!")
            print(score)
            l1ose = l1ose + 1
    elif a == 1:
        if c != 1:
               print("Приветствую вас на среднем уровне!")
               print("Первый вопрос- Правда ли, что любое число в 0 степени = 1")
               print("Да-1, Нет-2")
               a = int(input())
               if a == 1:
                   print("Молодец.Верно")
                   score = score + 1
               else:
                   print("Ну нет это неверно")
                   l1ose = l1ose + 1
                   print(score)
                   exit()
               print("Второй вопрос- Назовите теорему пифагора")
               print("Да-1, Нет-2")
               a = int(input())
               if a == 1:
                   print("Верно!")
                   score + score + 1
               else:
                   print("Похоже это твой предел")
                   l1ose = l1ose + 1
                   exit()
        else:
            print("Tы проходил этот уровень!")
            print("За попытку обмануть систму вы проиграли викторину!")
            print(score)
            l1ose = l1ose + 1

def geo():
    global l1ose, score, a, g, e, h
    print("Приветсвую на предмете история!")
    print("Куда отправимся?")
    print("Древний Египет - 0,Древняя Греция - 1, Древняя Италия - 2")
    a = int(input())
    if a == 0:
        if g != 1:
            print("Вопрос - для кого строили пирамиды и для чего? ")
            print("Для фараонов и захоронения их - 1, Для королей и проживания там - 2, Для всего народа и проживания там - 3")
            a = int(input())
            if a == 1:
                print("Верно!")
                score = score + 1
            else:
                print("Не верно")
                print(score)
                l1ose = l1ose + 1
                exit()
            print("Следующий вопрос - Где находился Древний египет и кто был правителем?")
            print("Северо-запад Африки и правил народ - 1, Северо-восток Африки и правитель был фараон - 2, Центр Евразии и правил президент - 3")
            a = int(input())
            if a != 2:
                print("Не верно!")
                l1ose = l1ose + 1
                print(score)
                exit()
            else:
                print("верно!")
                score = score + 1
                g = 1
        else:
            print("Tы проходил этот уровень!")
            print("За попытку обмануть систму вы проиграли викторину!")
            print(score)
            l1ose = l1ose + 1
    elif a == 1:
        if e != 1:
            print("Вопрос - кто-нибудь смог перенять культуру Древней Греции ")
            print("Да, это Великая Римская Империя - 1, Нет - 2, Да, Современная Греция - 3")
            a = int(input())
            if a == 1:
                print("Верно!")
                score = score + 1
            else:
                print("Упс! Ошибся")
                l1ose = l1ose + 1
                print(score)
                exit()
            print("Следующий вопрос - Где находилась Древняя Греция?")
            print("Европа - 1, Северная Африка - 2, Восточная Европа - 3")
            a = int(input())
            if d == 3:
                print("Верно!")
                score = score + 1
                e = 1
            else:
                print("Неверно!")
                print(score)
                l1ose = l1ose + 1
                exit()
        else:
            print("Tы проходил этот уровень!")
            print("За попытку обмануть систму вы проиграли викторину!")
            print(score)
            l1ose = l1ose + 1
    elif a == 2:
        if h != 1:
            print("Вопрос - Где зародилась такая страна, как Италия(Великая Римская Империя)?")
            print("Пиренейский полу-остров - 1, Мальдивы - 2, Австралия - 3")
            a = int(input())
            if a == 1:
                print("Верно!")
                score = score + 1
                print("Следующий вопрос - На какие части была поделина Великая Римская Империя?")
                print("На северную и западную - 1, На северную и южную - 2, Восточную и западную - 3")
                a = int(input())
                if a == 3:
                    print("Верно!")
                    score = score + 1
                    h = 1
                else:
                    print("Нееет! Ты проиграл!")
                    print(score)
                    l1ose = l1ose + 1
                    exit()
            else:
                print("Неверно!")
                print(score)
                l1ose = l1ose + 1
        else:
            print("Tы проходил этот уровень!")
            print("За попытку обмануть систму вы проиграли викторину!")
            print(score)
            l1ose = l1ose + 1

    else:
        print("Сомневаюсь, что ты после такого выбора решишь вопрос! ")
        print(score)
        l1ose = l1ose + 1


print ("Привет давай сыграем в викторину")
a = int(input("1-да 2-нет"))
if a == 1:
    print("Отлично давай начнем!")
    while l1ose != 1:
        print("Выбор игрока")
        print("Выберите предмет: 0-Математика, 1-история, 2-география, 3-информатика")
        a = int(input())
        if a == 0:
            def math():
        elif a == 1:
            def geo():
        else:
            exit()


    print("Ты ответил на все вопросы!")
    print("Игра закончена!")
    print("Твой счет - ", score)
elif a == 2:
     print("А зачем начинал?")
     exit()
else:
    print("Ты не понял вопрос?")
    exit()