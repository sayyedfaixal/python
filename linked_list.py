class Node:
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print('Linked List is Empty')
        
        temp = self.head
        print_ll =''
        while temp:
            print_ll += str(temp.data) + '-->'
            temp=temp.next
        print(print_ll)
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)

    def insert_in_middle(self, data, pos):
        temp = self.head
        while pos-1:
            temp = temp.next

        temp.next = Node(self, data)

    def leng(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp= temp.next
        print(f'Length of the linked list is {count}')
# 10->20->30->40            
        

if __name__ == '__main__':
            
    ll = Linkedlist()
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_begining(10)
    ll.printll()
    ll.leng()