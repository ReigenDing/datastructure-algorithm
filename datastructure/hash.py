# -*- coding: utf-8 -*-


class Hash:
    def __init__(self):
        self.hash_table = [[None, None] for i in range(11)]
    
    # 散列函数
    def hash(self, k, i):
        h_value = (k+i) % 11
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

    def get(self, k):
        print(self.hash_table)
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


if __name__ == "__main__":
    hash = Hash()
    hash.put(1, "ding")
    print(hash.get(1))
    hash.put(6, "ding2")
    print(hash.get(6))
    hash.put(12, "ding7")
    print(hash.get(12))
    print(hash.get(6))



















