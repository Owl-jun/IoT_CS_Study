
### 연결 리스트

# 배열 : 메모리가 연속적이며, 추가 및 수정에 오버헤드(컴퓨터가 힘들어해요)가 발생한다.
# 연결 리스트 : 메모리 주소는 상관 없이, 서로가 서로를 가르켜 연결하는 방식, 수정 및 추가, 삭제 등이 매우 간단하고 편리하다.



# 챌린지 1.

# 아래는 제가 구현한 연결리스트 클래스 입니다.
# 한줄 한줄 주석을 달아서 이게 뭔지, 어떤 동작인지 설명해보세요.

class LinkedList:
    def __init__(self):
        self.head = None  
        self.nodes = []     

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None  

        def __str__(self):
            return f"{self.data}"

    def push_back(self, data):
        new_node = self.Node(data)  
        if not self.head:
            self.head = new_node  
            prevNode = None
        else:
            self.nodes[-1].next = new_node  
            prevNode = self.nodes[-1]
        self.nodes.append(new_node)  
        self.nodes[-1].prev = prevNode
    
    def insert(self,find_data,insert_data):
        new_node = self.Node(insert_data)
        isFind = False
        for node in self.nodes:
            if node.data == find_data:
                curNode = node
                isFind = True
                break
        if isFind == False: return    

        if curNode.prev != None:
            new_node.prev = curNode.prev
            curNode.prev.next = new_node
            curNode.prev = new_node
            new_node.next = curNode
        else : 
            self.head = new_node
            new_node.prev = None
            new_node.next = curNode
            curNode.prev = new_node

    def delete(self,del_data):
        for node in self.nodes:
            if node.data == del_data:
                delData = node
                break
        if self.head == delData:
            self.head = delData.next
        elif delData.next == None:
            delData.prev.next = None
        else:
            delData.prev.next = delData.next
            delData.next.prev = delData.prev
        del(delData)

    def find(self,find_data):
        findNode = None
        for node in self.nodes:
            if node.data == find_data:
                findNode = node
                break
        return findNode 
        
    def print_list(self):
        current = self.head
        while current:
            print(current, end=" -> ")
            current = current.next
        print("None")

list1 = LinkedList()
list1.push_back('김씨')
list1.push_back('왕씨')
list1.push_back('철씨')
list1.print_list()
list1.insert('왕씨','옹씨')
list1.print_list()

list2 = LinkedList()
list2.push_back('굼씨')
list2.push_back('진씨')
list2.print_list()
list2.insert('굼씨','주씨')
list2.print_list()
