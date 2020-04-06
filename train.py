# Import environment
from gridworld import GridWorld

# Import baselines
from stable_baselines.common.policies import MlpPolicy, MlpLstmPolicy, MlpLnLstmPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import ACKTR

# multiprocess environment
env = GridWorld()

model = ACKTR(MlpPolicy, env, verbose=1, tensorboard_log = "/data/tensorboard")
model.learn(total_timesteps=1000)
model.save("acktr-gridworld")