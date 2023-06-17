# 시간구하기 예제
print("당신의 python 공부 시간을 알려주세요")
time = int(input("오늘의 파이썬 공부 시간은 몇분 인가요?\n"))
a = time // 60
b = time % 60
print(f"당신의 총 공부 시간은 {a}시간{b}분 입니다.")