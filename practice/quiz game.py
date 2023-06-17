import random
import time

game_title = """!!!Welcome to quiz game!!!"""

print(game_title)
print("------------------------------------------------")
print("게임의 규칙 \n >>> 이 게임은 사칙연산 풀이 게임입니다. \n >>> 유저는 컴퓨터가 제시하는 사칙연산 문제를 해결해주시면 됩니다. \n >>> 사칙연산 한단계를 통과하시면 다음 단계로 넘어갈 수 있습니다.")

score = 0

start_tm = time.time()
for i in range(1,6):
    su1 = random.randint(1,10)
    su2 = random.randint(1,10)

    print(f"{i}번째 문제입니다.")
    
    quiz_plus = su1 + su2
    quiz_minus = su1 - su2
    quiz_muitiply = su1 * su2
    
    user_answer = int(input(f"{su1} - {su2} = "))
    
    if user_answer == quiz_minus : 
        score += 1
        print(f"정답입니다. 지금까지 {score}점을 획득하셨습니다.")
    else :
        score -= 1
        print(f"틀렸습니다. 지금까지 {score}점을 획득하셨습니다.")
        
end_tm = time.time()
print(f"총 점수는 {score}점입니다. 총 시간은 {round(end_tm - start_tm)}초 걸렸습니다.")

if score >= 4:
    print(f"총 점수가 4점 이상인 경우 다음 단계가 자동진행 됩니다.")
