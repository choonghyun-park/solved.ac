# class 2
solved.ac class 2 essentials

## 시간초과
1920번 풀 때, input을 `sys.stdin.readline()` 으로 받았는데도 시간초과가 나왔다. 정답을 저장해 놓은 변수가 list로 돼있어서 그런 것이었다. 앞에 백준 단계별 문제에서도 본 적있는 케이스인데, `list`를 `set` 으로 변경시켜서 해결하였다.  

## 단어 사전순 정렬
`lst.sort()`를 하면 list 내의 숫자가 ascending order로 바뀌는 것은 알고 있을 것이다. 신기하게도, 영단어들이 들어있는 lst도 같은 함수로 사전순 정렬을 할 수 있다.
```py
lst = ["bc","ab","cd"]
lst.sort()
print(lst) # ["ab","bc","cd"]
```
만약 lst 원본은 그대로 두고, 결과값만 얻고싶으면 `lst.sorted()`를 사용하면 된다.
```py
lst = ["bc","ab","cd"]
sorted_lst = lst.sorted()
print(lst)        # ["bc","ab","cd"]
print(sorted_lst) # ["ab","bc","cd"]
```

## 소수 판별 함수
다소 수학적인 유형의 문제를 풀다보면 소수인지 판별하는 함수가 필요하다. 필요한 경우 아래 함수를 사용하면 된다. 내가 직접 구현한 것이다. 참고로 1은 소수도 합성수도 아니다.
```py
def isDecimal(n):
    # 1 is not Decimal
    if n==1:return False

    # check wether n is divided by smaller number than n
    for i in range(2,n):
        if n%i==0:return False
    return True
``` 

## deque
queue, stack은 자료구조의 기초적인 개념이다. 
* queue : FIFO (First In First Out)
* stack : LIFO (Last In First Out)
쉽게 설명하면 queue는 사람들이 줄서서 가게에 들어가는 것에 비유할 수 있고, stack은 컵 안에 도넛을 하나씩 넣었을 때 다시 뺄 때는 가장 마지막에 넣은 것부터 빼는 것에 비유할 수 있다.\
deque(덱, 데큐)는 큐이기는 하지만 양방향인 queue이다. 즉, 요소를 양쪽 방향에서 추가 및 제거할 수 있다.

### 기본 매서드
참고한 포스팅은 [여기](https://codingpractices.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%99%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8C%80%EC%8B%A0-%ED%81%90-%EB%8D%B0%ED%81%AC-deque-%EB%A5%BC-%EC%93%B8%EA%B9%8C).
* 정의
```py
from collections import deque

q = deque() # empty deque

# q = deque([list])
# q = deque([1,2,3])
``` 
 
* 오른쪽 끝에 삽입
```py
q.append(3)
``` 
 
* 왼쪽 끝에 삽입
```py
q.appendleft(2)
``` 
 
* 가장 오른쪽의 요소 반환 및 삭제
```py
q.pop()
``` 
* 가장 왼쪽의 요소 반환 및 삭제
```py
q.popleft()
```

* 주어진 array 배열을 순환하며 q의 오른쪽에 추가
순환한다는 말은 array의 첫번째 원소부터 차례대로 적용한다는 말이다.
```py
q = deque([1,2,3])
arr = [10,11,12]
q.extend(arr)
print(q) # deque([1,2,3,10,11,12])
``` 
* 주어진 array 배열을 순환하며 q의 왼쪽에 추가
앞의 원소부터 차례로 q의 왼쪽에 추가된다고 보면 된다.
```py
q = deque([1,2,3])
arr = [-2,-1,0]
q.extendleft(arr)
print(q) # deque([0,-1,-2,1,2,3])
``` 
* 해당 item을 q에서 찾아 삭제
```py
q.remove(3)
``` 
* 해당 숫자만큼 회전 (양수:시계방향 / 음수:반시계방향)
```py
q.rotate(1)     #시계방향
q.rotate(-1)    #반시계방향
```

## 최대공약수, 최소공배수
```py
# 최대공약수 (GCF : Greatest Common Factor)
def GCF(a,b):
    smaller = min([a,b])
    for i in range(smaller):
        gcf = smaller-i
        if a%gcf==0 and b%gcf==0:
            return gcf

# 최소공배수 (LCM : Least Common Multiple)
def LCM(a,b):
    gcf = GCF(a,b)
    lcm = gcf * int(a/gcf) * int(b/gcf)
    return lcm
```
## 순열과 조합
참고한 포스팅은 [여기](https://velog.io/@dramatic/Python-permutation-combination-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9).
### 순열 (Permutation)
서로 다른 n개 중 r개를 골라 순서를 정해 나열하는 가짓수
```py
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```
### 조합 (Combination)
```py
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
문제에서는 range(N) 으로부터 인덱스의 조합을 얻기 위해서 사용했다. 
```py
arr = list(range(N))
_5C3 = itertools.combinations(arr,3)
lst_5C3 = list(_5C3)
```
