from functools import reduce

x = [49, 80, 20, 100, 80]
y = [43, 60, 85, 30, 90]
z = [49, 82, 48, 50, 100]


f = lambda x,y,z:(x + y + z)/3

print("학생별 평균 :", list(map(f, x, y, z)))

total = list(map(f, x, y, z))

print("전체 평균 :", reduce(lambda x, y:(x+y)/2, total))
