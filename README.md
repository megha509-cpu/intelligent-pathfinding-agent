## Hybrid Intelligent Agent for Route Selection under Uncertainty


# Overview

In real-world situations like navigation, there are often multiple routes between two locations. Some routes are shorter, some are faster, and others may have hidden costs like traffic or delays. Choosing the best route is not always straightforward.

In this project, I built a simple intelligent agent that explores different possible paths using multiple search algorithms. It then compares these results, selects the most suitable approach, and estimates how reliable that decision is using probability.



# Problem Statement

The problem addressed in this project is:

How can a system choose the best path when multiple options exist and conditions are uncertain?

This is similar to real-world navigation systems where different routes must be evaluated before making a decision.

# Concepts Used

- Breadth First Search (BFS)
- Depth First Search (DFS)
- A* Search Algorithm
- Hill Climbing
- Rule-Based Decision Making
- Bayesian Probability

# How the System Works

1. The environment is represented as a graph where nodes are locations and edges are paths.

2. The system applies different search algorithms:
   
   - BFS → Finds shortest path in terms of steps
   - DFS → Explores deeper paths first
   - A* → Uses cost and heuristic to find an efficient path
   - Hill Climbing → Chooses locally optimal moves

3. Each algorithm produces a path.

4. A rule-based function compares these paths and selects the most suitable one.

5. Bayesian probability is used to estimate confidence in the selected decision.


# How to Run

1. Open terminal in the project folder
2. Run the program:

python main.py


# Sample Output

BFS Path: ['A', 'C', 'E']
DFS Path: ['A', 'C', 'E']
A* Path: ['A', 'B', 'D', 'E']
Hill Climbing Path: ['A', 'C', 'E']

Chosen Algorithm: A*
Confidence (Bayesian): 0.84

# Observations

- BFS guarantees shortest path in terms of steps
- DFS may not always give optimal results
- A* provides efficient and optimal paths using heuristic
- Hill Climbing is fast but may get stuck in local optimum

This comparison highlights how different algorithms behave under the same conditions.

# Real-World Relevance

This project is inspired by systems like GPS navigation and delivery routing, where multiple routes are evaluated based on distance, cost, and uncertainty such as traffic conditions.



# Limitations

- Works on a small predefined graph
- Heuristic values are manually defined
- No real-time data
- Hill climbing may not reach global optimum

# Future Improvements

- Add dynamic conditions like traffic simulation
- Improve decision-making logic
- Use real-world datasets
- Add graphical visualization
