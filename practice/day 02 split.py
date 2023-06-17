# 이스케이프시퀀스
# \n : 엔터키 
# \t: 탭키
# \\: 원화 기호출력

a , b = input("곱셈할 두 수를 입력하세요 ex> 5 3 \n").split() # 5와 3 두개의 숫자로 입력받게 된다. 변수를 , 로 나누어 각각 값을 저장한다.
print(f"{a} * {b} = {int(a) * int(b)} 입니다.")
print(f"{a} + {b} = {int(a) + int(b)} 입니다.")
print(f"{a} - {b} = {int(a) - int(b)} 입니다.")
print(f"{a} / {b} = {int(a) / int(b)} 입니다.")