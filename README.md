# RL-Sandbox
Experimentation bed to get the team familiarized with RL

## Gridworld environment
This repository contains an implementation of a simple gridworld environment to test if an RL algorithm is working correctly. The environment consists of a (n,n) grid. The objective is to reach the destination square, which can either be set to a fixed position or randomized. The observation is the (x,y) coordinates of the destination square. There are 4 possible actions in the action space: up, down, left, and right. The agent receives a -1 reward at each time step, regardless of the action.

The gridworld class implements two functions: reset() and step()

* __init__(grid_dim, randomize_goal, goal_position) - Initializes the RL environment
  * Arguments:
    * grid_dim - Dimension of the grid world, default: (10,10)
    * randomize_goal - Whether or not to randomize the goal square when the environment is reset, default: False
    * goal_position - If the goal is not randomized, the fixed position of the goal, default: (9,9)

* reset() - Resets the RL environment to start a new simulation
  * Return
    * observation - The initial observation for the RL environment

* step(action) - Moves the RL enviroment forward 1 time step:
  * Arguments:
    * action - The action selected by agent
  * Return
    * observation - The observation for the next time step
    * reward - The reward received for the action
    * done - Boolean describing whether the agent has completed the task
