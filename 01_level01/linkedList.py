
### 연결 리스트

# 배열 : 메모리가 연속적이며, 추가 및 수정에 오버헤드(컴퓨터가 힘들어해요)가 발생한다.
# 연결 리스트 : 메모리 주소는 상관 없이, 서로가 서로를 가르켜 연결하는 방식, 수정 및 추가, 삭제 등이 매우 간단하고 편리하다.



# 챌린지 1.

# 아래는 제가 구현한 연결리스트 클래스 입니다.
# 한줄 한줄 주석을 달아서 이게 뭔지, 어떤 동작인지 설명해보세요.

class LinkedList:                           # ex: 이 클래스의 이름은 LinkedList 이다.
    def __init__(self):                     # 
        self.head = None                    #
        self.nodes = []                     #
        self.count = 0                      #

    class Node:                             # 새로운 개념 : 이너클래스 (클래스 안의 클래스, 클래스와 개념은 같다.)
        def __init__(self, data):           #
            self.data = data                #
            self.link = None                #

        def __str__(self):                  #
            return f"{self.data}"           #

    def append(self, data):                 #       
        new_node = self.Node(data)          #
        if not self.head:                   #
            self.head = new_node            #
        else:                               #
            self.nodes[-1].link = new_node  #
        self.nodes.append(new_node)         #
        self.count += 1                     #

    def print_list(self):                   #
        current = self.head                 #
        while current:                      #
            print(current, end=" -> ")      #
            current = current.link          #
        print("None")                       #

list1 = LinkedList()
list1.append('김씨')
list1.append('왕씨')
list1.append('철씨')

list2 = LinkedList()
list2.append('굼씨')
list2.append('진씨')

list1.print_list()
list2.print_list()