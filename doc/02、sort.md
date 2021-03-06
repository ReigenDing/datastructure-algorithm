#### 排序算法
排序算法（英语： Sorting algorithm）是一种将一串数据按照特定的顺序进行排列的一种算法。

排序算法的稳定性

##### 冒泡排序
冒泡排序（英文：Buble Sort）是一种简单的排序算法。它重复的遍历要排序的数组，一次比较两个元素，如果他们的顺序错误就把它们交换过来。遍历数组的工作是重复的进行直到没有再需要交换的数据。这个算法名字由来是因为越小的元素会进过交换慢慢地浮到数列的顶端。

##### 选择排序
1、选择排序（Selection Sort）是一种简单直观的排序算法。它的工作原理如下：
首先在未排序序列中找到最大（最小）的元素，存放到排列序列中的起始位置，然后，再从剩余未排列元素中继续寻找最大（最小），然后放到已排序的末尾。以此类推，直到所有元素排序完毕。
选择排序的主要优点与数据移动有关。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行最多n-1次交换。在所有完全依靠移动元素的排序方法中，选择排序属于非常好的一种。

2、时间复杂度：
0 => n-1
    1 => n
    2 => n
    ...
    n-1 => n
    O(n)
O(n)
=> O(n^2)
3、稳定性：
不稳定的排序方式

#### 插入排序
1、插入排序（Insert Sort）是一种简单直观的排序算法。它的工作原理是通过构造有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应地位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

2、时间复杂度：
1 => n
    1 => 
最坏的时间复杂度就是： O(n^2)
最优的时间复杂度就是：O(n)
3、稳定性：
稳定的

#### 快速排序
1、快速排序（quicksort），又称为交换排序，通过一趟排序将要排序的数据分割为独立的两个部分。假设要排序的列表是A[0]......A[N-1]，首先任意选取一个数据（通常第一个）作为基准数据，然后将所有比他小的的数都放到它的左边，所有比它大的数字放到它的右边，这个过程称为一趟快速排序。值得注意的是，快速排序不是一种稳定的排序的算法，，也就是说，多个相同的值得相对位置也许会在算法结束之时发成变动。

2、时间复杂度：
nlog(n)

3、稳定性
不稳定

#### 归并排序
1、归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。将数组分解最小之后，然后合并两个有序数组，基本思路就是比较两个数组的最前面的的数，谁小就先取谁，取了后相应地指针就往后移一位。然后再比较，直到一个数组为空，最后把另一个数组的剩余部分复制过来即可。

2、时间复杂度
最优时间复杂度 => nlog(n)
最差时间复杂度 => nlog(n)

3、稳定性
稳定