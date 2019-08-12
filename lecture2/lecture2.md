2. [Lecture II: Applied Graph Search](#Lecture-II)
    <br>a. [When do you use BFS over DFS?](#When-do-you-use-BFS-over-DFS?)
    <br>b. [Why can we use DFS recursively?](#Why-can-we-do-DFS-recursively-but-not-really-BFS?)
    <br> c. [Example Code Challenge](#Let's-try-an-example-problem)
    <br>
    <br>

# Lecture II 

[CS18 Lecture II Recording](https://www.youtube.com/watch?v=Yi7V4AzhFPc)

A traversal search visits every single node in an order and does something (make a change, mark as visited, print, etc.).

In a Breadth-First Search, we're still traversing the nodes but only _looking_ for the target and return the item or the path to that node. We're returning the shortest path each time, whereas Depth First does not return the _shortest_ path.

![Example Graph](../img/dfs-visit-order-2.png "Example Graph")


If we're looking at this graph and try to find the shortest path from 1 to 6, it should return [1, 2, 4, 6].

If we were looking from 1 to 3, the shortest path is [1, 2, 3] but a perfectly valid answer would also be [1, 2, 4, 6, 3]. BFS will always gives us the shortest route whereas DFS might give us an alternate route that is not the shortest.


#### When do you use BFS over DFS?

BFS is good for giving the shortest path but the downsides are that you need to hold each entire row in memory (which is bad on a very wide graph where the solution is in depth).

Large sets of data/possible solutions is better for DFS (memory efficient) but BFS is best for when we want the shortest path. If we need to go deep into a tree, DFS is better.

Sometimes it doesn't matter.

BFS always returns the shortest path because it looks at _all_ the possibilities to find something 1 step away, then 2 steps away, then 3 steps away....until it finds a successful path.

With DFS, it's searching paths but not across all one path possibilites first. It's going down a path to see if it's a _possible_ path -- not if it's the shortest.

Let's try a recursive DFS algorithm:

```
def dft_recursive(self, starting_vertex, visited=set() ):
    # Print each vertex in depth-first order beginning from starting_verex. This should be done using recursion.

    # If the node hasn't been visited...
    if starting_vertex not in visited:
        # Mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
    # Then call DFT_recursive on each child
    for neighbor in self.vertices[starting_vertex]:
        self.dft_recursive(neighbor, visited)

```

While this solution would work once, why won't it work if it gets called more than once?

Python handles default values a little uniquely. `visited=set()` will create this default value once and use it each time, referencing the same place in memory, even if we want to call it a second time where the set() should initialize as a different value.

This is a common Python gotcha, but not the case in other languages (like Ruby).

Instead, we need to initialize like so:

```
def dft_recursive(self, starting_vertex, visited=None ):
    # Print each vertex in depth-first order beginning from starting_verex. This should be done using recursion.
    if visited is None:
        visited = set()
```

We have to always set it to None and then initialize it within the function, if we want a default value to be set to variable data.

#### Why can we do DFS recursively but not really BFS?

Recursion has to be called on a new node each time, independently each time. But BFS puts all of the children into the queue at the same time, so it can't be used recursively.

(There is a way to search BFS with a while loop that is not entirely recursion but similar.)


##### How does DFS work on each loop?

Looking at this example graph, let's find a path from 1 to 3:

![Example Graph](../img/dfs-visit-order-2.png "Example Graph")


We want to find a path from our starting vertex (1) to the destination vertex (3)

```
start = 1
target = 3

stack = [] # stack
visited = {} # set
```

The first loop goes:

```
stack = [1]
visited = {}

path = [1]
path_copy = [1, 2]
v = 1
```

The next loop:

```
stack = [1,2]
visited = {1}

path = [1, 2]
path_copy = [1, 2, 3]
v = 2
```

But there's also a path to [1,2,4] so we need:

```
path = [1, 2]
path_copy = [1, 2, 4]
```

So now...

```
stack = [ [1,2,3], [1,2,4]]
visited = {1, 2}

path = [1,2 4]
path_copy = [1, 2, 4, 6]
v = 3

path = [1,2 4]
path_copy = [1, 2, 4, 7]
v = 3
```

Next loop:

```
stack = [ [1,2,3], [1,2,4,6], [1,2,4,7]]
visited = {1, 2, 4}

path = [1,2,4,7]
path_copy = [1, 2, 4, 7, 6]
v = 4
```

Next loop:

```
stack = [ [1,2,3], [1,2,4,6], [1,2,4,7]]
visited = {1, 2, 4, 7}

path = [1,2,4,7,6]
path_copy = [1, 2, 4, 7, 6, 3]
v = 5
```

Next loop:

```
stack = [ [1,2,3], [1,2,4,6], [1,2,4,7,6,3]]
visited = {1, 2, 4, 7,6}

path = [1,2,4,7,6,3]
```

Since 3 is our target, we return the path. It's not the shortest but that's how DFS iterates through, checking the possibilities of each path.



### Let's try an example problem

Using Leet Code's Word Ladder problem (https://leetcode.com/problems/word-ladder/)

```
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
```

We want to change one letter at a time and see if this word exists in the given list.

Let's use POLYA and our steps for solving graph problems.

1. Translate the problem
2. Build your graph
3. Traverse your graph


##### How do we recognize that this is a graph problem? 

It doesn't look ike a graph problem off the bat. We need to look for some key words, like "shortest transformation sequence" or are seeking the relationships between things (words are one letter away).

Many coding challenges are graph problems, because they're tricky and they contain many data structures and concepts. They're usually shorter on code for a solution once the idea is solved.

First, let's translate this problem into graph terminology.

What are the nodes, edges, weights and how do we traverse the graph?

Words are our vertices. Neighbors are our edges (connection between words that are only one letter apart).

Using the first example:

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
```

Starting vertex is "hit", goal vertex is "cog".

We should use BFS because the problem is asking us for the _shortest_ path.

"Transformation sequence" should make you think of BFS as well. 

"Word" is the graph vertex. "One letter change" is the graph edge.


##### Build Your Graph

What graph operations are necessary?
Our vertex list needs to become a word list.

We need to define a function to get all edges (neighbors).

Using our basic BFS formula (that is being memorized):

```
# Implement our traversal
def find_ladders(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue( [beginWord] )
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == endWord:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
```

Now we need to define our `getNeighbors()` function that's being called.

We could loop over the letters in both words, at the same time, and set a count variable for all differences. If the count is exactly 1, then it's a neighbor. This comparison would be O(n) time where n is the length of the wordList we're comparing the given word to.

That's not a problem when the list has 7 words, but an issue when it contains a full dictionary of words in the tens of thousands.

We could search using a "wild card" by trying to find the neighbors of "cab" by searching for all words that would match `"*ab"`, `"c*b"`, and `"ca*"`.

We would start by placing our wordList into a set.

```
word_set = set(["hot", "dot", "dog", "lot", "log", "cog"])
```

If we searched the wildcard of `*it`:

`ait`
`bit`
`cit`
`dit`...

and so on, checking 26 possibilities if they are in the set.

We'll repeat this for each following letter in the word.

This is also `O(n)` but where n is the word length, not the wordlist we search through. While it's O(26 * n), that's not very long compared to the tens of thousands of a word list.

Understanding how to compare O(n) where n is a different variable helps us decide which method of solving a problem is more efficient.

Let's test out our get_neighbors function:

```
word_set = set(["hot", "dot", "dog", "lot", "log", "cog"])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get neighbors function
def get_neighbors(word):
    # A neighbor is all words in the word list that differ by exactly one letter
    
    # create an empty neighbors list
    neighbors = []
    # turn our word into an array of characters
    string_word = list(word)
    # for each letter in the word...
    for i in range(len(string_word)):
        # For each letter in the alphabet...
        for letter in letters:
            # Make a copy so we don't override our item
            # swap that letter with a letter in the alphabet
            temp_word = list(string_word)
            temp_word[i] = letter
            # reform it into a word string and check if it's in word_set
            w = "".join(temp_word)
            # if it doesn't equal the original word and it's in the set, add to neighbors
            if w !== word and w in word_set:
                neighbors.append(w)
```

Now that both functions are written, we can use get_neighbors to run a BFS and efficiently solve this code challenge.

But how would this solution scale if we have a wordList with over 200,000 words? 

Testing against a large data set is a good way to see how efficient our solution is.

It's still running quickly. The set allows us to check efficiently.

So, overall, this ladder problem was just a path finding problem, perfecting for graphing.

Today's assignment is solving the Earliest Ancestor code challenge.

<br>
<br>