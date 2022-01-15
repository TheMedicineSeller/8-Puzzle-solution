# 8-Puzzle-solution

This directory includes a simple solution to the 8-tiles board puzzle problem in python.

The 8 puzzle problem involves a board with 8 tiles numbered from one to eight and an empty tile. An initial board configuration (the initial state) is given. The tiles are to be rearranged so that the board could reach a final goal state (which is also specified). The problem asks to output a sequence of board states that lead up to the goal state from the initial one.

![image](https://user-images.githubusercontent.com/87657352/149614642-65e50fa9-9cba-4f77-b76f-0fbcd6df52f6.png)

The solution uses bfs to generate a tree (or graph) of board states with the children nodes to the parent node being all possible permutations (left, right, up and down shift) applied on the parent. The tree is generated until the parent node visited is equivalent to the goal state.
