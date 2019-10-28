A top-view of a tree contains nodes that are the top-most among the common horizontal distanced nodes.

The Horizontal distance of a node is determined by either by adding one to its predecessors horizontal distance (if child is to the right) or by subtracting one to its parents horizontal distance (if child is to the left).

To have a clear representation check the tree below, values in brackets are the horizontal distance

```
     1(0)
       / \
 (-1)2   3(1)
    / \
(-2)4   5(0)
     \    \
   (-1)6    8(1) 
        \     \
      (0)7    9(2)
```

So for each horizontal distance if you pick the top-most node it gives the top-view of the tree.

So For:
DISTANCE                Node

-2                               4

-1                               2

0                                1

1                                3

2                                9

And hence the top view for this tree would be **4 2 1 3 9**

I hope this helps 



