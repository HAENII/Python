import random
quiz = """Hi welcome to quiz game"""

print(quiz)
print("1~30사이의 숫자가 있습니다.")

computer_su = random.randint(1,30)
user_su = 0
count = 0

while computer_su != user_su:
    user_su=int(input("컴퓨터가 뽑은 숫자는 무엇일까요?"))
    count +=1

    if computer_su > user_su :
        print("더 큰 수 입니다.")
    elif computer_su < user_su : 
        print("더 작은 수 입니다.")

print(f"정답입니다. 컴퓨터가 선택한 숫자는 {computer_su}입니다.")
print(f"총 {count}번만에 성공하셨습니다.")