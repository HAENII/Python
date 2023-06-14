store = """ !!burger store!!"""
menu = """
불고기버거 : 5,500원
치즈버거 : 4,500원
에그버거 : 4,000원
콜라 : 2,000원
사이다 : 2,000원

각 버거 세트메뉴 있습니다. 
세트메뉴 주문 시 500원 할인됩니다."""
print(store)
print("#"*40)
print(menu)
print("#"*40)

burger = input("버거를 선택해주세요. 예> 불고기 , 치즈, 에그 >>> ")
drink = input("음료를 선택해주세요. 예> 콜라, 사이다 >>>")
combo = input("세트메뉴 주문하시겠습니까? 예> 네, 아니오 >>>")

b_price = 0
d_price = 0
price = 0

#햄버거 주문
if burger == "불고기" :
    b_price = 5500
    print(f"선택한 버거는 {burger}이고 가격은 {b_price}원 입니다.")
elif burger == "치즈" : 
    b_price = 4500
    print(f"선택한 버거는 {burger}이고 가격은 {b_price}원 입니다.")
elif burger == "에그" : 
    b_price = 4000
    print(f"선택한 버거는 {burger}이고 가격은 {b_price}원 입니다.")
else: print("선택한 버거는 메뉴에 없습니다.")


#음료 주문
if drink == "콜라" :
    d_price = 2000
    print(f"선택한 음료는 {drink}이고 가격은 {d_price}원 입니다.")
elif drink == "사이다" :
    d_price = 2000
    print(f"선택한 음료는 {drink}이고 가격은 {d_price}원 입니다.")
else: print("선택한 음료는 메뉴에 없습니다.")

# 총 금액
if combo == "네" :
    price = b_price + d_price
    price -= 500
    print(f"총 금액은 {price}원 입니다.")
else :
    price = b_price + d_price
    print(f"총 금액은 {price}원 입니다.")