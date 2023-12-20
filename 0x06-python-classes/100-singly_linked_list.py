#!/usr/bin/python3
'''Python Interpreter.'''


class Node:
    '''Defines a node of a singly linked list.'''

    def __init__(self, data, next_node=None):
        '''Instantiating a linked list Node.
        Parameters:
            data: data stored in the node of the linked list
            next_node: pointer to the next node in the linked list.
        Raise:
            TypeError: if data not an integer
            TypeError: if next_node not None or a Node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Property to retrieve the value of 'data'.'''
        return (self.__data)

    @data.setter
    def data(self, value):
        '''Property setter to set the value of 'data'.'''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''Property to retrieve the value of the next Node.'''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        '''Property setter to set value of the next Node.'''
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    '''Defines an attribute SimglyLinkedList.'''

    def __init__(self):
        '''Instantiating an instance attribute of a Node in a linked list.'''
        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a value in a sorted order into the linked list.
        Parameters:
                value: value to be inserted.
        '''
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            while (temp_node.next_node is not None and
                    temp_node.next_node.data < value):
                temp_node = temp_node.next_node
                temp_node.next_node = new_node

    def __print_list__(self):
        '''Prints the elements of the SinglyLinkedList.'''
        data_value = []
        temp_node = self.__head
        while temp_node is not None:
            data_value.append(str(temp_node.data))
            temp_node = temp_node.next_node
        return ('\n'.join(data_value))
