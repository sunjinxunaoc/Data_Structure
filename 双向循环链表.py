class Node(object):
    def __init__ (self,item):
    #双向循环链表的节点不接指向next还要prve
        self.elem = item
        self.next = None
        self.prev = None
class DoubleLinkList(object):
    def __init__(self, node = None):
        self.head = node

    def is_empty(self):
        return self.head == None

    def length(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.elem)
            cur = cur.next    
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length() - 1):
            self.append(item)
        else:
            cur = self.head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.head
        while cur != None:
            if cur.elem == item:
                if cur == self.head:
                    self.head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                break
            else:
                cur = cur.next
    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False   
    
if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.travel()
    ll.insert(3,100)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    print(ll.search(200))