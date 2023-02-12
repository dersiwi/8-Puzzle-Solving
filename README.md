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
The following table contains the data i was interested in when developing this program. I used the configuration above to test both goal-configurations. (21.11.2022)

| Category                     | Goal_1        | Goal_2  |
| -------------------------    |:-------------:| :------:|
| Total nodes in tree*         |    3560       |   290   |
| Moves to reach goal config   |      26       |   20    |
| time  needed                 |       0.32s   |   0.11s |

*the total nodes are all nodes that have been added to the tree. 
 This includes the ones that have been explored, and the ones that have not been explored yet.
 
 ### Usage
 To use the program type
 ```
 python3 8puzzle.py [goal_config] [custom_starting_configuration]
 ```
 into your terminal. 
 
 #### [goal_config]
 Not optional.
 This describes the goal-configuration you want the solver to solve for. This parameter can either be 1 or 2.
 1 correspondes to Goal_1 and 2 correspondes to Goal_2, as described in the benchmark configuration.
 
 #### [custom_starting_configuration]
 Optional. 
 Allows you to provide a custom starting configuration, a board you want to solve. 
 Provide the numbers from 0-8 in the order you want your board to be. The 0 correspondes to the empty field.
 Every 3 numbers, a new row on the board begins.
 Notice, that a configuration that is impossible to solve (depending on the goal-confiuration) keeps the program searching
 until it eventually explores all possible nodes - that however might take a while.
 
 #### Example
 ```
 python3 8puzzle.py 1 724506831
 ```
 runs the solver with Goal_1 as the goal-configuration and starting configuration used as the benchmark configuration.
