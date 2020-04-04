import numpy as np

class GridWorld():

    def __init__(self, grid_dim = (10,10), randomize_goal = False, goal_position = (9,9)):

        if(not randomize_goal):
            # Check that the goal position is a valid position on the grid
            assert goal_position[0] < grid_dim[0] and goal_position[0] >= 0
            assert goal_position[1] < grid_dim[1] and goal_position[1] >= 0

        # Save environment parameters
        self.grid_dim = np.array(grid_dim)
        self.randomize_goal = randomize_goal
        self.goal_position = np.array(goal_position)

    def __observation__(self):
        # Observation is the current agent state concatenated with the position of the goal
        return [self.state[0], self.state[1], self.goal_position[0], self.goal_position[1]]


    # Action should be an integer from 0-3 inclusive
    def __take_action__(self, action):
        # Left
        # If on left edge of grid, do nothing
        if(action == 0):
            if(self.state[0] > 0):
                self.state[0] -= 1

        # Right
        # If on right edge of grid, do nothing
        elif(action == 1):
            if(self.state[0] < self.grid_dim[0] - 1):
                self.state[0] += 1

        # Up
        # If on top edge of grid, do nothing
        elif(action == 2):
            if(self.state[1] > 0):
                self.state[1] -= 1

        # Down
        # If on left edge of grid, do nothing
        elif(action == 4):
            if(self.state[1] < self.grid_dim[1] - 1):
                self.state[1] += 1

    def __reward__(self):
        self.total_reward -= 1
        return -1


    def reset(self):
        # Initialize the state of the agent to be (0,0)
        self.state = np.array((0,0))

        # Count of the number of steps
        self.steps = 0

        # Count of the total reward
        self.total_reward = 0

        # If randomize_goal is true, choose a random location for the goal
        # Ensure that the goal position is not the starting position
        if(self.randomize_goal):
            goal_position = np.array([np.random.randint(0, self.grid_dim[0]), np.random.randint(0, self.grid_dim[1])])

            while(goal_position != self.state):
                goal_position = np.array([np.random.randint(0, self.grid_dim[0]), np.random.randint(0, self.grid_dim[1])])

        return self.__observation__()

    # Step environment forward one time step
    # Returns observation, reward, done, and info
    def step(self, action):
        # Take action
        self.__take_action__(action)
        reward = self.__reward__()

        self.steps += 1

        # Check if goal is reached
        done = (self.state == self.goal_position)

        # If done, compile stats about the simulation
        info = {
            "steps" : self.steps,
            "total_reward" : self.total_reward
        }

        return self.__observation__(), self.__reward__(), done, info

    def print_state(self):






