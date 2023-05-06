import random
import time

def fight():
        seedit = random.randint(1, 24**7)
        random.seed(seedit)
        print(f'seed for fight: {seedit}') # глобально записано переменная randseed -> seedit = светиться в принте c кодом dir()
        p1 = random.randint(random.randint(280, 310), random.randint(1000, 1500)) #выбрать случайно ( выбрать случайно минимальное число), (выбрать случайно максимальное число) число.
        dp1 = random.randint(random.randint(80, 100), random.randint(400, 500))//6 #выбрать случайно ( выбрать случайно минимальное число), (выбрать случайно максимальное число) число.
        p2 = random.randint(random.randint(280, 310), random.randint(1000, 1500))
        dp2 = random.randint(random.randint(80, 100), random.randint(400, 500))//6
        hp1 = p1 #здоровье отображаеться остаточное после боя(повторяеться для следущей строки)
        hp2 = p2
        turn = 1 #очерёдный тумблер(тоесть как контроллер очереди)
        turntime = 0 #счётчик ходов
        print("урон и здоровье случайный, для каждого игрока.")
        time.sleep(1)
        print(f"\nигрока 1, hp:{p1}, урон:{dp1}. игрока 2, hp:{p2} урон:{dp2}.")
        time.sleep(3)
        while True: #условие для окончания цикла.
                time.sleep(2)
                cube = random.randint(1, 6)
                if turn == 1:# игрок1
                        #математический подсчёт
                        lcd1=dp1*cube #умножаем урон игрока 1 на номинал выпавшего кубика
                        hp2=hp2-lcd1 # сказано - присвоить новое здоровье. Это текущей переменной количество здоровья, отняли минимальным уроном
                        #информационные сообщения.
                        print(f"\nигрок 1 атакует")
                        print(f"выпало число: {cube},наносит урон:{lcd1}")
                        print(f"очки здоровья:{hp2} у игрока 2")
                        #условия для окончания боя(когда здоровье достигает нуля или минус один)
                        if -hp2 > -1:
                                print("\nЭто конец для Player2")
                                break
                        else: #оно пропускает это условие так как оз ещё осталось
                                pass
                        turn = 2 # переменная... переключает для очереди следующему игроку.
                        turntime += 1
                elif turn == 2:
                        lcd2=dp2*cube
                        hp1=hp1-lcd2
                        print(f"\nигрок 2 атакует")
                        print(f"выпало число: {cube}, наносит урон: {lcd2}")
                        print(f"очки здоровья:{hp1} у игрока 1")
                        if -hp1 > -1:
                                print("\nЭто конец для Player1")
                                break
                        else:
                                pass
                        turn = 1
                        turntime += 1
                else:
                        print("something wrong")
                        break
        print("\nСтатистика")
        time.sleep(1)
        print(f"Имя|- Здоровье( HP )|- После боя HP\n")
        time.sleep(1)
        print(f'player1:', end=" ")
        time.sleep(1)
        print(f'({p1}) — ({hp1})')
        time.sleep(1)
        print(f'player2:', end=" ")
        time.sleep(1)
        print(f'({p2}) — ({hp2})')
        print(f'длительность ходов: {turntime}')
        time.sleep(5)
        print('Игра окончена')

fight()
