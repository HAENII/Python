s = "a b c d e f g"
print(f"s      : {s}")

r = s.split()
print(f"s.split: {r}")

se = "aa.bb.cc.dd.ee.ff.gg"
print(f"s          : {s}")

r0 = se.split()
r1 = se.split('.')
r2 = se.split('.', 4)
print(f"\n s.split() \n {r0}")
print(f"\n s.split('.') \n {r1}")
print(f"\n s.split('.' , 4) \n {r2}")
