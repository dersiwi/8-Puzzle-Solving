# 8-Puzzle-Solving
Solve the 8-Puzzle-Problem using manhattan heuristic and A* tree search.

#### Benchmark configuration

```

Configuration        Goal_1            Goal_2

  7 | 2 | 4           | 1 | 2         1 | 2 | 3
  ---------         ---------         ---------
  5 |   | 6         3 | 4 | 5         4 | 5 | 6
  ---------         ---------         ---------
  8 | 3 | 1         6 | 7 | 8         7 | 8 | 
 ```
 
 

I implemented the search with Goal_1 as the desired Goal-Configuration. As i later foud out, Goal_2 is very wide spread as the Goal-Configuration.

#### Benchmarks
The following table contains the data i was interested in when developing this little program. I used the configuration above to test both programs. (21.11.2022)

| Category                     | Goal_1        | Goal_2  |
| -------------------------    |:-------------:| :------:|
| Total nodes in tree*         |    3560       |   290   |
| Moves to reach goal config   |      26       |   20    |
| time  needed                 |       0.32s   |   0.11s |

*the total nodes are all nodes that have been added to the tree. 
 This includes all nodes whoose children have been added to the tree, but also the ones whoose children have not been added to the tree yet.
 
 ### Usage
 To use the program type
 ```
 python3 8puzzle.py [goal_config]
 ```
 into your terminal. [goal_config] is either 1 or 2, depending on the goal-config you want to run.

