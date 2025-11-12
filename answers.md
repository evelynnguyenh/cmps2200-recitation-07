# CMPS 2200 Recitation 10## Answers

**Name:**Hoang Dieu Linh Nguyen
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work of reachable is O(n + m), where n is the number of nodes and m is the number of edges.  
Each node and edge is visited at most once.

- **4)**
In the worst case, we only need to call reachable once to determine if a graph is connected starting from any node covers the entire graph if it’s connected.

- **5)**
The work of connected is O(n + m), because it makes a single call to reachable and no extra work dominates.

---


- **7)**
If we switched to an adjacency matrix, the work of reachable would become O(n^2).  
This is because checking all neighbors for each node requires scanning all n entries per node instead of just its actual neighbors.

