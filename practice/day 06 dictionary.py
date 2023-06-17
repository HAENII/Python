#dictionary 는 key:value 로 자료값을 저장해서, key 값으로 자료값에 접근하는 방법이다. = js의 object와 같음
planets = {'수성':'Mercury' , '금성':'Venus' , '지구':'Earth' , '화성':'Mars'}

print(planets)

x = planets['지구'] #key 값을 사용해서 불러오기
y = planets.get('수성') #get 사용해서 불러오기

print(f"지구는 영어로 {x}")
print(f"수성은 영어로 {y}")

planets['목성'] = 'Jupiter'
print(planets)

del planets['금성']
print(planets)