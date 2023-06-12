# random 모듈을 import 해서 사용할 수 있는 부가적인 모듈들

#   random() : 0 ~ 1 사이의 임의 float 리턴
#import random
#print(random.random())

#   randint(a,b) : a~b 사이의 임의 int 리턴
#import random
#print(f"선택한 수는 : {random.randint(0,5)} 입니다.")

#   uniform(a,b) : a~b 사이의 임의 float 리턴

#import random
#a = random.uniform(1.14, 36.5)
#print(f"1.14와 36.5 사이에서 선택한 수는 {a} 입니다.")

#   randrange(a,b,c) : a~b 사이에서 c 간격으로 임의 int 리턴
#import random
#a = random.randrange(5, 20 , 1)
#print(f"5와 20 사이에서 선택한 수는 {a} 입니다.")

#   shuffle(a) : 배열 안의 값들을 shuffle 후 리턴
#import random
#a = ['apple' , 'book' , 'cat' , 'dog' , 'bat']
#random.shuffle(a)
#print(f"{a}입니다.")

#   choice(a) : 배열 안의 값 중 임의 choice 해서 리턴
#import random
#a = ['apple' , 'book' , 'cat' , 'dog' , 'bat']
#print(f"{random.choice(a)}입니다.")

#   choices(a,b,c) : 배열 a의 값에 b 가중치를 각각 지정 후 리턴 (가중치가 큰 값을 리턴하는 경우가 많음) 
#import random
#a = random.choices([1,2,3,4,5] , [10, 10, 20, 20, 5])
#print(f"{a} 입니다.")

#   sample(a,b) : 배열 a의 값중 b 숫자의 개수만큼 리턴 

import random
a = [1,2,3,4,5,6,7,8,9,10]
b = random.sample(a, 3)
print(f"{b} 입니다.")