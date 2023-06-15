import time
print(time.time())
print(time.localtime(time.time()))

tm = time.localtime()
print(f"년: {tm.tm_year}")
print(f"월: {tm.tm_mon}")
print(f"일: {tm.tm_mday}")
print(f"시: {tm.tm_hour}")
print(f"분: {tm.tm_min}")
print(f"초: {tm.tm_sec}")

now = time.localtime()
print(time.strftime('%Y%m%d' , now)) >>> %Y : 네 자리수 연도 // %m : 숫자 월 // %d : 숫자 일
print(time.strftime('%c', now)) >>> 날짜,요일,시간을 현재 시간대에 맞춰 출력
print(time.strftime('%x', now)) >>> 현재 시간대 월/일/년도 출력
print(time.strftime('%X', now)) >>> 현재 시간대 시/분/초 출력
print(time.strftime('%H%M%S', now)) >>> %H : 시간(24시간) / %M : 분 / %S : 초



