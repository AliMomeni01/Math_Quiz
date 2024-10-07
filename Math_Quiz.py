import time
import random

def math_quiz():
    a = random.randint(1,10)
    b = random.randint(1,10)
    operators = '-','+','*'
    random_operators = random.choice(operators)
    print(f'{a} {random_operators} {b}')
    if random_operators == '-':
        return a - b
    elif random_operators == '+':
        return a + b
    else:
        return a * b 
    
count_b = 5
count_s = 0
point=0
time_limit = 5
while count_b>count_s:
    count_s +=1
    result = str(math_quiz())
    start_time = time.time()
    customer = input('Enter your answer: ')
    end_time = time.time()
    time_dif = end_time - start_time
    if time_dif < time_limit:
        if result == customer : 
            point +=1 
            print(f'Perfect, Point: {point}')
        else:
            print('It is wrang')
    else: 
        print('Time ist finished')
print (f'Finall point:{point} out of {count_s}')