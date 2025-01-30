import deque form collections

FUNCTION bfs(graph, start):
    SET an empty list 'visted' to store visited nodes
    SET a queue using deque and initialize it with the 'start' node

    WHILE the queue is not empty:
        node = REMOVE the first element from the queue

        IF node is not in 'visted':
            ADD node to 'visited'
            ADD all neighbors of 'node' (graph[node]) to the queue

    RETURN 'visited'



graph = {

    'A": ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F],
    'E': ['F'],
    'F': []
}

print bfs function with args graph and 'A'