1. [Lecture IV: Maze Traversal](#Lecture-IV:-Maze-Traversal)  
    <br>a. [Social Network Model Solution](#Social-Network-Model-Solution)  
    <br>b. [Implement Degrees of Separation](#Implement-Degrees-of-Separation)  
    <br>c. [Adventure Map Traversing](#Adventure-Map-Traversing)  
    <br>d. [](#)
    <br>e. [](#)

<br>
<br>

# Lecture IV: Maze Traversal

[CS18 Lecture IV Recording](https://www.youtube.com/watch?v=p263i-Shn9o)


Today we're going to go over the social network problems and work on the adventure project within the Graphs Sprint repo.

<br>

## Social Network Model Solution

We want to create a number of users and randomly distribute friendships between them, such that the average friendships per user matches the given integer.

Remember, friendship relationships are (usually) undirected so we always need to create two edges. You cannot be friends with yourself or create a duplicate one.

First we want to add users in our `social.py` file:

```
        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")
```

Now we need to create all possible friendships:

<br>

```
# Create friendships
# numUsers * average number of friendships is how many we should create
# n = total users * average friendships / 2

# First generate all possible friendships (if user 1 is friends with everyone, 2-10; then, user 2 doesn't need to add user 1, but 3 -10, etc.. until every possible friendship that could be created is generated)

possibleFriendships = []
for userID in self.users:
    # this doesn't include the users ID but does include the last possible friend ID
    for friendID in range(userID + 1, self.lastID + 1):
        possibleFriendships.append((userID, friendID))
    # This prints all possible combos without duplicates
```

<br>

What is the time complexity of this? 

`O(n)` for the first loop because we are iterating through all the users; but on the nested loop, we go through some (but not all) of the users on each loop (progressively fewer with each loop as we near the end).

This is still `O(n^2)` even though the second loop doesn't go through all of n with each loop, it averages 1/2 * n ( `O(n/2)` ), but removing the qualifying integer, it's still O(n) * O(n) = `O(n^2)`.

Now let's actually create the friendships and assign them friendships:

<br>

```
# Now we need to actually create users and assign them friendships at random

friendshipsToCreate = random.sample(possibleFriendships, (numUsers * avgFriendships) // 2)
print(friendshipsToCreate)

for friendship in friendshipsToCreate:
    self.addFriendship(friendship[0], friendship[1])

# This results in roughly 2 average friendships per user, even though the friendships are randomly assigned (so some will have 3 or 4, and others only 1 or 2)
```

<br>

If we wanted to do this with a shuffle instead of a random.sample(), it might look like this:

<br>

```
        friendshipsToCreate = (numUsers * avgFriendships) // 2
        random.shuffle(possibleFriendships)
```

<br>

We can check the time it takes to run by adding in some time variables and printing the difference:

<br>

```
if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    end_time = time.time()
    connections = sg.getAllSocialPaths(1)

    print(f'Runtime: {end_time - start_time} seconds')
    print(connections)
```

<br>
<br>


## Implement Degrees of Separation

Now let's try to `getAllSocialPathts(self, userID)`. We'll pass in a userID and return the extended network, and the shortest path between the user and each person in the extended network. 

We're going between each user in the extended network and calculating the distance between that user and the primary user.

We need to use a Breadth First Search (shortest path). We'll need to store the result in a dictionary instead of a set.

```
visited = {}  # Note that this is a dictionary, not a set
# Create empty queue
q = Queue()
q.enqueue( [userID] )
while q.size() > 0:
    path = q.dequeue()
    v = path[-1]
    # Check if visited
    if v not in visited:
        # Store the social path in the visited dictionary
        visited[v] = path
        # Friendships is our edges adjacency list
        for neighbor in self.friendships[v]
            path_copy = list[path]
            path_copy.append(neighbor)
            q.enqueue(path_copy)
return visited
```

This is following the same BFS algorithm that we've worked with all week. Again, memorizing the basic outline will help to implement BFS and DFS easily.

Is this model accurate to real life?

Not exactly. Friendships aren't random. They're usually formed in clusters - Lambda school friendships are probably clustered around the cohort they're in.

Randomness is a powerful tool but can also be limited in reflecting real life.

What is another way we could create these friendships at a linear runtime?

Here we'll account for collisions and continue to run the algorithm until we don't run into a collision.

```
def populateGraphLinear(self, numUsers, avgFriendships):
    # reset graph
    self.lastID = 0
    self.users = {}
    self.friendships = {}

    for i in range(numUsers):
        self.addUser(f'User {i +1}')

    targetFriendships = numUsers * avgFriendships
    totalFriendships = 0
    # A collision is a failed friendship - trying to create one with yourself or one that already exists
    collisions = 0
    while totalFriendships < targetFriendships:
        userID = random.randint(1, self.lastID)
        friendID = random.randint(1, self.lastID)
        if self.addFriendship(userID, friendID):
            totalFriendships += 2
        else:
            collisions += 1
    print(f"Collisions: {collisions}")
```

This has a _much_ faster run time than our previous solution, which has `O(n^2)` runtime, when accounting for the worst case scenario with the nested loops.

If we consider this within an app, knowing if our scale reaches over 10,000 users, the run time of our previous solution would be unacceptable.

Despite this efficiency, when would we maybe not want to use this solution?

The total number of friendships must be less than the number of users - but if it was only _one_ less.... (100 users, each with 99 friends), the number of times it runs into collisions becomes high enough to be detrimental to performance.

In that case, the quadratic equation would perform better because it does not have collision issues.

If we were to write this for a network where we might assume that almost everyone in the network is a friend with everyone else, the quadratic solution would be more performant, even if it doesn't scale well.

Random sampling performs better with sparse graphs.

The shuffle quadratic sampling performs better with dense graphs.

<br>
<br>

## Adventure Map Traversing

This last portion of the project is both your project and Sprint Challenge. Because of its level of difficulty, you have extra time to work on it.

Like a previous repo, we have an `adv.py` file and associated room, player and room files that help us travel (in the class Player).

Our 500 room map allows us to walk North, South, East and West.

There is also visualization code (`python3 adv.py`) to see the map with built in tests that show how many rooms are unvisited.

If we uncomment the REPL code in that file, we can walk around to experiment with how to navigate through the maze.

Our job is to fill out the traversal path with directions.

If we fill it in like so:

```
traversalPath = ['n']
```

Our tests will return that we have 498 unvisited rooms (since we successfully moved to a new room).

We might continue to fill it out like so:

```
traversalPath = ['n', 's', 's', 'w']
```

We can add this code to our room class to print when we visit a room:

```
def __repr__(self):
    return self.name
```

There are also smaller graphs that we can uncomment to use as easier sample graphs for building and testing a solution.

Thinking about this, it's a depth first search because we are not searching level by level, but instead by path.

If we implemented BFS, we'd be backtracking constantly.

With DFS, we're only backtracking after hitting the end of any single path.

Start a graph and begin to build it as you traverse the graph:

```
graph = {}
graph[0] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}


print(player.currentRoom.id)
print(player.currentRoom.getExits())
```

If we move north one room, we'll see that we're now in room one, so we know now that 'n' actually leads to room 1, and that in room 1, 's' leads to room 0:

```
graph[0]['n'] = 1
graph[1] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
graph[1]['s'] = 0
```

Keep building an algorithm that explores every possible exit and fills in the explored paths.

But when we hit a room where all the explored exits have been marked, how do we determine where to go from our graph code?

A room with an unexplored exit has a '?', so we need to find the nearest room with a '?'. We might use BFS to find the _nearest_ (aka, shortest) path with an unexplored exit.

Solely backtracking will get us to a room we have not fully explored, but that's not the most efficient way to get there (as you might backtrack along paths fully explored, to deep levels).

How do you know when your path is complete and you've explored every single room?

Our traversalPath length won't match the number of rooms because we will need to backtrack eventually - so it'll actually be roughly twice as many path moves than rooms.

When entries in the graph equal the number of rooms, then we know it's complete - or when the exit dictionary contains no question marks.

HINT: A stack DFS might not be the best. It may lead you to complications.

HINT: How do you turn a list of exits (n, s, e, w), into a dictionary filled with question marks?

When in doubt, use POLYA and stayed neat, organized, and well-planned.

>Beautiful is better than ugly.  
>Explicit is better than implicit.  
>Simple is better than complex.  
>Complex is better than complicated.  
>Flat is better than nested.  
>Sparse is better than dense.  
>Readability counts.  
>Special cases aren't special enough to break the rules.  
>Although practicality beats purity.  
>Errors should never pass silently.  
>Unless explicitly silenced.  
>In the face of ambiguity, refuse the temptation to guess.  
>There should be one-- and preferably only one --obvious way to do it.  
>Although that way may not be obvious at first unless you're Dutch.  
>Now is better than never.  
>Although never is often better than *right* now.  
>If the implementation is hard to explain, it's a bad idea.  
>If the implementation is easy to explain, it may be a good idea.  
>Namespaces are one honking great idea -- let's do more of those!  

<br>
  
`help(random.sample)` pulls up info on how to use that in the terminal. What is that extension?

<br>
<br>