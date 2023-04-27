from Node import Node

class LinkedList():

    def __init__(self):
        self.head = None

    def __iter__(self):            #Makes nodes iterable with external conditional loops
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.value)
        return ' -> '.join(nodes)    #when externally printing object it returns user friendly message
                                     #rather than info on object

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = node

    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:      #for loop enabled by __iter__
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print('Empty list')

    def insert_prior(self, target, value):
            new_node = Node(value)
            if self.head:
                # we have the __iter__ dunder method that lets us loop through all our nodes.
                if self.head.value == target:
                    right_node = self.head
                    self.head = new_node
                    new_node.right = right_node
                for node in self:
                    if node.right.value == target:
                        right_node = node.right
                        node.right = new_node
                        new_node.right = right_node
                        return
            else:
                print("empty list")

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right:
                    if node.right.value == value:
                        node.right = node.right.right
                        return
                    
    def get_tail(self):
        for node in self:
            pass
        return node.value

    def remove_tail(self):
        node = self.head
        while node.right.right:
            node = node.right
        node.right = None

    def add_list_elements(self, alist):
        for element in alist:
            linked_list.add_node(element)





linked_list = LinkedList()

linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Tuesday')
linked_list.add_node('Thursday')
print(linked_list)
# print(linked_list.head.value)
# print(linked_list.head.right.value)
# print(linked_list.head.right.right.value)

# linked_list.insert_node('Tuesday', 'Wednesday')

# print(linked_list)

# linked_list.add_node('Spazday')
# print(linked_list)
# linked_list.remove_node('Sunday')
# linked_list.remove_node('Spazday')
# linked_list.remove_node('Wednesday')
# linked_list.insert_prior('Thursday', 'Wednesday')

new_list = ['Monday', 'Tuesday','Wednesday']

linked_list.add_list_elements(new_list)

print(linked_list)