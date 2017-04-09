### Class 8: Wednesday, April 5 – Trees

**Topics:**
- [tree], [terminology]
- [binary search tree], [operations][bst operations]

**Resources:**
- review Make School's [tree slides]
- watch Make School's [tree video lecture]
- play with VisuAlgo's [interactive binary search tree visualization][visualgo bst]

**Challenges:**
- implement `BinaryNode` class with the following properties and instance methods using [binary search tree starter code]:
    - `data` - the node's data
    - `left` - the node's left child, if any
    - `right` - the node's right child, if any
    - `is_leaf` - check if the node is a leaf (has no children)
    - `is_internal` - check if the node is internal (has at least one child)
    - `height` - return the node's height (the number of edges on the longest downward path between the node and a leaf)
- implement `BinarySearchTree` class using `BinaryNode` objects with the following properties and instance methods using [binary search tree starter code]:
    - `root` - the tree's root node
    - `size` - the number of nodes in the tree (can be tracked in constant time)
    - `is_empty` - check if the tree is empty
    - `height` - return the tree's height (the number of edges on the longest path between the root node and a leaf)
    - `contains(item)` - check if a node in this tree contains `item`
    - `search(item)` - return a node's data in the tree matching `item`
    - `insert(item)` - insert a new node with `item` in order into the tree
    - `delete(item)` - remove the node with `item` from the tree, or raise ValueError
    - `_find_node(item)` - return the node containing `item` in the tree, or None
    - `_find_parent_node(item)` - return the parent node of where `item` is (or would be) in the tree, or None
- run `python binarysearchtree.py` to test `BinarySearchTree` class instance methods on a small example
- run `pytest test_binarysearchtree.py` to run the [binary search tree unit tests] and fix any failures
- annotate all class instance methods with running time complexity analysis

**Stretch Challenges:**
- implement binary search tree with singly linked list nodes instead of binary tree nodes

**Project:**
- [trees and mazes] tutorial on Make School's [Online Academy]

[tree]: https://en.wikipedia.org/wiki/Tree_(data_structure)
[terminology]: https://en.wikipedia.org/wiki/Tree_(data_structure)#Terminology_used_in_trees
[binary search tree]: https://en.wikipedia.org/wiki/Binary_search_tree
[bst operations]: https://en.wikipedia.org/wiki/Binary_search_tree#Operations

[tree slides]: slides/Trees.pdf
[tree video lecture]: https://www.youtube.com/watch?v=Yr3y78d2KYI
[visualgo bst]: https://visualgo.net/bst

[binary search tree starter code]: source/binarysearchtree.py
[binary search tree unit tests]: source/test_binarysearchtree.py

[trees and mazes]: http://make.sc/oa-trees-and-mazes
[Online Academy]: https://www.makeschool.com/academy
