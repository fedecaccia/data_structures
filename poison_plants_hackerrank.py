#!/bin/python3

import math
import os
import random
import re
import sys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Plants(object):

    # Complete the poisonousPlants function below.
    def poisonousPlants(self, p):

        if len(p) == 0:
            return 0

        first_node = Node(p[0])
        n_prev = first_node

        if len(p) > 1:
            for pi in p[1:]:
                n = Node(pi)
                n_prev.next = n
                n_prev = n

        days = -1
        scanning = True        

        while (scanning):
            
            days += 1
            n = first_node
            n_last_survivor = n
            scanning = False

            while n.next is not None:
                
                n_prev = n
                n = n.next

                if n.value > n_prev.value:
                    scanning = True
                    # n_prev.next = n.next
                    n_last_survivor.next = n.next
                else:
                    n_last_survivor = n

        return days
