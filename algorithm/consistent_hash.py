import bisect
from hashlib import md5


class ConsistentHashRing:
    def __init__(self, replicas=100):
        self.replicas = replicas
        self._keys = []
        self._nodes = {}

    def _hash(self, key):
        return md5(key.encode()).hexdigest()

    def _repl_iterator(self, nodename):
        return (self._hash("{}:{}".format(nodename, i)) for i in range(self.replicas))

    def __setitem__(self, nodename, node):
        """
        Add a node, given its name. The given nodename is hashed
        among the number of replicas
        """
        for hash_ in self._repl_iterator(nodename):
            if hash_ in self._nodes:
                raise ValueError(
                    "Node name {} is already present".format(nodename))
            self._nodes[hash_] = node
            bisect.insort(self._keys, hash_)

    def __delitem__(self, nodename):
        """
        remove a node, given its name
        """
        for hash_ in self._repl_iterator(nodename):
            del self._nodes[hash_]
            index = bisect.bisect_left(self._keys, hash_)
            del self._keys[index]

    def __getitem__(self, key):
        """
        Return a node given a key. The node replica with a 
        hash value nearest but not less than that of given 
        name is returned. If the hash of the given name is greater
        than the greatest hash, return the lowest hashed node.

        """
        hash_ = self._hash(key)
        print(hash_)
        start = bisect.bisect(self._keys, hash_)
        print(start)
        print(self._keys[start-1])
        print(self._keys[start])
        print(self._keys[start+1])
        if start == len(self._keys):
            start = 0
        return self._nodes[self._keys[start]]
