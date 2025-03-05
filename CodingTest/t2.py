from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)  # 귤 개수 카운트 (O(n))
    
    # 내림차순 정렬 대신, 가장 많이 나오는 귤부터 선택
    freq_list = count.most_common()  # O(n) (Counter가 최적화된 정렬 제공)
    
    result = 0
    for _, freq in freq_list:
        k -= freq
        result += 1
        if k <= 0:  # 필요한 만큼 골랐으면 즉시 종료
            break
    
    return result


print(solution(4,[1,3,2,2,3,5]))
