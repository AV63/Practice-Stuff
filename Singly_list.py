class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.start
        self.start = newNode

    def insert_after(self, pos, data):
        temp = self.start
        newNode = Node(data)
        for i in range(pos - 1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def append(self, data):
        newNode = Node(data)
        if self.start is None:
            self.start = newNode
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def display(self):
        if self.start is None:
            print('The list is empty')
        temp = self.start
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next

    def deleteNode(self, pos):
        temp = self.start
        for i in range(pos - 1):
            temp = temp.next
        temp.next = temp.next.next

    def key_deletion(self, key):
        temp = self.start
        self.pos = 0
        if temp.data == key:
            self.start = self.start.next
            del self.start
        while temp.data != key:
            self.pos += 1
            temp = temp.next
        cur = self.start
        for i in range(self.pos - 1):
            cur = cur.next
        cur.next = cur.next.next
        del cur.next

    def count_nodes(self):
        self.count = 0
        temp = self.start
        while temp.next:
            self.count += 1
            temp = temp.next
        print('The number of nodes is the list is ', self.count + 1)

    def delete_list(self):
        self.start = None

t = LinkedList()

while True:
    print('1.Push\n2.Insert\n3.Delete\n4.Node count\n5.Delete list\n6.Display list')
    choice = int(input('Enter your choice '))
    if choice == 1:
        data = input('Enter the data you wish to insert!')
        t.push(data)
        print('\nThe list is ')
        t.display()
    elif choice == 2:
        data = input('Enter the data you wish to insert ')
        c = input('a.Append\nb.Insert after a position')
        if c == 'a':
            t.append(data)
            print('\nThe list is ')
            t.display()
        elif c == 'b':
            pos = int(input('Enter the position where you wish to insert your data. '))
            t.insert_after(pos, data)
            print('\nThe list is ')
            t.display()
    elif choice == 3:
        c = input('a.Delete using key\nb.Delete using position')
        if c == 'a':
            data = input('Enter the data you wish to delete ')
            t.key_deletion(data)
            print('\nThe list is ')
            t.display()
        elif c == 'b':
            pos = int(input('Enter the position'))
            t.deleteNode(pos)
            print('\nThe list is ')
            t.display()
    elif choice == 4:
        t.count_nodes()
    elif choice == 5:
        t.delete_list()
        t.display()
    elif choice == 6:
        t.display()
    else:
        print('Wrong choice!')

    n = int(input('\nDo you wish to continue?(1/0)'))
    if n == 1:
        continue
    else:
        break

