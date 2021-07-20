from tree import *
from collections import defaultdict


def paths_with_sum(root: BTNode, s):
    """Find the number of paths for which the sum of the path gives the needed value."""
    # Solution: O(n) where n is the number of nodes in the tree, O(n) space for hash table.

    return helper(root, 0, s, defaultdict(int))

    

def helper(root: BTNode, running, s, sum_map):
    # running is the running sum so far.
    # s is the sum to get.
    # sum_map stores the number of times we have seen a running sum through our search.

    # Base case. If root is None, then return 0.
    if root is None:
        return 0
    
    paths = 0
    # If we minus the required sum from the running sum, we will get a running sum we have gotten before,
    # for which the path from that running sum to this running sum will give the required sum.
    # Therefore, we can lookup the number of times the other running sum has appeared before,
    # to get the number of paths.
    other_running = running - s
    paths += sum_map[other_running]
    # Since the root node is not counted (for which the sum is zero), we have to take into account if 
    # the current sum is equal to the required sum. If it is, then we add one extra.
    if running == s:
        paths += 1

    # We add this current sum to the sum_map.
    sum_map[running] += 1
    # Then we return the number of times the node's subtrees encounter this sum.
    paths += helper(root.left, running, s, sum_map) + helper(root.right, running, s, sum_map)
    # Remember to remove the current sum from the sum_map after subtrees have been counted.
    sum_map[running] -= 1
    return paths
