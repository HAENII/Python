import random

print("이 시스템은 당신의 나이가 컴퓨터가 임의 지정한 숫자가 같을때까지 반복됩니다.")
print("-"*80)

age = int(input("당신의 나이를 입력해주세요"))
computer_age = random.randint(1,100)
print(computer_age)

if age != computer_age:
    
