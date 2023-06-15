import random
import time

main_art = """!!quiz!!"""

print(main_art)
print()
print("수학 퀴즈 입니다.")
print("문제를 풀어보세요")
print()

score = 0

start_tm = time.time() # 타이머 시작
for i in range(1,11) : 
    su1 = random.randint(1,10) # 1부터 10까지 랜덤숫자를 가져오기
    su2 = random.randint(1,10) # 위와 동일
    
    print(f"{i}번 문제입니다.")
    
    answer = su1 * su2
    player = int(input(f"{su1}*{su2} = "))
    
    if answer == player : 
        score += 1
        print(f"정답입니다. 현재 점수는 {score}입니다.")
        print()
    
    else: 
        score -= 1
        print(f"정답입니다. 현재 점수는 {score}입니다.")
        print()
        
end_tm = time.time() # 타이머 끝

print(f"{round(end_tm - start_tm)}초 동안 총 {i}문제를 푸셨습니다.") #round 는 소수첫째점에서 반올림
print(f"당신의 점수는 {score}점 입니다.")
print("퀴즈가 종료되었습니다.")

