r = float(input("원의 반지름을 입력해주세요 \n"))
print(f"원의 넓이는? {r*r*3.14}")
print(f"원의 넓이(거듭제곱)는? {r**2*3.14}")
#2^7 (2의 7승) = 2**7, r^2 = r**2
# round(a/b , 1) 결과값: 소수자리수 1자리까지 출력한다. 
r = float(input("원의 반지름을 입력해주세요 \n"))
print(f"원의 넓이는? {r*r*3.14}")
print(f"원의 넓이(거듭제곱)는? {round(r**2*3.14 , 2)}")