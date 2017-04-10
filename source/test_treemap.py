#!python

from treemap import TreeMap
import unittest


class TestTreeMap(unittest.TestCase):

    def test_init(self):
        map = TreeMap()
        assert map.size == 0

    def test_size(self):
        map = TreeMap()
        assert map.size == 0
        map.set('I', 1)
        assert map.size == 1
        map.set('V', 5)
        assert map.size == 2
        map.set('X', 10)
        assert map.size == 3

    def test_keys(self):
        map = TreeMap()
        assert map.keys() == []
        map.set('I', 1)
        assert map.keys() == ['I']
        map.set('V', 5)
        self.assertItemsEqual(map.keys(), ['I', 'V'])  # Ignore item order
        map.set('X', 10)
        self.assertItemsEqual(map.keys(), ['I', 'V', 'X'])  # Ignore item order

    def test_values(self):
        map = TreeMap()
        assert map.values() == []
        map.set('I', 1)
        assert map.values() == [1]
        map.set('V', 5)
        self.assertItemsEqual(map.values(), [1, 5])  # Ignore item order
        map.set('X', 10)
        self.assertItemsEqual(map.values(), [1, 5, 10])  # Ignore item order

    def test_items(self):
        map = TreeMap()
        assert map.items() == []
        map.set('I', 1)
        assert map.items() == [('I', 1)]
        map.set('V', 5)
        self.assertItemsEqual(map.items(), [('I', 1), ('V', 5)])
        map.set('X', 10)
        self.assertItemsEqual(map.items(), [('I', 1), ('V', 5), ('X', 10)])

    def test_contains(self):
        map = TreeMap()
        map.set('I', 1)
        map.set('V', 5)
        map.set('X', 10)
        assert map.contains('I') is True
        assert map.contains('V') is True
        assert map.contains('X') is True
        assert map.contains('A') is False

    def test_set_and_get(self):
        map = TreeMap()
        map.set('I', 1)
        map.set('V', 5)
        map.set('X', 10)
        assert map.get('I') == 1
        assert map.get('V') == 5
        assert map.get('X') == 10
        assert map.size == 3
        with self.assertRaises(KeyError):
            map.get('A')  # Key does not exist

    def test_set_twice_and_get(self):
        map = TreeMap()
        map.set('I', 1)
        map.set('V', 4)
        map.set('X', 9)
        assert map.size == 3
        map.set('V', 5)  # Update value
        map.set('X', 10)  # Update value
        assert map.get('I') == 1
        assert map.get('V') == 5
        assert map.get('X') == 10
        assert map.size == 3  # Check size is not overcounting

    def test_delete(self):
        map = TreeMap()
        map.set('I', 1)
        map.set('V', 5)
        map.set('X', 10)
        assert map.size == 3
        map.delete('I')
        assert map.size == 2
        assert map.contains('I') is False
        with self.assertRaises(KeyError):
            map.delete('I')  # Key no longer exists
        map.delete('V')
        assert map.size == 1
        assert map.contains('V') is False
        with self.assertRaises(KeyError):
            map.delete('V')  # Key no longer exists
        map.delete('X')
        assert map.size == 0
        assert map.contains('X') is False
        with self.assertRaises(KeyError):
            map.delete('X')  # Key no longer exists
        with self.assertRaises(KeyError):
            map.delete('A')  # Key does not exist


if __name__ == '__main__':
    unittest.main()
