import random
print("컴퓨터가 선택한 숫자를 맞춰 보세요.")
value = int(input("1부터 10까지 숫자 중 한개를 선택하세요. \n"))
computer = random.randint(1, 10)

if computer == value : 
    print("축하합니다. 정답입니다.")
else : 
    print(f"틀렸습니다. 컴퓨터가 선택한 숫자는 {computer} 입니다.")