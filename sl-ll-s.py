class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def slice(self, start, end):
        if not self.head:
            return None

        current = self.head
        result = LinkedList()
        index = 0
        while current and index < end:
            if index >= start:
                result.append(current.data)
            current = current.next
            index += 1

        return result

if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(1, 11):
        linked_list.append(i)

    print("Original Linked List:")
    linked_list.display()

    start = 2
    end = 7
    sliced_list = linked_list.slice(start, end)

    print(f"Sliced Linked List from index {start} to {end}:")
    sliced_list.display()
