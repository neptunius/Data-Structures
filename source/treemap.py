#!python

from binarysearchtree import BinarySearchTree


class KeyMatcher(tuple):
    """Provides comparison method used for ordering or matching by key only."""

    def __cmp__(self, other):
        """Compare this tuple to the given tuple for matching by key only."""
        # Check if the given object is a tuple with at least one item
        if isinstance(other, tuple) and len(other) >= 1:
            # Compare only this tuple's key to the other tuple's key
            assert len(self) >= 1
            assert hasattr(self[0], '__cmp__')
            return self[0].__cmp__(other[0])
        else:
            # Otherwise, defer to the default comparison method
            return super(KeyMatcher, self).__cmp__(other)

    def __eq__(self, other):
        """Compare this tuple to the given tuple for matching by key only."""
        # Check if the given object is a tuple with at least one item
        if isinstance(other, tuple) and len(other) >= 1:
            # Compare only this tuple's key to the other tuple's key
            assert len(self) >= 1
            return self[0] == other[0]
        else:
            # Otherwise, defer to the default comparison method
            return super(KeyMatcher, self).__eq__(other)

    def __lt__(self, other):
        """Compare this tuple to the given tuple for matching by key only."""
        # Check if the given object is a tuple with at least one item
        if isinstance(other, tuple) and len(other) >= 1:
            # Compare only this tuple's key to the other tuple's key
            assert len(self) >= 1
            return self[0] < other[0]
        else:
            # Otherwise, defer to the default comparison method
            return super(KeyMatcher, self).__lt__(other)

    def __gt__(self, other):
        """Compare this tuple to the given tuple for matching by key only."""
        # Check if the given object is a tuple with at least one item
        if isinstance(other, tuple) and len(other) >= 1:
            # Compare only this tuple's key to the other tuple's key
            assert len(self) >= 1
            return self[0] > other[0]
        else:
            # Otherwise, defer to the default comparison method
            return super(KeyMatcher, self).__gt__(other)


class TreeMap(object):

    def __init__(self, entries=None):
        """Initialize this tree map and insert the given entries, if any"""
        self.tree = BinarySearchTree()
        self.size = 0  # Count number of key-value entries
        if entries is not None:
            for key, value in entries:
                self.set(key, value)

    def __str__(self):
        """Return a formatted string representation of this tree map"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this tree map"""
        return 'TreeMap({})'.format(repr(self.items()))

    def keys(self):
        """Return a list of all keys in this tree map in order"""
        # TODO: Get all entries from the tree in order and filter only the keys
        ...
        return ...

    def values(self):
        """Return a list of all values in this tree map in order by key"""
        # TODO: Get all entries from the tree in order and filter only the values
        ...
        return ...

    def items(self):
        """Return a list of all entries (key-value pairs) in this tree map in order by key"""
        # TODO: Get all entries from the tree in order
        return ...

    def contains(self, key):
        """Return True if this tree map contains the given key, or False"""
        # Check if the tree contains an entry with the given key
        return self.tree.contains(KeyMatcher(key))

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # Search the tree for an entry with the given key, if one exists
        entry = self.tree.search(KeyMatcher(key))
        if entry is not None:  # Found
            # TODO: Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return ...
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # Search the tree for an entry with the given key, if one exists
        entry = self.tree.search(KeyMatcher(key))
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # TODO: Remove the old key-value entry from the tree first
            ...
        # TODO: Insert the new key-value entry into the tree in either case
        ...

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError"""
        # Search the tree for an entry with the given key, if one exists
        entry = self.tree.search(KeyMatcher(key))
        if entry is not None:  # Found
            # TODO: Remove the key-value entry from the tree
            ...
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))


def test_tree_map():
    # Create a map of 4 entries mapping Roman numerals to Arabic numerals
    entries = [('I', 1), ('V', 5), ('X', 10), ('L', 50)]
    print('entries: ' + str(entries))

    map = TreeMap()
    print('map: {}'.format(map))

    print('\nSetting entries:')
    for key, value in entries:
        map.set(key, value)
        print('set({}, {}), size: {}'.format(key, value, map.size))
        print('map: {}'.format(map))

    print('\nGetting entries:')
    for key, value in entries:
        print('contains({}): {}'.format(key, map.contains(key)))
        print('get({}): {}, expected: {}'.format(key, map.get(key), value))
    print('contains({}): {}'.format('Z', map.contains('Z')))

    print('\nDeleting entries:')
    for key, value in entries:
        map.delete(key)
        print('delete({}), size: {}'.format(key, map.size))
        print('map: {}'.format(map))

    print('\nChecking entries:')
    for key, value in entries:
        print('contains({}): {}'.format(key, map.contains(key)))


if __name__ == '__main__':
    test_tree_map()
