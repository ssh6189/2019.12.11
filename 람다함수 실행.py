f=lambda x,y:x+y
print(f(1,5))

함수의 인수로 기능을 넘겨주기 위해서 람다 함수가 사용된다.
출력할 값뿐만 아니라, 기능도 넘겨준다.

맵리듀스
맵리듀스는 파이썬 뿐만 아니라, 빅데이터를 처리하기 위한 기본 알고리즘으로도
많이 사용한다.

즉, Key, Value구조로 만드는것이다.

맵리듀스에는 map()함수와 reduce()함수가 있다.



#제너레이터
반복자와 같은 루프의 작용을 컨트롤하기 위해 사용되는 함수 또는 루틴
모든 제너레이터는 반복자이다.
제너레이터는 배열이나 리스트를 리턴하는 함수와 비슷하며, 호출을 할 수 있는 파라미터를
가지고 연속적인 값들을 만들어낸다.

한번에 모든 값을 포함한 배열을 만들어서 리턴하는 대신 yield구문을 이용해 한번
호출할 때마다 하나의 값만을 리턴한다.

반복자에 비해 작은 메모리 사용

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

nums1 = square_numbers([1, 2, 3, 4, 5])
print(nums1)

def square_numbers2(nums):
    result = []
    for i in nums:
        yield i*i

nums2 = square_numbers2([1, 2, 3, 4, 5])
print(nums2)

print(nums2)
print(next(nums2))
print(next(nums2))


제너레이터는 함수객체인데, 리스트나, 함수를 호출할때 딱 하나씩만 호출하는것


리스트 컴프리헨션을 잘 이용하는것이 좋다.


