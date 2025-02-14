# 정규표현식 re 활용 문제

# 정규표현식을 알아보기엔 너무많고, 맛만 봐보자.
import re

p = re.compile('\d')    # \d = decimal , 숫자를 탐색하는 정규식
print(p.match('asdf'))  # 결과값 : None
print(p.match('0099'))  # 결과값 : match='0' , 매치된 결과의 시작이 0번인덱스에 존재한다.

pp = re.compile('\w')   # \w = 공백(화이트스페이스)을 제외한 모든 것을 탐색하는 정규식
print(pp.match('asdf')) # 결과값 : match = '0'
print(pp.match('0099')) # 결과값 : match = '0'

# match(text) 메서드 : text의 인덱스 0 번 부터 정규식을 만족하는지 알아보는 메서드

# 01

# 다음 전화번호를 입력받은 a, b, c 변수가 있다.
a = '010-777-7777'
b = '번호 010-777-7777'
c = '010-4875-7766'

# 이 프로그램의 규칙은 010 으로 시작하는 번호가 담겨야한다.
# 위 입력 값중 잘못된 규칙으로 들어온 입력을 match 를 활용해서 찾아주세요.

inputs = [a,b,c]
rule = re.compile() # 매개변수는 뭘 넣어야할까
result = []

for i in inputs:
    if rule.match(i):   # match의 결과값이 있을 때만 동작
        pass            # 로직 구현

print(result)
    