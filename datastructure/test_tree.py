#! --*-- coding: utf-8 --*--


import pytest
from datastructure import tree


@pytest.fixture
def btree():
    node1 = tree.BinaryTree(1)
    node2 = tree.BinaryTree(2)
    node3 = tree.BinaryTree(3)
    node4 = tree.BinaryTree(4)
    node5 = tree.BinaryTree(5)
    node6 = tree.BinaryTree(6)
    node7 = tree.BinaryTree(7)
    node8 = tree.BinaryTree(8)
    node9 = tree.BinaryTree(9)
    node10 = tree.BinaryTree(10)
    node11 = tree.BinaryTree(11)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    node5.left = node10
    node5.right = node11
    return node1


def test_pre_order(btree):
    temp = []
    res = tree.preOrder(btree, temp)
    print(res)
    print(temp)
    assert temp == temp




