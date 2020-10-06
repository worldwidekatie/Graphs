# Representation of graphs

# Which nodes are adjacent (directly connected) 
# to a particular node? 

# The nodes you are adjacent to are the ones you can reach
# in one hop.

# Adjacency matrix
## Big grid that has true/false values showing which
## nodes are adjacent (or edge weights)

# Adjacency list
## Keeps track of which nodes connect to other nodes.

# A: {B, D} #For weights, make it tuples e.g. [(B, 2), (D, 3)]
# B: {D, C}
# C: {B, C}
# D: {}
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.verticies = {} # keys are all the verts in the graph
                            # values are sets of adjacent verts
        
    def add_vertex(self, vertex):
        """Add a new unconnected vert"""
        self.verticies[vertex] = set()

    def add_edge(self, v_from, v_to):
        if v_from in self.verticies and v_to in self.verticies: # keys are all the verts in the graph
            self.verticies[v_from].add(v_to) # add is a set method
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, v):
        return self.verticies[v]

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()

        # Init:
        q.enqueue(starting_vertex_id)

        # While queue isn't empty
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v) # "Visited" the node
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
    
    def dft(self, starting_vertex_id):
        s = Stack()
        visited = set()
        # Init:
        s.push(starting_vertex_id)

        # While queue isn't empty
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v) # "Visited" the node
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
    
    def dft_recursive(self, starting_vertex_id, visited=None):

        if visited is None:
            visited=set()
        
        print(starting_vertex_id) # Visited!
        visited.add(starting_vertex_id)

        for neighbor in self.get_neighbors(starting_vertex_id):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
    
    def dfs_recursive(self, starting_vertex_id, target_vertex_id, visited=None, path=None):

        if visited is None:
            visited=set()

        if path is None:
            path = [starting_vertex_id]

        print(starting_vertex_id) # Visited!
        visited.add(starting_vertex_id)

        for neighbor in self.get_neighbors(starting_vertex_id):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == target_vertex_id:
                    return new_path

                dfs_path = self.dfs_recursive(neighbor, target_vertex_id, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
        
        return None


    def bfs(self, starting_vertex_id, target_vertex_id):
        q = Queue()
        visited = set()

        # Init:
        q.enqueue([starting_vertex_id])

        # While queue isn't empty
        while q.size() > 0:
            path = q.dequeue()

            # end of path nod is path[-1]
            v = path[-1]
            if v not in visited:
                if v == target_vertex_id:
                    return path # Found it!
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)


    def bfs_recursive(self, starting_vertex_id, target_vertex_id):
        q = Queue()
        visited = set()

        # Init:
        q.enqueue([starting_vertex_id])

        # While queue isn't empty
        while q.size() > 0:
            path = q.dequeue()

            # end of path nod is path[-1]
            v = path[-1]
            if v not in visited:
                if v == target_vertex_id:
                    return path # Found it!
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)
# g = Graph()
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(3)

# g.add_edge(2, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 3)

# print(g.verticies)
# # print(g.bft(2))
# # print(g.dft(2))
# print(g.bfs(1, 2))
# print(g.bfs(1, 3))
# print(g.bfs(2, 3))
# print(g.bfs(2, 1))
# print(g.bfs(3, 1))

# g = Graph()
# g.add_vertex('A')
# g.add_vertex('y')
# g.add_vertex('x')
# g.add_vertex('z')

# g.add_edge('A', 'x')
# g.add_edge('x', 'A')
# g.add_edge('A', 'y')
# g.add_edge('y', 'z')
# g.add_edge('z', 'x')

# print(g.verticies)
# #print(g.dft_recursive('A'))
# print(g.dfs_recursive('A', 'z'))
# print(g.dfs_recursive('A', 'x'))
# Breadth-first Traversal, visit every node
# Everything at distance 1 is visited
# Then everything at distance 2 (number of hops)
# Then everything at distance 3, etc.

#BTF

# Init:
## Add the starting vert to the queue
# While the queue is not empty
## pop current vert off queue
## if not visited:
### "visit" the node
### Track it as visited
### Add all its neighbors (adjacent nodes) to the queue

# Breadth-first search, looking for certain node/shortest path

"""
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not
a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
"""

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return ['hit', 'hot', 'cot', 'cog']

# begin_word = "sail"
# end_word = "boat"
# return ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# return None
from string import ascii_lowercase

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def get_neighbors(word):
    neighbors = []
    for w in words:
        if len(w) == len(word):
            diff_count = 0

            for i in range(len(w)):
                if w[i] != word[i]:
                    diff_count += 1

                if diff_count > 1:
                    break

            if diff_count == 1:
                neighbors.append(w)
    return neighbors

def get_neighbors2(word):
    neighbors = []
    letters = list(ascii_lowercase)

    word_letters = list(word)

    for i in range(len(word_letters)):
        for l in letters:
            word_letters_copy = list(word_letters)
            word_letters_copy[i] = l
            candidate_word = "".join(word_letters_copy)

            if candidate_word != word and candidate_word in words:
                neighbors.append(candidate_word)
    
    return neighbors


def bfs(begin_word, end_word):
    if len(begin_word) != len(end_word):
        return None

    visited = set()
    q = Queue()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path
            
            for neighbor in get_neighbors2(v):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)

words = set()
with open('words.txt') as f:
    for w in f:
        w = w.strip()
        words.add(w)
# print(words)
# print(len(words))

# print(func('happy', 'hungry', []))

print(bfs('hit', 'cog'))
print(bfs('sail', 'boat'))