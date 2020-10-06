def get_parents(ancestors, node):
    parents = []
    for i in ancestors:
        if i[1] == node:
            parents.append(i[0])
    
    if len(parents) > 0:
        return parents

    else:
        return -1


def earliest_ancestor(ancestors, starting_node):
    node = starting_node
    parents = []
    go = True
    while go:
        if get_parents(ancestors, node) == -1:
            go = False
            if len(parents) < 1:
                return -1
            else:
                return parents[0]
        else:
            parents = get_parents(ancestors, node)
            node = parents[0]



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print("should be 10")

print(earliest_ancestor(test_ancestors, 2))