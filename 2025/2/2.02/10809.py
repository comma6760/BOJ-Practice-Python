#check = [-1 for _ in range(26)]
#"abcd"
#check[chr(a) -chr('a')]

a = "abcdefghijklmnopqrstuvwxyz"
s = input()#스트링 자체가 리스트임. 대신 상수리스트인 튜플 형태
for i in range(len(a)):
    print(s.find(a[i]), end= ' ')