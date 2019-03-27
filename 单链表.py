class Node(object):
    "定义节点"
    def __init__(self,elem):
        self.elem = elem
        self.next = None
    #通过next指向下一个节点来连接成链表
class SingleLinklist(object):
    def __init__(self, node = None):
        self.head = node
    #初始化单链表 self.head指向输入的node 无输入时为None
    def is_empty(self):
        "判断链表是否为空"
        return self.head == None
    #判断链表的head是否为None
    def length(self):
        "返回链表的长度"
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    #从head开始遍历到队尾 以cur = None 为判据
    def travel(self):
        cur = self.head
        while cur != None:
            print(cur.elem, end = ' ')
            cur = cur.next
    #与返回长度类似 从头遍历输出
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
    #将先node的next赋为head，然后将node赋值为head 完成头部添加node
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    #链表为None时，直接将head赋值为node
    #cur循环到最后节点 然后将cur.next赋为node
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
    #pos如果小于0 则将在头部添加
    #pos如果大于链表的长度 则将在尾部添加
    #将pre定义为head 开始循环到pos的前一位 在这位置上将node.next = pre.next pre.next = node 完成插入
    def remove(self, item):
        cur = self.head
        pre = None
        #循环至尾部
        while cur != None:
            if cur.elem == item:
                #如果对应item在头部
                if cur == self.head:
                    self.head = cur.next
                #将删除节点的前一位的next赋值为cur的next   
                else:
                    pre.next = cur.next
                break
            #pre始终在cur的前一个节点
            else:
                pre = cur
                cur = cur.next
    def search(self, item):
        cur = self.head
        #从头结点循环到尾节点
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinklist()
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

