class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        return self.head

    def print_func(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llistr = " "
        while itr:
            llistr += str(itr.data) + "------>"

            itr = itr.next

        print(llistr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_values(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_values(["banana", "grapes", "Mango", "apple"])
    # print("length:", l1.get_length())
    # l1.insert_at_beginning(3)
    # l1.insert_at_beginning(4)
    # l1.insert_at_beginning(5)
    # l1.insert_at_beginning(6)
    # l1.insert_at_end(890)
    l1.print_func()
    # l1.insert_at(3, "jackfruit")
    # l1.print_func()
    # l1.insert_after_values("banana" , "appy")
    l1.remove_by_value("apple")
    l1.print_func()
    # l1.remove_at(2)
    # l1.print_func()
    # l1.remove_at(2)
    # l1.print_func()
    print("length:", l1.get_length())
