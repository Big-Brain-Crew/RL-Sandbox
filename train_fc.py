# Import environment
from fc_env import FCEnv

# Import baselines
from stable_baselines.common.policies import MlpPolicy, MlpLstmPolicy, MlpLnLstmPolicy
from stable_baselines.common import make_vec_env
from stable_baselines import PPO2

# multiprocess environment
env = FCEnv()

model = PPO2(MlpPolicy, env, verbose=1, tensorboard_log = "/data/tensorboard")
model.learn(total_timesteps=1000)
model.save("ppo2-fc")