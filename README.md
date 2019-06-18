# Graphs

#### Pre-Class Resources

Intro to Graphs - Components, Uses & Types: https://youtu.be/Etva3hOjGMU
Depth First Search: https://youtu.be/VTLI7l-Ah-8
Breadth First Search: https://youtu.be/BK_8-XVp5XA

Article: A Gentle Introduction to Graph Theory: https://medium.com/basecs/a-gentle-introduction-to-graph-theory-77969829ead8

## Lecture I Notes: Graphs Intro, Representations & BFS/DFS

#### What are Graphs?

Graphs are a generalized data structure that represent relationships between data like linked lists or a binary tree. Anything you can do in those data structures, you can do in a graph.

The components that make up a graph are:

- Nodes of Vertices: these represent objects in a data set (like cities, animals, web pages, etc)

- Edges: the connections between vertices, they can be bi-directional

- Weight: the cost to travel across an edge

For example, cities could be vertices, with roads as the edges that connect all the cities. Not all edges are created equally so it may take more time or resources to go from one node to another.

![Edges and weights](edges_weights.png "Edges and Weights")


What are graphs useful for?

They allow us to understand data and the relationship between the data better. For example, we might use a subway graph to understand to go from one station to another.

There are several types of graphs:

- `Directed Graph`: can only move in one direction along edges, like a single linked list.

- `Undirected Graph`: allows movement in both directions along edges, like a doubly linked list.

- `Cyclic Graph`: edges allow you to revisit at least one vertice, like a graph demonstrating the water cycle. There are states that water can revisit multiple times.

- `Acyclic Graph`: vertices can only be visited once. A recipe turned into a graph might be acyclic because some steps should only be done _once_.


If there are no weights on the edges, it's considered an `Unweighted Graph`.




#### What will we be learning?

We'll work with traversals and searches - breadth first search v depth first search. These are two search types that _should_ be memorized in their most basic form; but depending on your graph implementation and data, those searches will need to be adjusted and tweaked.

You can turn almost any code challenge into a graph - because everything can be turned into a graph that shows the relationship between data. Graphs also come up frequently when interviewing and doing take home challenges.

We'll use _translation_ techniques to turn an algorithm into a graph.

Handling graph problems follow the same three steps each time:

1. Translate into Graph terminology
2. Build Your Graph
3. Traverse the Graph

_Further learning: Dijkstra's's Algorithm (shortest path first) is a form of Breadth First Search. Once you learn BFS, learning that would be easier._










