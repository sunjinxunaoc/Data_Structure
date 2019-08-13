def bubble_sort(alist):
    """"""
    for j in range(len(alist)-1,0,-1):
    #从末尾循环到倒数第二位
        for i in range(j):
        #相邻两位比较 前者大于后者则交换位置
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1]>alist[i+1], alist[i]
def selection_sort(alist):
    n = len(list)
    for i in range(n-1):
    #从首位到最后一位 找到序列最小值放到相应位置
        min_index = i
        for j in range(i+1, n):
        #记录最小值的index
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
        #如果最小值的索引不为i 则交换位置
            alist[i], alist[min_index] = alist[min_index], alist[i]

def insert_sort(alist):
    for i in range(1, len(alist)):
    #从第二个位置开始插入
        for j in range(i, 0,-1):
        #从第i个元素开始比较， 如果小于前一个元素 交换位置
            if alist[j]<alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

def partition(alist,start,end):
    #选取最后一个元素为基准
    pivot = alist[end]
    #i是慢指针
    i = start-1
    #j是快指针
    for j in range(start,end):
        if alist[j] < pivot:
            i+=1
            alist[i],alist[j] = alist[j],alist[i]
    #基准元素插入到相应的位置
    alist[i+1],alist[end] = alist[end],alist[i+1]
    return i+1

def quick_sort(alist,start,end):
    if start<end:
        pivot_index = partition(alist,start,end)
        #分治
        quick_sort(alist,start,pivot_index-1)
        quick_sort(alist,pivot_index+1,end)


def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    # 二分分解
    num = len(alist)/2
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left,right)
def merge(left, right):
    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    #left与right的下标指针
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

