max1 = 0
max2 = 0
a = []

for i in range(10):

    print("정수를 입력해주세요. 종료하고 싶으시면, 0을 입력하세요.")
    a.append(int(input()))

    if (a[i] != 0):
        if(a[i] > max1):
            max2 = max1
            max1 = a[i]
        elif(a[i] > max2):
            max2 = a[i]
        else:
            max2 = max2
            
    else:
        break


print("두번째로 큰 정수 : ", max2)

str(input())
