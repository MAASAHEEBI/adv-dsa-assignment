'''Delete the elements in an linked list whose sum is equal to zero'''

#Building Nodes
class Node():
    def __init__(self,value):
        self.value=value
        self.nextnode=None
#Class Linked List for Pointing Head and Tail
class LinkedList():
    def __init__(self):
        self.head=None
    
    def insert(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        crnt_node=self.head
        while True:
            if crnt_node.nextnode is None:
                crnt_node.nextnode=node
                break
            crnt_node=crnt_node.nextnode

    def print_llist(self):
        crnt_node=self.head     
        v_llist=[]
        while True:
            print(crnt_node.value,end='->')
            v_llist.append(crnt_node.value) # storing data into list
            if crnt_node.nextnode is None:              
                break
            crnt_node=crnt_node.nextnode
        print('None')
        return v_llist
        
    def print_modified_llist(self):
        p_add=0
        v_llist=self.print_llist()
        #going till the second last element of list and then trying to print requested o/p
        for i in range(len(v_llist)-1):
            p_add=p_add+v_llist[i]
        if v_llist[-1]>0 and p_add>0:
            print(p_add,v_llist[-1])
        elif v_llist[-1]<0 and p_add>0:
            print(p_add+v_list[-1])
        elif v_llist[-1]<0 and p_add<0:
            print(v_llist[-1],p_add)
            

sll=LinkedList()
sll.insert(4)
sll.print_llist()
sll.insert(6)
sll.print_llist()
sll.insert(-10)
sll.print_llist()
sll.insert(8)
sll.print_llist()
sll.insert(9)
sll.print_llist()
sll.insert(10)
sll.print_llist()
sll.insert(-19)
sll.print_llist()
sll.insert(10)
sll.print_llist()
sll.insert(-18)
sll.print_llist()
sll.insert(20)
sll.print_llist()
sll.insert(25)
sll.print_llist()
sll.print_modified_llist()
