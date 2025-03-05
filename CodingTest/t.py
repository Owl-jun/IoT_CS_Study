from math import factorial

def solution(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지 숫자 리스트
    result = []
    k -= 1  # 인덱스는 0부터 시작하므로 k를 1 감소
    
    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # (i-1)! 계산
        index = k // fact  # 현재 위치에서 몇 번째 그룹인지 계산
        result.append(numbers.pop(index))  # 해당 숫자를 결과에 추가하고 리스트에서 제거
        k %= fact  # 남은 순서 조정
    
    return result


solution(3,5)