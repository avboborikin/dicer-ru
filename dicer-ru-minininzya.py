import random
i=0
itog=0
dice=int(input('Какой кубик вы хоитите бросить(к4, к6, к8, к10, к12, к20, к100, напишите максимальное значение кубика)'))
num=int(input('сколько кубиков этого типа вы хотите бросить'))
while i!=num:
    rez=random.randint(1, dice)
    print('бросок', i+1,' ', rez)
    itog=itog+rez
    i=i+1
print('итог броска=', itog)