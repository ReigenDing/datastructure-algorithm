import pytest
from datastructure import hash


@pytest.fixture
def _hash():
    return hash.Hash()


@pytest.mark.parametrize(["k", "v"], [[0, "test0"], [1, "test1"], [8, "test8"], [12, "test12"]])
def test_hash(_hash, k, v):
    hash_v = _hash.hash(k, 0)
    if k <= 11:
        assert hash_v == k
    elif k == 12:
        assert hash_v == 1



def test_put(_hash):
    k = 0
    v = "test"
    _hash.put(0, "test")
    assert _hash.hash_table[0][0] == k
    assert _hash.hash_table[0][1] == v


def test_get(_hash):
    k = 0
    v = "test"
    _hash.put(k, v)
    assert _hash.get(k) == v


def test_resize(_hash):
    capability = _hash.capability
    _hash.resize()
    want_capability = capability * 2
    got_capanility = _hash.capability
    got_capanility2 = len(_hash.hash_table)

    assert got_capanility == got_capanility2
    assert want_capability == got_capanility

@pytest.fixture
def my_dict():
    return hash.MyDict()


@pytest.mark.parametrize(["key"], ["a", "b", "c"])
def test_my_dict_hash(my_dict, key):
    want = ord(key) % my_dict.table_size
    got = my_dict.hash_function(key)
    assert got == want


@pytest.mark.parametrize(["key"], ["a", "b", "c"])
def test_my_dict_rehash(my_dict, key):
    old_hash_value = my_dict.hash_function(key)
    got = my_dict.rehash(old_hash_value)
    want = ((ord(key) % my_dict.table_size) +3) % my_dict.table_size
    assert got == want 














