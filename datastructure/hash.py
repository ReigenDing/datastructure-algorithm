
# -*- coding: utf-8 -*-


class Hash:
    def __init__(self):
        self.capability = 11
        self.hash_table = [[None, None] for i in range(self.capability)]
        self.num = 0
        self.load_factor = 0.75
    
    # 散列函数
    def hash(self, k, i):
        h_value = (k+i) % self.capability
        if self.hash_table[h_value][0] == k:
            return h_value
        # 处理hash冲突，使用了开放定址法 #
        if self.hash_table[h_value][0] != None:
            i += 1
            h_value = self.hash(k, i)
        return h_value
    
    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        self.num += 1
        if self.num / len(self.hash_table) >= self.load_factor:
            self.resize()
        
    def resize(self):
        print("resizing......")
        self.capability = 2 * self.capability
        temp = self.hash_table[:] 
        self.hash_table = [[None, None] for i in range(self.capability)]
        for ele in temp:
            if ele[0] is not None:
                hash_v = self.hash(ele[0], 0)
                self.hash_table[hash_v][0] = ele[0]
                self.hash_table[hash_v][1] = ele[1]




    def get(self, k):
        print(self.hash_table)
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


class MyDict:

    def __init__(self):
        self.table_size = 13
        self.key_list = [None] * self.table_size
        self.value_list = [None] * self.table_size
    
    def hash_function(self, key):
        count_char = 0
        key_string = str(key)
        for key_char in key_string:
            count_char += ord(key_char)
            print(count_char)
        length = len(str(count_char))
        if length > 3:
            mid_int = 100 * int((str(count_char)[length // 2 -1])) \
                + 10 * int((str(count_char//2)[length//2])) \
                + 1 * int((str(count_char)[length // 2 + 1]))
        else:
            mid_int = count_char
        return mid_int % self.table_size
    
    def rehash(self, hash_value):
        """
        重新散列函数，返回新的散列值，hash_value为旧的散列值
        重新散列的逻辑：向前间隔为3的线性探测
        """
        return (hash_value + 3) % self.table_size

    def __setitem__(self, *args):
        print("setitem")
        print(args)

    def __getitem__(self, *args):
        print("getitem")
        print(args)

    def __delitem__(self, *args):
        print("del")
        print(args)
    
    def __len__(self, *args):
        print("__len__")
        print(args)
        return 3



if __name__ == "__main__":
    # hash = Hash()
    # hash.put(1, "ding")
    # print(hash.get(1))
    # hash.put(6, "ding2")
    # print(hash.get(6))
    # hash.put(6, "ding7")
    # hash.put(7, "ding8")
    # hash.put(8, "ding9")
    # hash.put(9, "ding10")
    # hash.put(10, "ding11")
    # hash.put(11, "ding12")
    # hash.put(12, "ding13")
    # hash.put(13, "ding14")
    # hash.put(14, "ding15")
    # hash.put(16, "ding16")
    # hash.put(15, "ding17")
    # print(hash.get(12))
    # print(hash.get(6))
    mydict = MyDict()
    mydict[0] = "test"
    mydict[0]
    print(len(mydict))
    del mydict[0]
    hash_value = mydict.hash_function("tttt2123sfdasfs")
    print(hash_value)


















