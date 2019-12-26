#enumerate()

#for i, v in enumerate(['tic', 'tac', 'toe']):

#zip() 함수는 1개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수이다.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print(a, b)
