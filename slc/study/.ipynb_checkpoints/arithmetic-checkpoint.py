

import numpy as np
def sort_function_check(func):
    for i in range(1000):
        datas = np.random.randint(1,10,(100)).tolist()
        answer = np.sort(datas).tolist()
        our_answer = func(datas)
        assert answer == our_answer
    return 'pass check'

# 冒泡排序

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst

%%time
sort_function_check(bubble_sort)

# 选择排序

def selection_sort(lst):
    for i in range(len(lst) - 1):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

%%time
sort_function_check(selection_sort)

# 快速排序

def quick_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    baseline = lst[0]
    left = [lst[i] for i in range(1, len(lst)) if lst[i] < baseline]
    right = [lst[i] for i in range(1, len(lst)) if lst[i] >= baseline]
    return quick_sort(left) + [baseline] + quick_sort(right)

%%time
sort_function_check(quick_sort)


# 归并排序

def merge_sort(lst):
    def merge(left,right):
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left,right)


%%time
sort_function_check(merge_sort)

# 堆排序

def heap_sort(lst):
    def adjust_heap(lst, i, size):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest_index = i
        if left_index < size and lst[left_index] > lst[largest_index]:
            largest_index = left_index
        if right_index < size and lst[right_index] > lst[largest_index]:
            largest_index = right_index
        if largest_index != i:
            lst[largest_index], lst[i] = lst[i], lst[largest_index]
            adjust_heap(lst, largest_index, size)

    def built_heap(lst, size):
        for i in range(len(lst )/ /2)[::-1]:
            adjust_heap(lst, i, size)

    size = len(lst)
    built_heap(lst, size)
    for i in range(len(lst))[::-1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)
    return lst


%%time
sort_function_check(heap_sort)

# 插入排序

def insertion_sort(lst):
    for i in range(len(lst) - 1):
        cur_num, pre_index = lst[i+1], i
        while pre_index >= 0 and cur_num < lst[pre_index]:
            lst[pre_index + 1] = lst[pre_index]
            pre_index -= 1
        lst[pre_index + 1] = cur_num
    return lst

%%time
sort_function_check(insertion_sort)

#希尔排序

def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j]
                else:
                    break
        gap //= 2
    return lst

%%time
sort_function_check(shell_sort)

# 计数排序

def counting_sort(lst):
    nums_min = min(lst)
    bucket = [0] * (max(lst) + 1 - nums_min)
    for num in lst:
        bucket[num - nums_min] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            lst[i] = j + nums_min
            bucket[j] -= 1
            i += 1
    return lst

%%time
sort_function_check(counting_sort)

#桶排序

def bucket_sort(lst, defaultBucketSize=4):
    maxVal, minVal = max(lst), min(lst)
    bucketSize = defaultBucketSize
    bucketCount = (maxVal - minVal) // bucketSize + 1
    buckets = [[] for i in range(bucketCount)]
    for num in lst:
        buckets[(num - minVal) // bucketSize].append(num)
    lst.clear()
    for bucket in buckets:
        bubble_sort(bucket)
        lst.extend(bucket)
    return lst


%%time
sort_function_check(bucket_sort)

# 基数排序


# LSD Radix Sort
def radix_sort(lst):
    mod = 10
    div = 1
    mostBit = len(str(max(lst)))
    buckets = [[] for row in range(mod)]
    while mostBit:
        for num in lst:
            buckets[num // div % mod].append(num)
        i = 0
        for bucket in buckets:
            while bucket:
                lst[i] = bucket.pop(0)
                i += 1
        div *= 10
        mostBit -= 1
    return lst

%%time
sort_function_check(bucket_sort)



# 栈
class Stack():
    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

#队列
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

#树
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    @classmethod
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    @classmethod
    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    @classmethod
    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    @classmethod
    def breadth_travel(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print
            node.elem,
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

#递归
class To_factorial:
    """
    递归
    1 定义一个阶乘函数f(x)
    2 明确等级关系 5的阶乘 = 5 * 4的阶乘
    3 明确出口 1的阶乘 = 1
    4 写出函数
    def 阶乘(x):
        if x ==1:
            return 1
        else:
            return x*阶乘(x-1)
    """

    def __init__(self):
        pass

## 单链表
class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表
    is_empty() 链表是否为空
    create() 创建
    length() 链表长度
    travel() 遍历链表
    add(item) 链表头部添加元素
    append(item) 链表尾部添加元素
    insert(pos, item) 指定位置添加元素
    remove(item) 删除节点
    find(item) 查找节点是否存在
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def create(self,data):
        self._head = SingleNode(0)
        cur = self._head
        for i in range(len(data)):
            node = SingleNode(data[i])
            cur.next = node
            cur = cur.next

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        while cur:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


