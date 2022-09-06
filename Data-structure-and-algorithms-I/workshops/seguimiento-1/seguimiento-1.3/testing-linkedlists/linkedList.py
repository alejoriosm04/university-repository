class node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    def add(self,data):
        newNode=node(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode

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
    def getData(self):
        data=""
        current=self.head
        while current.next:
            data+=" "+str(current.val)
            current=current.next
        #current.next=newNode
        return data

    def search(self, itemsearch):
        current=self.head
        while current != None:
            if current.val == itemsearch:
                return current 
             
            current = current.next
         
        return False

 
 
def recSearch(node,itemsearch):
    current=node
    if not current:
        return -1#not found
    else:
        if current.val==itemsearch:
            return current
        else:
            return recSearch(current.next,itemsearch)

def recPos(node,itemsearch,pos):
    current=node
    if not current:
        return -1#not found
    else:
        if current.val==itemsearch:
            return pos
        else:
            return recPos(current.next,itemsearch,pos+1)

def recInsert(node,item,pos,posobj):
    current=node
    if not current:
        return -1#not found
    else:
        if pos-1==posobj:
            #return pos
            tmp=node(item)
            tmp.next=current
        else:
            #return 
            recInsert(current.next,item,pos+1,posobj)
def borrar(head,posobj,pos):
    current=head
    if not current:
        return -1#not found
    else:
        if pos-1==posobj:
            tmp=current.next
            current.next=current.next.next
            return head  
        else:
            return borrarAux(current.next,posobj,pos+1)

def maxNum(node,maxnum):
    current=node
    if not current:
        return -1#not found
    else:
        if maxnum<current.val:
            return maxNum(current.next,itemsearch,current.val)
        else:
            return maxNum(current.next,itemsearch,maxnum)

def test():
    ll=linkedList()
    ll.madd(1,2,3,6,5,7,8)
    # #print(ll.search(4).val)
    # #tmp=recSearch(ll.head,4)
    # #print(tmp.val)
    # print(recPos(ll.head,4,0))
    # print(recInsert(ll.head,4,3,0))
    # print(recInsert(ll.head,4,7,0))
    # print(recInsert(ll.head,4,8,0))
    # print()
    print(ll.getData())


test()