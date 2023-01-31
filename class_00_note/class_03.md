# class 3
solved.ac class 3 Essentials

## 다이나믹 프로그래밍
### 1003.py
피보나치 수열을 재귀함수로 구현하면 아래와 같이 된다.
```py
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```
그런데, 문제에서 이렇게 재귀를 사용하면 시간초과가 난다. 위와 같은 재귀함수는 n이 커지면 연산 수행시간이 기하급수적으로 늘어난다. 질문게시판을 보니 다이나믹 프로그래밍을 사용해야 하는 문제라고 한다. \
다이나믹 프로그래밍은 `메모리 공간을 약간 더 사용`하여 연산속도를 비약적으로 증가시키는 방법이다. 한 번 수행한 연산의 결과를 메모리에 저장해 놓고 똑같은 연산의 결과가 필요하면 저장된 값을 다시 가져다 쓰는 개념이다. 메모리를 투자해서 연산속도를 증가시키는 방법인데, 이를 `메모제이션(캐싱) 기법`이라고도 한다.  \
1003.py 를 확인해보면, 0과 1을 카운팅하는 메모리 변수를 따로 만들어서 문제에서 요구하는 연산도 수행하도록 코드를 짜놨다. 기본적인 다이나믹 프로그래밍을 확인하기 위해서는 아래 피보나치 함수를 확인하면 된다.
```py
d = [0]*50
d[1] = 1

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    if d[n] != 0:
        return d[n]
    
    d[n] = fibonacci(n-1)+fibonacci(n-2)
    return d[n]
```
### 1463.py
이후 1463번 문제에서 BFS 트리를 만들 때도, 다음 트리를 계산하는 연산에서 동적 메모라이제이션을 사용하지 않아 시간초과가 났다. 동일한 연산을 반복하는 경우는 꼭 활용하도록 하자!

### 1697.py
이 문제도 BFS문제였는데, 다음에 움직일 수 있는 위치를 계산하여 트리를 만드는 과정에서 `메모리 초과`가 나왔다. 이는 다음 위치 계산시 `앞, 뒤, 앞, 뒤, ...` 이렇게 반복적인 루프를 형성해서 트릴를 만들어서 그런 것이었다. 이 경우도 동적 메모라이제이션으로 거쳐갔던 곳에 다시 오는 경우는 노드를 만들지 않고 넘어가서 해결되었다. 

## 0으로 채워진 2차원 배열 
numpy를 이용하면 간단하게 0으로 채워진 2차원 배열을 만들 수 있다.
```py
import numpy as np

a = np.zeros((3,4))
```
그런데, 백준에서는 외부 라이브러리는 사용 못한다고 한다. numpy는 외부 라이브러리이므로 못써서, 다른 방법으로 0으로 채워진 list를 얻는 법을 알아봤다. 
### 0으로 채워진 1차원 배열 만들기
```py
list = [0 for i in range(10)]
# [0,0,0,0,0,0,0,0,0,0]
```
### 0으로 채워진 2차원 배열 만들기
변수 w는 width를, h는 height를 의미한다.
```py
double = [[0 for w in range(3)] for h in range(5)]
'''
[[0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0], 
 [0, 0, 0]]
'''
```

## BFS, DFS
1012번을 풀면서 BFS를 사용하였다. BFS와 DFS는 앞으로도 계속 출제될 유형이니, 정리해보려고 한다. 참고 포스팅은 [여기](https://devuna.tistory.com/32)
* BFS : Breathe First Search, 너비 우선 탐색
* DFS : Depth First search, 깊이 우선 탐색
1012 문제를 풀 때는 인접한 점들을 차례로 돌면서 이어진 점들을 deque에 넣는 방식으로 문제를 풀었다. 사실 BFS와 DFS는 그래프 서칭 기법이기 때문에, 이 문제에서 어느 것을 썼는지는 좀 애매했다. BFS인 이유는 한 점으로부터 인접한 점(즉, 트리형 그래프에서는 인접 노드)을 하나씩 살펴보고, 그 다음에 그 점으로부터 인접한 점들을 다시한번 확인하는 알고리즘이기 때문이다. 
### 특징
DFS
* 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색
* 스택 또는 재귀함수로 구현
BFS
* 현재 정점에 연결된 가까운 점들부터 탐색
* 큐를 이용하여 구현
### 시간복잡도
모든 노드를 방문하는 것은 동일하기 떄문에 시간복잡도는 서로 같다.

## reversed dictionary
1620문제에서 dictionary의 key와 value를 쌍방으로 찾을 수 있도록 하는 문제가 있었다. 나는 그냥 두개의 딕셔너리를 만들어서 해결했다. 그런데, 다른사람이 푼 방법중에 key와 value를 뒤집는 코드를 사용한 사람이 있었다. 물론 이 방법은 모든 원소를 차례로 바꿔줘야해서 시간복잡도 O(n)의 작업이 되며, 결과적으로 시간초과가 났다고 한다. 하지만, `reversed dictionary`를 만드는 방법은 유용할 것 같으니 적어놓는다.
```py
dic = {}
dic[1]="Hi"
dic[2]="I'm"
dic[3]="Choonghyun"
print(dic) 
# {1: 'Hi', 2: "I'm", 3: 'Choonghyun'}

reversed_dic = dict(map(reversed,dic.items()))
print(reversed_dic)
# {'Hi': 1, "I'm": 2, 'Choonghyun': 3}
```

## list 사전순 정렬 반대로 하기
문제에서 다룬 부분은 아니지만, 질문게시판에서 본 스킬이라 적어본다. 만약 `list를 사전순 정렬`하는 경우는 아래처럼 하면 된다. sorted를 사용하면 원래 리스트는 그대로이고 결과만 리턴해준다.
```py
lst = ["abc","cde","bcd"]
lst_sorted = sorted(lst) # ["abc","bcd","cde"]
lst.sort() # ["abc","bcd","cde"]
```
list를 사전순 역정렬
```py
lst_sorted = sorted(lst,reverse=True) # ["cde","bcd","abc"]
```

## 최소 힙
참고한 포스팅은 [여기](https://reakwon.tistory.com/42). 문제 번호는 1927번. \ 
자료구조 중에는 `최소 힙`, `최대 힙`이 있다. 이들 `힙`은 어떠한 배열에서 최솟값과 최댓값을 꺼내기 쉬운 구조이다.  \
아래와 같은 list가 있다고 해보자.
```py
lst = [1,3,5,7,4,2]
``` 
일반적인 list에서 최솟값을 찾는 알고리즘은 O(n)의 시간복잡도를 갖는다. 아마 `sort()`, `min()`, `for 루프` 등을 사용해 구할 수 있을 것이다. \ 
힙에서는 시간복잡도를 O(log n)으로 해결해준다. \
힙은 `완전 이진트리 구조`인데, 이는 각 노드의 자식이 2개(1개이거나 없을 수는 있다.)만 가능하고, leaf의 가장 왼쪽부터 채우는 구조의 트리이다.
### 최소 힙
최소힙에서는 루트가 가장 작은 값이 되어야 한다. 그 다음은 자식이 자신의 크기보다 크기만 하면 된다. 이때 왼쪽, 오른쪽은 따질 것 없이 순차적으로 넣어지기만 하면 된다. \
<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99CEB1495C0238A107">
</p>
이러한 완전 이진트리 구조는 배열로도 구현할 수 있다. 즉, 최소힙은 배열을 통해 구현된다. 이때 자식 노드가 저장될 위치를 배열에 저장할 때 규칙이 존재한다.
```
왼쪽 자식은 자신의 인덱스 *2
오른쪽 자식은 자신의 인덱스 *2+1
```
<p align="center">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9987FB3D5C0260C92F">
</p>

반대로 부모는 `자신의 인덱스 / 2` 로 알아볼 수 있다. \ 
다시 한번 정리하면,
```
leftChild = parent*2
rightChild = parent*2+1
parent = child/2
```
### 최소힙에 작은 값 넣기
위에서는 최소힙에 순서대로 큰 값이 들어오는 경우만 다뤘는데, 만약 중간정도의 값이나 가장 최솟값이 들어오는 경우는 `빈 노드를 만들어서 그 아래 노드를 밀어준 후, 만든 빈다리에 값을 넣어주기`의 과정으로 정렬된다. \
위에 언급한 포스팅은 C로 heap을 구현하는 내용인데, 그걸 다 알 필요는 없는 것 같아서, heap이 위 규칙으로 동작한다는 것만 알아두자. 

## 최소힙, 최대힙 in python
참고 링크는 [여기](https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99)입니다.
### 최소힙
```py
import heapq

heap = []

# 아래 for문을 실행하고 나면 heap은 [1,2,3,5,4]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, i)

# 작은 숫자 순서대로 1,2,3,4,5가 출력된다.
for i in range(5):
	print(heapq.heappop(heap))
```
### 최대힙
python에서는 따로 최대 힙을 지원하지는 않는다. 대신 push 및 pop 할 때, 부호 `-`를 붙여줘서 사용하면된다.
```py
import heapq

heap = []
values = [1,5,3,2,4]

# 아래 for문을 실행시키고 나면 heap은 [-5,-4,-3,-1,-2]가 된다.
for value in values:
	heapq.heappush(heap, -value)

# 아래 for문을 실행시키면 5,4,3,2,1이 출력된다. 즉, 큰 숫자부터 출력이 된다.
for i in range(5):
	print(-heapq.heappop(heap))
```

 