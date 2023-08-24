# CS50_AI
Sandbox following the CS50’s Artificial Intelligence with Python

## Concepts
- state/initial state:
- actions: 
- transition model: Results()
- path cost
- goal test
- solution/optimal solution

## Data structure
- Node: state, parent, action (applied to parent), a path cost 

## Approach
Initial state:
- Starts with a frontier that contains an initial state
- Empty Explored states
Then repeat:
- If frontier is empty, no solution
- Remove a node from the frontier
- if node == goal state, return solution
- Add node to explored set
- expand node, add node to frontier if not in frontier or explored set