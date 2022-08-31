class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=[]
        num2=[]
        current1=l1
        current2=l2
        while current1 is not None:
            num1.append(current1.val)
            current1=current1.next
        while current2 is not None:
            num2.append(current2.val)
            current2=current2.next
        sumr=[]
        sign=0
        c=max(len(num1),len(num2))
        while len(num1)!=c:
            num1.append(0)
        while len(num2)!=c:
            num2.append(0)
        for i in range(c):
            if(sign==0):
                sumr.append(num1[i]+num2[i])
            if(sign==1):
                sumr.append(num1[i]+num2[i]+1)
            if(sumr[i]>=10):
                sumr[i]-=10
                sign=1
            else:
                sign=0
        if(sign==1):
            sumr.append(1)
        c=len(sumr)
        head=ListNode()
        #创建列表的时候初始是一个只有0为head的列表，如果最后返回的列表是head的话包含0这个元素，如返回head.next的话是从head后面那一项开始返回————列表————，因为指向的位置是固定的
        cur=head
        for i in range(c):
            cur.next=ListNode(sumr[i])
            cur=cur.next #为了保证从开始向前读取，所以分离了head和cur，cur用于挨个存储每个节点的数据，然后head得以从头读取不同节点的数字
        return head.next

    #参考 https://www.jianshu.com/p/5875efe4748d
    #使用链表