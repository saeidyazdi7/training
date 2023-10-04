o = open("boss.txt", "r", encoding="utf-8")
# s = ("YazdiΩ")
# if o.writable():
#     print(o.write(s))
if o.readable():
    print(o.readline())
