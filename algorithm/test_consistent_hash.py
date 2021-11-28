import pytest
from consistent_hash import ConsistentHashRing


@pytest.fixture
def chr():
    return ConsistentHashRing()


class TestConsistentHashRing:

    def test_hash(self,chr):
        hv = chr._hash("key")
        print(hv)
        assert 1
    
    def test_repl_iterator(self, chr):
        repl_hash = chr._repl_iterator("node1")
        print(list(repl_hash))
        assert 1

    @pytest.mark.parametrize("node", ["node1", "node2", "node3"])
    def test_add_new_node(self, chr, node):
        chr[node] = node
        print(chr._nodes)
        assert len(chr._nodes) == 100
    
    def test_cache_key(self,chr):
        test_case = ["key1", "key2", "item3"]
        chr["node1"] = "node1"
        chr["node2"] = "node2"
        chr["node3"] = "node3"
        for key in test_case:
            node = chr[key]
            print(node)
            print("=============")