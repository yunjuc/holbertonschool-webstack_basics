#!/usr/bin/python3


class Node:
    '''a node class'''

    def __init__(self, data, next_node=None):
        '''node constructor'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''data getter'''
        return self.__data

    @data.setter
    def data(self, value):
        '''data setter'''
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''next_node getter'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''next_node setter'''
        if isinstance(value, Node) is False and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''singly linked list class'''

    def __init__(self):
        '''singly linked list constructor'''
        self.__head = None

    def __str__(self):
        '''return list in string representation'''
        res = ""
        if self.__head is None:
            return res
        current = self.__head
        while current:
            if current.next_node is None:
                res += str(current.data)
            else:
                res += str(current.data) + '\n'
            current = current.next_node
        return res

    def sorted_insert(self, value):
        '''insert node to sorted list'''
        if self.__head is None:
            self.__head = Node(value)
            return

        current = self.__head
        while current.next_node:
            if value < self.__head.data:
                temp = self.__head
                self.__head = Node(value)
                self.__head.next_node = temp
                return
            elif value < current.next_node.data:
                temp = current.next_node
                current.next_node = Node(value)
                current.next_node.next_node = temp
                return
            current = current.next_node;
        if not self.__head.next_node and value <= self.__head.data:
            temp = self.__head
            self.__head = Node(value)
            self.__head.next_node = temp
            return
        elif value <= current.data:
            temp = current.next_node
            current.next_node = Node(value)
            current.next_node.next_node = temp
            return
        current.next_node = Node(value)
