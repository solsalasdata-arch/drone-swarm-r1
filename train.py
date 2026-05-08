from stable_baselines3 import PPO
from drone_env import DroneSwarmEnv

# Instanciar el entorno
env = DroneSwarmEnv()

# Definir el modelo de Deep RL (Red Neuronal)
model = PPO("MlpPolicy", env, verbose=1)

print("Iniciando entrenamiento del enjambre...")
model.learn(total_timesteps=10000)

# Guardar el modelo entrenado
model.save("ppo_drone_swarm_model")
print("Modelo guardado exitosamente.")

# Prueba rápida
obs, _ = env.reset()
for _ in range(10):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    print(f"Posición actual: {obs}, Recompensa: {reward}")
    if done:
        break
