import unittest

from lru import Lru


class LruTest(unittest.TestCase):
    def test_init(self):
        lru = Lru()
        self.assertIsInstance(lru, Lru)

    def test_add_int_key(self):
        lru = Lru()
        lru.addEntry(8, 16)
        keys = list(lru.entryMap.keys())
        self.assertEqual(keys, [8])

    def test_add_str_key(self):
        lru = Lru()
        lru.addEntry('q29fk', 16)
        keys = list(lru.entryMap.keys())
        self.assertEqual(keys, ['q29fk'])

    def test_get_entry(self):
        lru = Lru()
        lru.addEntry(8, 16)
        val = lru.getEntry(8).value
        self.assertEqual(val, 16)

    def test_get_invalid_entry(self):
        lru = Lru()
        lru.addEntry(8, 16)
        val = lru.getEntry(0)
        self.assertEqual(val, -1)

    def test_modify_entry(self):
        lru = Lru()
        lru.addEntry(8, 10)
        lru.addEntry(8, 20)
        lru.addEntry(8, 42)
        val = lru.getEntry(8).value
        self.assertEqual(val, 42)

    def test_evict_cache(self):
        lru = Lru()
        lru.lruSize = 4  # assume lruSize = 4
        lru.addEntry(1, 1)
        lru.addEntry(2, 1)
        lru.addEntry(3, 2)
        lru.addEntry(4, 3)
        lru.addEntry(5, 5)

        vals = lru.getCacheInOrder()
        self.assertEqual(vals, [5, 3, 2, 1])

    def test_mixed_use_01(self):
        lru = Lru()
        lru.addEntry(0, 0)
        lru.addEntry(1, 2)
        lru.addEntry(2, 4)
        lru.addEntry(3, 6)
        node0 = lru.getEntry(0)
        lru.addEntry(4, 8)

        vals = lru.getCacheInOrder()
        self.assertEqual(vals, [8, 0, 6, 4])
        self.assertEqual(node0.value, 0)

    def test_mixed_use_02(self):
        lru = Lru()
        lru.addEntry(0, 0)
        lru.addEntry(1, 2)
        lru.addEntry(2, 4)
        lru.addEntry(3, 6)
        lru.getEntry(0)
        lru.addEntry(4, 8)
        node = lru.getEntry(1)
        lru.addEntry(5, 10)

        vals = lru.getCacheInOrder()
        self.assertEqual(vals, [10, 8, 0, 6])
        self.assertEqual(
            node, -1, 'Node having key 1 should have been evicted')
