# -*- coding: utf-8 -*-

import os
import pickle


class Node:

    def __init__(self, data, nx):
        self.data = data
        self.next = nx


def enum(root: Node):
    index = 0
    while True:
        if root is None:
            break
        with open("file-{}".format(index), mode="a") as f:
            f.write(str(pickle.dumps(root)) + "\n")
        print(root.data)
        root = root.next
        if os.path.getsize("file-{}".format(index)) > 1 * 1024:
            index += 1


# def recover():
#     index = 0
#     with open("file-{}".format(index), "r") as f:
#         lines = f.readlines()
#     for line in lines:
#         print(type(line))
#         data = pickle.loads(bytes(line))



def recovery():
    index=0
    while True:
        if not os.path.exists("file-{}".format(index)):
            break
        with open("file-{}".format(index), mode="r", encoding="utf-8") as rf:
            lines=rf.readlines()
        for line in lines:
            line=eval(line)
            node=pickle.loads(bytes(line))
            print(node.data)
            print(node.next)
        index += 1


node8=Node(data="88888888888888", nx=None)
node7=Node(data="77777777777777", nx=node8)
node6=Node(data="66666666666666", nx=node7)
node5=Node(data="55555555555555", nx=node6)
node4=Node(data="44444444444444", nx=node5)
node3=Node(data="33333333333333", nx=node4)
node2=Node(data="22222222222222", nx=node3)
node1=Node(data="11111111111111", nx=node2)


if __name__ == "__main__":
    # enum(node1)
    recovery()
