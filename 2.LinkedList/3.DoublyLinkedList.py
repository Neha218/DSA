# Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction. Your node class will look this this,
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
# Add following new methods,

# def print_forward(self):
#     # This method prints list in forward direction. Use node.next

# def print_backward(self):
#     # Print linked list in reverse direction. Use node.prev for this.
# Implement all other methods in regular linked list class and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        if self.head != None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None, itr)
        itr.next = node
    
    def print_forward(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        listr = ''
        while itr:
            listr += '-->'+str(itr.data) if listr != '' else str(itr.data)
            itr = itr.next
        print(listr)

    def print_backward(self):
        if self.head is None:
            print("Linkedlist is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        listr = ''
        while itr:
            listr += '-->'+str(itr.data) if listr != '' else str(itr.data)
            itr = itr.prev
        print(listr)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next, itr)
                itr.next = node
                if node.next:
                    node.next.prev = node
                break
            itr = itr.next
            count += 1
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        index = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(index+1, data_to_insert)
                break
            itr = itr.next
            index += 1
        if index == self.get_length():
            print("No such value present in the linkedlist")

    def remove_by_value(self, data):
        itr = self.head
        index = 0
        while itr:
            if itr.data == data:
                self.remove_at(index)
                break
            itr = itr.next
            index += 1
        if index == self.get_length():
            print("No such value present in the linkedlist")

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_values(["banana","mango","grapes","orange"])
    print("\nForward print")
    dll.print_forward()
    print("\nBackward print")
    dll.print_backward()
    
    dll.insert_after_value("mango", "apple")
    print("\nInserted apple after mango")
    dll.print_forward()
    print("\nBackward print")
    dll.print_backward()

    dll.insert_at_begining("begin")
    print("\nInserted at begining")
    dll.print_forward()

    dll.insert_at_end("end")
    print("\nInserted at end")
    dll.print_forward()

    dll.remove_at(2)
    print("\nRemoved value at index 2")
    dll.print_forward()
    print("\nPrinted backward: ")
    dll.print_backward()

    dll.insert_at(2, "two")
    print("\nInserted at index 2")
    dll.print_forward()

    dll.remove_by_value("banana")
    print("\nRemoved banana")
    dll.print_forward()

    print("\nPrinted backward: ")
    dll.print_backward()