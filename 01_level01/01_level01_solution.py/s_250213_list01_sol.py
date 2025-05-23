# 목적 : 리스트 숙련 + 자료구조 및 알고리즘 습득
# 리스트 자유자재로 다루기 예제

# 01
# -------------------------------------------------------------------------
# 난이도 = 입문자 , 알고리즘
# 아래는 클럽에 입장하려는 사람들의 나이를 순서대로 담은 리스트입니다.
# *19세 미만의 사람은 5명으로 고정적입니다.*
ages = [18, 20, 17, 15, 13, 12, 21, 24, 33]

# 이 중 19살 이하의 나이를 가진 사람을 입구컷 시키는 로직을 작성하세요.
def ipguCut(input):
    result = []
    # 여기에 구현
    for age in ages:
        if age > 19:
            result.append(age)
    return result
    
print(ipguCut(ages))

# 팁1. sort  +  리스트 슬라이싱 ex) list[0:3] 을 활용하여 푸는 알고리즘
# 팁2. for문, 그리고 if 문을 활용한 알고리즘
# -------------------------------------------------------------------------


# 02
# -------------------------------------------------------------------------
# 난이도 = 입문자 , 리스트 컴프리핸션
# 리스트 컴프리핸션을 활용해서 1~10까지 숫자를 담은 리스트를 작성하고 출력해보세요.
# 리스트 컴프리핸션이란 ? ex) a = [i for i in list] 이런 모양의 리스트입니다.

result = [i for i in range(1,11)]
print(result)

# -------------------------------------------------------------------------




# 03
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , 메모리 동작방식 , 깊은복사와 얕은복사

list1 = [1,2,3,4,5]
list2 = list1

print(id(list1))    # 주소값 : 1763517509376
print(id(list2))    # 주소값 : 1763517509376 동일

list2.clear()
print(list1)

# 여기서 list2.clear() 를 했음에도 불구하고 list1의 출력값이 []가 된 이유는 뭘까?
"""
list2는 list1의 주소값을 공유한다. (얕은 복사)가 일어난 상황이다.
여기서 list2 가 가르키고 있는 주소를 clear() 하는 순간, list1도 같은 주소를 가지고 있기 때문에
출력값이 날아간 것이다.
"""
# -------------------------------------------------------------------------






# 04
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , 리스트 가지고 놀기
# [1, 3, 5, 7, 9 .....] 와같이 정수 n 을 입력하면 1부터 n까지의 홀수만 반환하는 함수를 작성하세요.

def oddList(n):
    answer = [i for i in range(n) if i&1]
    return answer

print(oddList(5)) # 결과 : [1,3]
print(oddList(8)) # 결과 : [1,3,5,7]

# 팁1. 리스트 컴프리핸션 활용
# 팁2. for문과 if문 활용
# -------------------------------------------------------------------------







# 05
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , string과 배열의 유사한 점 ?!

# 반갑습니다 를 notice 변수를 활용하여 출력하시오.
notice = "다니습갑반"
result = ""
for i in range(len(notice) - 1, -1, -1): # i 는 문자열 notice 의 마지막 인덱스에서 0 까지 -1씩 감소한다는 뜻
    result += notice[i]
    pass

print(result)
# -------------------------------------------------------------------------






# 06 (어려움 주의)
# -------------------------------------------------------------------------
# 난이도 = 초~중급 , 버블 정렬을 활용하여 직접 커스텀 sort함수  만들어보기
six = [3,2,7,5,9]
def my_sort(lst = list):
    # 버블정렬 알고리즘
    # 리스트의 첫번째 요소와 두번째 요소를 비교하고, 첫번째 < 두번째 = False 라면 서로 교환
    # 두번째 요소와 세번째 요소를 비교하고 두번째 < 세번째 = False 라면 서로 교환
    # 다음은 세번째 와 네번째 ..... 에서 끝까지 비교 진행 하는 것이 1사이클
    # 이 사이클을 len(list) - 1 만큼 반복

    # 여기에 구현
    isSorted = False    # 정렬 완료 됬는지 알아보는 bool 변수

    for _ in range(len(lst)-1): # 리스트의 길이 -1 만큼 반복하겠다.
        count = 0               # 정렬 완료가 되었는지 알아보기위한 변수
        if count == len(lst)-1: isSorted = True # 비교가 len - 1 만큼 일어났는데 아무일도 없었다면 정렬완료된 상황이니까 True
        if isSorted: break      # 정렬완료됬으면 그만 돌려도 되잖아
        for j in range(len(lst)-1): # 1싸이클 당 리스트의 길이 -1 만큼 반복
            if lst[j] > lst[j+1]:   # 인덱스 0 부터 자기 뒤에 있는 녀석과 크기 비교, 만약 위에있는게 더 작다면
                lst[j], lst[j+1] = lst[j+1], lst[j]     # 자리교체
            else: count += 1    # 교환이 일어나지 않은 횟수 체크
    return lst

print(my_sort(six))

# 뭔 소리인지도 모르겠고, 감도 안잡힌다면, 풀지말자.
# -------------------------------------------------------------------------
