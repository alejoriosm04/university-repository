class node:
    def __init__(self, val : int):
        self.val = val
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
    def getData(self):
        data=""
        current=self.head
        while current.next:
            data+=" "+str(current.val)
            current=current.next
        #current.next=newNode
        return data
    def madd(self,*data):
        for i in data:
            newNode=node(i)
            if self.head:
                current=self.head
                while current.next:
                    current=current.next
                current.next=newNode
            else:
                self.head=newNode


def test():
    ll=linkedList()
    ll.madd(1,2,3,6,5,7,8)
    print(ll.getData())


test()