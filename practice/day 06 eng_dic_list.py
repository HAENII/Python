title = """!!!This is a eng_dictionary!!!"""

print(title)
print()
print("나만의 영어사전 만들기")
print("*"*80)

voca = ['apple:사과' , 'book:책' , 'desk:책상']
user = 0
while user != "4": #false 일때 반복을 멈추고 종료.
    # for i in range(3):
    #     print(f"{voca[i]}")

    #for i in voca : # range 가 아닌 리스트이름을 사용해서 출력할 수 있다.
    #    print(f"{i}")
    use = ("""
    ===사전 수정모드===
    1. 등록된 단어 보기
    2. 단어 추가하기
    3. 단어 삭제하기
    4. 사전수정모드 종료하기
    """)

    print(use)

    user = input("원하는 기능을 선택하세요.(숫자만 입력) >>> ")

    if user == '1':
        print()
        print("===등록된 단어===")
        for i in voca:
            print(f"{i}")
    elif user == "2":
        print("===단어 추가하기===")
        user_dict = input("추가하고 싶은 단어를 입력하세요(단어:뜻) >>> ")
        voca.append(user_dict)
        print(f"{user_dict} 가 추가되었습니다.")
        print(f"현재 리스트는 다음과 같습니다.\n {voca}")
    elif user == "3":
        print("===단어 삭제하기===")
        del_voca = input("삭제하고싶은 단어를 입력하세요(단어:뜻) >>> ")
        voca.remove(del_voca)
        print(f"{del_voca}가 삭제되었습니다.")
        print(f"현재 리스트는 다음과 같습니다.\n {voca}")