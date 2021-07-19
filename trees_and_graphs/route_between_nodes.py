def route_between_nodes(n1, n2):
    """Find out whether there is a route between n1 and n2."""
    # Solution: O(k^(b/2)) time and space, k is the average number of neighbour nodes for each node,
    # b is the breadth of the search.

    # Use a queue to do BFS through n1's and n2's neighbours.
    n1_search = set()
    n1_search.add(n1)
    n1_store = set()

    n2_search = set()
    n2_search.add(n2)
    n2_store = set()

    while len(n1_search) != 0 and len(n2_search) != 0:
        # Loop through all nodes in n1 to search, and store their neighbours in a temp buffer
        for node in n1_search:
            if node in n2_search:
                return True
            for n in node.neighbours:
                n1_store.add(n)
        # Replace n1_search with the nodes in n1_store and empty n1_store.
        n1_search = n1_store
        n1_store = set()

        # Do the same thing for n2 nodes.
        for node in n2_search:
            if node in n1_search:
                return True
            for n in node.neighbours:
                n2_store.add(n)
        # Replace n2_search with the nodes in n2_store and empty n2_store.
        n2_search = n2_store
        n2_store = set()
