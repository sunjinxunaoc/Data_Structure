class Node(object):
    "定义节点"
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleCycleLinklist(object):
#同单链表类似 但是循环链表为节点的next指向head
#所以循环判断时， cur！= None 改为了cur.next != self.head
    def __init__(self, node = None):
        self.head = node
        if node:
            node.next = node
    def is_empty(self):
        return self.head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return None
        cur = self.head
        while cur.next != self.head:
            print(cur.elem)
            cur = cur.next
        print(cur.elem)
    
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            self.head = node
            cur.next = self.head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            pre = self.head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.head
        pre = None
        while cur.next != self.head:
            if cur.elem == item:
                if cur == self.head:
                    rear = cur.next
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = cur.next
                    rear.next = self.head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            if cur == self.head:
                self.head = None
            else:
                pre.next = cur.next
    def search(self, item):
        if self.is_empty():
            return False

        cur = self.head
        while cur.next != self.head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    ll = SingleCycleLinklist()
    print(ll.is_empty())
    print(ll.length())
    ll.append(0)
    print(ll.is_empty())
    print(ll.length())
    ll.append(3)
    ll.add(2)
    ll.insert(1,9)
    ll.remove(9)
    ll.travel()
    print(ll.search(9))  
