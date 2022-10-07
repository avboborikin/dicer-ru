import random
i=0
result=0
dice=int(input('Какой кубик вы хоитите бросить(к4, к6, к8, к10, к12, к20, к100, напишите максимальное значение кубика)'))
num=int(input('сколько кубиков этого типа вы хотите бросить'))
while i!=num:
    roll=random.randint(1, dice)
    print('бросок', i+1,' ', roll)
    result=result+roll
    i=i+1
print('итог броска=', result)