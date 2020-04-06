from gymfc.envs.fc_env import FlightControlEnv
import gym


class FCEnv(FlightControlEnv, gym.Env):
    def __init__(self, aircraft_config = "/data/solo/model.sdf", config=None, verbose=False):
        super().__init__(aircraft_config, config_filepath=config, verbose=verbose)