
class my_stack():

    def __init__(self,size):
        self.top = -1
        self.stack = []
        self.size = size

    def __str__(self):
        return f'현재 스텍 데이터 : {self.stack} , 남은 용량 : {self.top+1}/{self.size}'

    def push(self,data):
        if self.top < self.size-1:
            self.stack.append(data)
            self.top += 1
        else:
            print('스택이 꽉찼습니다.')
            pass

    def pop(self):
        if self.top != -1:
            result = self.stack[self.top]
            self.top -= 1
            self.stack = self.stack[:self.top+1]
        else:
            print('스택이 비었습니다.')
            return None
        return result

stack = my_stack(5)

stack.push('사과')
stack.push('포도')
stack.push('바나나')
stack.push('오렌지')

print(stack)
print(stack.pop())
print(stack)

stack.push('오렌지')
stack.push('샤인머스켓')
print(stack)
stack.push('까악')
print(stack)
