"""
Main File, with all functions and work done
"""
import time

from countsmth import rivnynnya
from readingfiles import intruction, userequat, known_roots
from rivn import calc_matrices, beat_output, all_elements


print(intruction("intro"))
time.sleep(2)

print(2*'\n')

# print(intruction("choice_first"))
# print('\n')

def asking_output():
    
    def mainn():
        print(intruction("choice_first"))
        print('\n')
        time.sleep(1)
        answer = input("Type here: ")
        print('\n')
        if answer not in ['1', '2', '3', '4']:
            time.sleep(1)
            print("Try that again")
            time.sleep(1)
            print('\n')
            print(asking_output())
            mainn()
        if answer == '1':
            time.sleep(1)
            print("Приклад: " + '\n' + 'r**1 - r**0' + '\n')
            time.sleep(1)
            ask_2 = input("Введіть рівняння формату як в прикладі: ")
            print("Це <'r**1 - r**0'> те сме, що і <'r**1 - r**0' = 0>")
            print("Не додавайте '=0' в кінці!")
            # mainn()
            try: 
                print(rivnynnya(ask_2))
            except SyntaxError:
                time.sleep(1)
                print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
                print(asking_output())
            mainn()
        if answer == '2':
            print(intruction("instructions"))
            time.sleep(2)
            rivn = userequat()
            known_r = known_roots()
            time.sleep(1)
            ask_3 = input("Введіть кількість перших членів: ")
            time.sleep(1)
            # rivn = userequat()
            try:
                print(beat_output(all_elements(rivn, known_r, int(ask_3))))
            except ValueError:
                time.sleep(1)
                print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
                print(asking_output())
            mainn()
        if answer == '3':
            print(intruction("instructions"))
            time.sleep(2)
            rivn = userequat()
            time.sleep(1)
            known_r = known_roots()
            time.sleep(1)
            ask_3 = input("Введіть номер шуканого члена: ")
            time.sleep(1)
            try:
                print('a({}) = {}'.format(int(ask_3), calc_matrices(rivn, known_r, int(ask_3))))
            except ValueError:
                time.sleep(1)
                print("ВиНиКлА пОмИлКа 0_о" + '\n' + 'Спробуйте ще раз!')
                print(asking_output())
            mainn()
        if answer == '4':
            print('Дякую, що скористалися, до зустрічі')

    mainn()
asking_output()
# time.sleep(1)

# def cicl():
#     """
#     to ask many times
#     """
#     def mainnn():

#         print("Чи бажаєте використати програму ще раз?")
#         time.sleep(1)
#         print("Так - введіть 1" + '\n' + 'Ні - введіть 2')
#         time.sleep(1)
#         answer = input("Вводіть тут: ")
#         if answer == '2':
#             print('Дякую, що скористалися, до зустрічі')

#         if answer == '1':
#             print(asking_output())
#             time.sleep(1)
#             mainnn()
#         else: 
#             print("ERROR")
#             time.sleep(1)
#             mainnn()
#     mainnn()
# cicl()
