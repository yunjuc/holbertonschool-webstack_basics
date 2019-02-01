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
        while self.__head is not None:
            print(self.__head.data)
            self.__head = self.__head.next_node

    def sorted_insert(self, value):
        '''insert node to sorted list'''
        if self.__head is None:
            self.__head = Node(value)
            return

        if self.__head.next_node is not None:
            while self.__head.next_node:
                if value <= self.__head.data:
                    temp = self.__head
                    self.__head = Node(value)
                    self.__head.next_node = temp
                    return
                elif value <= self.__head.next_node.data:
                    temp = self.__head.next_node
                    self.__head.next_node = Node(value)
                    self.__head.next_node.next_node = temp
                    return
                self.__head = self.__head.next_node

        if value > self.__head.data:
            self.__head.next_node = Node(value)
            return
        else:
            temp = self.__head
            self.__head = Node(value)
            self.__head.next_node = temp
