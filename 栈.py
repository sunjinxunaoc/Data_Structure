class Stack(object):
    """栈 LIFO（last in first out）"""
    def __init__(self):
        self._list = []
    def push(self, item):
        #添加元素
        self._list.append(item)
    def pop(self):
        #删除元素
        self._list.pop()
    def peek(self):
        #返回栈顶元素
        if self._list != []:
            return self._list[-1]
        else:
            return None
    def is_empty(self):
        #判断栈是否为空
        return self._list == []
    def size(self):
        #返回栈的长度
        return len(self._list)

if __name__ == '__main__':
    stack = Stack()
    stack.push("hello")
    stack.push("world")
    stack.push("itcast")
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())    
    print(stack.pop())
    print(stack.pop())