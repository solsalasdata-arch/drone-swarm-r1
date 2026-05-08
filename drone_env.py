import gymnasium as gym
from gymnasium import spaces
import numpy as np

class DroneSwarmEnv(gym.Env):
    def __init__(self):
        super(DroneSwarmEnv, self).__init__()
        self.grid_size = 10
        # Acción: 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha
        self.action_space = spaces.Discrete(4)
        # Observación: Posición [x, y] del dron
        self.observation_space = spaces.Box(low=0, high=self.grid_size-1, shape=(2,), dtype=np.int32)
        
        self.state = np.array([0, 0]) # Inicio
        self.goal = np.array([9, 9])  # Meta
        self.obstacle = np.array([5, 5]) # Obstáculo estático [cite: 18, 19]

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.array([0, 0])
        return self.state.astype(np.float32), {}

    def step(self, action):
        # Mover el dron según la acción
        if action == 0 and self.state[1] < self.grid_size - 1: self.state[1] += 1
        elif action == 1 and self.state[1] > 0: self.state[1] -= 1
        elif action == 2 and self.state[0] > 0: self.state[0] -= 1
        elif action == 3 and self.state[0] < self.grid_size - 1: self.state[0] += 1

        # Lógica de Recompensas [cite: 19]
        done = np.array_equal(self.state, self.goal)
        truncated = False
        
        if done:
            reward = 100  # Éxito: meta alcanzada 
        elif np.array_equal(self.state, self.obstacle):
            reward = -50 # Penalización: choque con obstáculo 
            done = True
        else:
            reward = -1 # Penalización por tiempo/paso

        return self.state.astype(np.float32), reward, done, truncated, {}
