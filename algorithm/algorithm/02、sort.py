# Bubble sort冒泡排序

from typing import Mapping


def bubble_sort(alist):
    # 相邻连个元素进行比较，如果发现位置错误则进行交换位置
    print(id(alist))
    length = len(alist)
    for k in range(length):
        for i in range(length-1-k):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(alist)
    print(alist)


# 如果传入的列表就是有序，只需要检测一轮，如果没有进行交换，则直接退出循环
def bubble_sort2(alist):
    # 相邻连个元素进行比较，如果发现位置错误则进行交换位置
    print(id(alist))
    length = len(alist)
    for k in range(length-1):
        count = 0
        for i in range(length-1-k):
            if alist[i] > alist[i+1]:
                count += 1
                alist[i], alist[i+1] = alist[i+1], alist[i]
        print(alist)
        if count == 0:
            break
    print(alist)


# 选择排序
# #
def selection_sort(alist):
    length = len(alist)
    for j in range(length):
        for i in range(length-j):
            if alist[j] > alist[i+j]:
                alist[j], alist[i+j] = alist[i+j], alist[j]
        print(i, j, " => ", alist)
    print(alist)


if __name__ == "__main__":
    alist = [7 ,4, 6, 9, 1]
    alist2 = [1, 2, 3, 4, 5]
    alist3 = [1, 2, 4, 3, 5]
    # print(id(alist))
    # bubble_sort(alist)
    # print(alist)
    # bubble_sort2(alist)
    # bubble_sort2(alist2)
    # bubble_sort2(alist3)
    selection_sort(alist)
