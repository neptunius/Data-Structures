### Class 9: Friday, April 7 – Tree Traversals

**Topics:**
- [tree traversals]: pre-order, post-order, in-order, level-order

**Resources:**
- review Make School's [tree traversal slides]
- watch Make School's [tree traversal video lecture]
- play with VisuAlgo's [interactive binary search tree visualization][visualgo bst]

**Challenges:**
- implement tree traversal instance methods on your `BinarySearchTree` class using [binary search tree starter code]:
    - `items_in_order` - return a list of all items in the tree found using in-order traversal
    - `items_pre_order` - return a list of all items in the tree found using pre-order traversal
    - `items_post_order` - return a list of all items in the tree found using post-order traversal
    - `items_level_order` - return a list of all items in the tree found using level-order traversal
- run `python binarysearchtree.py` to test `BinarySearchTree` traversal instance methods on a small example
- run `pytest test_binarysearchtree.py` to run the [binary search tree unit tests] and fix any failures
- annotate all class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement `TreeMap` class (map/dictionary abstract data type implemented with binary search tree data structure) with the following properties and instance methods using [tree map starter code]:
    - `keys` - return a list of all keys in the tree map
    - `values` - return a list of all values in the tree map
    - `items` - return a list of all entries (key-value pairs) in the tree map
    - `contains(key)` - check if the tree map contains `key`
    - `get(key)` - return the value associated with `key`, or raise KeyError
    - `set(key, value)` - insert or update `key` with its associated `value`
    - `delete(key)` - delete `key` and its associated value, or raise KeyError
- run `python treemap.py` to test `TreeMap` class instance methods on a small example
- run `pytest test_treemap.py` to run the [tree map unit tests] and fix any failures
- annotate all class instance methods with running time complexity analysis

**Project:**
- [trees and mazes] tutorial on Make School's [Online Academy]

[tree traversals]: https://en.wikipedia.org/wiki/Tree_traversal

[tree traversal slides]: slides/TreeTraversals.pdf
[tree traversal video lecture]: https://www.youtube.com/watch?v=Qd8dKFaRu9I
[visualgo bst]: https://visualgo.net/bst

[binary search tree starter code]: source/binarysearchtree.py
[binary search tree unit tests]: source/test_binarysearchtree.py
[tree map starter code]: source/treemap.py
[tree map unit tests]: source/test_treemap.py

[trees and mazes]: http://make.sc/oa-trees-and-mazes
[Online Academy]: https://www.makeschool.com/academy
